echo [$(date)]: "START"


# echo [$(date)]: "creating env with python 3.11.3 version" 

# conda create --prefix /opt/conda/envs/env python=3.11.3


# echo [$(date)]: "activating the environment" 

source activate /opt/conda/envs/env

echo [$(date)]: "installing the dev requirements" 

pip install -r requirements.txt

echo [$(date)]: "END"