echo [$(date)]: "START"
echo [$(date)]: "creating conda virtual env"
conda create --prefix ./venv python=3.8 -y
echo [$(date)]: "activating conda virtual env"
source activate ./venv
echo [$(date)]: "installing dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "END"



# conda create -p .venv python=3.8 -y
# source activate .venv
# pip install -r requirements_dev.txt
