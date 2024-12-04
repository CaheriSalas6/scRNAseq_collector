wsl
sudo apt-get install pip
quit() clear
sudo apt-get install pip
clear
pip --version
sudo apt update
sudo apt install python3 python3-pip
pip3 --version
cd ~
wget https://repo.anaconda.com/archive/Anaconda3-latest-Linux-x86_64.sh
wget Anaconda3-latest-Linux-x86_64.sh
wget https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh
sha256sum Anaconda3-latest-Linux-x86_64.sh
sha256sum Anaconda3-2024.10-1-Linux-x86_64.sh
bash Anaconda3-2024.10-1-Linux-x86_64.sh
conda init
jupyter-noteboock
clear 
where conda
source ~/.bashrc
conda --version
~/anaconda3/bin/conda init
source ~/.bashrc
conda --version
flas --version 
flask --version 
http://127.0.0.1:5000
http://127.0.0.1:500
clear
sudo apt update
sudo apt upgrade
sudp apt install python3-venv
sudo apt install python3-venv
python3 -m venv development
source development/bin/activate
nano ~/.bashrc
source ~/.bashrc
ls 
cd ~/development
rm -rf development
cd
ls 
rm -rf development
ls 
python3 -m venv apis_csn
nano ~/.bashrc
apis_csn
source ~/.bashrc
nano ~/.bashrc
source ~/.bashrc
apis_csn
pip install Flask python-dotenv requests
pip install --upgrade pip
clear
jupyter-notebook 
apis_csn
curl -X POST -H "Content-Type: application/json" -d '{"organism": "Homo sapiens", "tissue": "hippocampus", "data_type": "rna-seq"}' http://127.0.0.1:5000/fetch_rnaseq_data
git init
git add .
clear
git commit -m "First commit fro the scRNAseq_collector"
git config --global user.email "csalas.navarrete@gmail.com"
git config --global user.name "CaheriSalas6"
git commit -m "First commit fro the scRNAseq_collector"
git remote add origin https://github.com/CaheriSalas6/scRNAseq_collector.git
git branch -M main
git push -u origin main
git remote set-url origin git@github.com:CaheriSalas6/scRNAseq_collector.git
git push -u origin main
ssh-add -l
eval "$(ssh-agent -s)"
ssh-add -l
ssh-keygen -t ed25519 -C "csalas.navarrete@gmail.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
ssh-add -l
cat ~/.ssh/id_ed25519.pub
git push -u origin main
git pull origin main --rebase
git add .
git rebase --continue
git push -u origin main
clear
ls -la
touch .gitignore
nano .gitignore
clear
ls
git add README.md api_RNAseq_collector.ipynb ncbi_rnaseq_data.xml 
git commit -m "Adding just working files to repo"
git push -u origin main
# Ignorar entornos virtuales y archivos grandes innecesarios
/env/
/venv/
/anaconda3/
*.pyc
__pycache__/
*.ipynb_checkp
nano .gitignore
git add README.md api_RNAseq_collector.ipynb ncbi_rnaseq_data.xml 
git push -u origin main
sudo apt-get install git-lfs
git lfs install
git lfs track "*.xml"
git add .gitattributes
git add ncbi_rnaseq_data.xml
git commit -m "Añadir archivo XML con Git LFS"
git push -u origin main
nano .gitignore
git rm -r --cached anaconda3
git rm --cached ncbi_rnaseq_data
git commit -m "Eliminar archivos grandes e innecesarios del historial"
git add .gitignore
git add -u
git commit -m "Eliminar archivos grandes e innecesarios del historial"
git push -u origin main
git rev-list --objects --all | sort -k 2 | git cat-file --batch-check='%(objectname) %(objectsize) %(rest)' | sort -n -k 2 | tail -10
nano .gitignore
sudo apt-get install git-filter-repo
git filter-repo --path anaconda3 --invert-paths
git filter-repo --path anaconda3 --invert-paths --force
git status
git push -u origin main --force
git remote add origin git@github.com:CaheriSalas6/scRNAseq_collector.git
git remote -v
git push -u origin main --force
git filter-repo --path "Anaconda3-2024.10-1-Linux-x86_64.sh" --invert-paths --force
git status
git rev-list --objects --all | sort -k 2 | git cat-file --batch-check='%(objectname) %(objectsize) %(rest)' | sort -n -k 2 | tail -10
git push -u origin main --force
git filter-repo --path ".ssh/id_ed25519" --invert-paths --force
git status
git rev-list --objects --all | sort -k 2 | git cat-file --batch-check='%(objectname) %(objectsize) %(rest)' | sort -n -k 2 | tail -10
git push -u origin main --force
ls
jupyter-notebook 
touch scRNAseq_collector.py
notepad scRNAseq_collector.py 
notepad.exe scRNAseq_collector.py 
python3 scRNAseq_collector.py 
