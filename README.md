# this is my end to end project

## Usefull Conda commands
| First Header  | Second Header |
| ------------- | ------------- |
| Get a list of all your environments  | conda env list  |
| Get a list of all the packages installed in your current active environment  | conda list  |
| Create an environment called [ENV_NAME]  | conda create --name [ENV_NAME]  |
| Create an environment called [ENV_NAME] and install pandas and numpy  | conda create --name [ENV_NAME] pandas numpy  |
| Activate an environment called [ENV_NAME]  | conda activate [ENV_NAME]  |
| Create an environment folder called env in the current working directory (e.g. /Users/Daniel/project_1/) and install pandas and numpy  | conda create --prefix ./env pandas numpy  |
| Activate an environment stored in a folder called env which is located within /Users/Daniel/project_1/  | conda activate /Users/daniel/project_1/env  |
| Deactivate an environment  | conda deactivate  |
| Export your current active environment to a YAML file called environment (see why below)  | conda env export > environment.yaml  |
| Export an environment stored at /Users/Daniel/project_1/env as a YAML file called environment (see why below)  | conda env export --prefix /Users/Daniel/project_1/env > environment.yaml  |
| Create an environment from a YAML file called environment (see why below)  | conda env create --file environment.yaml  |
| Install a new package [PACKAGE_NAME] in a target environment (while the target environment is active)  | conda install [PACKAGE_NAME]  |
| Delete an environment called [ENV_NAME]  | conda env remove --name [ENV_NAME]  |
| Delete an environment stored at /Users/Daniel/project_1/env  | conda remove --prefix /Users/Daniel/project_1/env --all  |
|   |   |
|   |   |
|   |   |


## setup the env for WINDOWS and DOCKER
- Create a folder in local. 
- sync/create repo in repository. 
- run in cmd => docker run -i -t -p 8888:8888 -v <LOCAL_FOLDER_PATH>:/home --name <ENV_NAME> phenomback/conda-env:latest /bin/bash
  To run the puthon files in your local vscode by pointing to container, we need to create the volume to the path "/opt/conda/envs".
  To attach the container to vscode => ctrl+p and choose the "dev Containers: Attach to Running Container..." and then attach the container.
- create the init_setup.sh (Creating conda env and installing the dependancies) 
- create the requirements.txt file. 
- open the container in bash SHELL. "docker exec -it <CONTAINER_ID> bash"
- go to home inside container and run the sh file. (sh init_setup.sh OR bash init_setup.sh)

- When you want to open the env later, 1st open the container SHELL in bash and activate the env with full path. ex: conda activate /opt/conda/envs/env



