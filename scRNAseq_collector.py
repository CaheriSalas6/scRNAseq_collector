# Importar las librerías necesarias
from flask import Flask, request, jsonify
import requests
import os
import logging
from dotenv import load_dotenv
import re
import ftplib
import shutil

# Cargar variables de entorno para mayor seguridad
load_dotenv()
API_KEY = os.getenv("NCBI_API_KEY")

# Crear la instancia de la app Flask
app = Flask(__name__)

# Configuración de seguridad
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = False
app.secret_key = os.urandom(24)  # Clave secreta para proteger cookies y sesiones

# Configurar logging seguro
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger()

# Endpoints base de NCBI
NCBI_BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
NCBI_FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

# Función para validar entradas (sanitización)
def sanitize_input(user_input):
    return re.sub(r'[^a-zA-Z0-9_ ]', '', user_input)

# Ruta principal para buscar datos RNA-seq de hipocampo del cerebro
@app.route('/fetch_rnaseq_data', methods=['POST'])
def fetch_rnaseq_data():
    try:
        # Obtener los parámetros de búsqueda desde la solicitud
        data = request.get_json()
        organism = sanitize_input(data.get('organism', ''))
        tissue = sanitize_input(data.get('tissue', 'hippocampus'))
        data_type = sanitize_input(data.get('data_type', 'rna-seq'))

        if not organism:
            return jsonify({"error": "Organism field is required."}), 400

        # Construir la consulta segura para NCBI
        query = f"{organism} {tissue} {data_type}"
        params = {
            'db': 'gds',
            'term': query,
            'retmode': 'json',
            'api_key': API_KEY
        }

        # Hacer la solicitud al endpoint de búsqueda de NCBI
        response = requests.get(NCBI_BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        result = response.json()

        # Procesar los IDs de los estudios encontrados
        id_list = result.get('esearchresult', {}).get('idlist', [])
        if not id_list:
            return jsonify({"message": "No data found for the specified query."}), 404

        # Obtener detalles de cada estudio encontrado
        details = []
        for study_id in id_list:
            fetch_params = {
                'db': 'gds',
                'id': study_id,
                'retmode': 'xml',
                'api_key': API_KEY
            }
            fetch_response = requests.get(NCBI_FETCH_URL, params=fetch_params, timeout=10)
            fetch_response.raise_for_status()
            details.append(fetch_response.text)

        # Definir la ruta de descarga
        base_dir = '/home/caheri_salas/db_scRNAseq'

        # Verificar si el directorio existe
        if os.path.exists(base_dir):
            user_input = input(f"El directorio {base_dir} ya existe. ¿Deseas sobrescribirlo? (s/n) o crear una nueva carpeta (escribe el nombre de la nueva carpeta): ")
            if user_input.lower() == 's':
                shutil.rmtree(base_dir)
                os.makedirs(base_dir)
            elif user_input.lower() == 'n':
                return jsonify({"message": "Operación cancelada por el usuario."}), 200
            else:
                new_dir = os.path.join('/home/caheri_salas', user_input)
                os.makedirs(new_dir, exist_ok=True)
                base_dir = new_dir
        else:
            os.makedirs(base_dir)

        # Descargar los archivos FTP de cada estudio
        for idx, study in enumerate(details, start=1):
            # Buscar la URL de descarga FTP en el XML
            ftp_url_match = re.search(r'ftp://[^"]+', study)
            if ftp_url_match:
                ftp_url = ftp_url_match.group(0)
                logger.info(f"Descargando desde: {ftp_url}")

                # Conectar al servidor FTP y descargar los archivos
                ftp = ftplib.FTP("ftp.ncbi.nlm.nih.gov")
                ftp.login()
                ftp.cwd(ftp_url.replace("ftp://ftp.ncbi.nlm.nih.gov/", ""))

                files = ftp.nlst()
                study_dir = os.path.join(base_dir, f'study_{idx}')
                os.makedirs(study_dir, exist_ok=True)

                for file in files:
                    local_filepath = os.path.join(study_dir, file)
                    with open(local_filepath, 'wb') as f:
                        ftp.retrbinary(f'RETR {file}', f.write)
                    logger.info(f"Archivo descargado: {local_filepath}")

                ftp.quit()

        return jsonify({"message": "All data fetched and saved successfully."}), 200

    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching data from NCBI: {e}")
        return jsonify({"error": "Failed to fetch data from NCBI."}), 500
    except ftplib.all_errors as e:
        logger.error(f"Error connecting to FTP: {e}")
        return jsonify({"error": "Failed to connect to FTP server."}), 500
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return jsonify({"error": "An unexpected error occurred."}), 500

# Medida de seguridad: limitar métodos HTTP
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "API is running."}), 200

# Ejecutar la aplicación de Flask
if __name__ == '__main__':
    # Solo permitir conexiones locales (evitar exposición pública durante desarrollo)
    app.run(host='127.0.0.1', port=5000, debug=False)

# Instrucciones de instalación de Flask
# Para instalar Flask, ejecuta el siguiente comando:
# pip install Flask python-dotenv requests
