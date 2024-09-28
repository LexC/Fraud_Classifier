read -p 'MiniConda directory: ' miniconda
source $miniconda
conda create -n fraudclass python=3.10
conda activate fraudclass
pip install -r src/requirements.txt