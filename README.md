# this is my end to end project

## setup the env for WINDOWS and DOCKER
- Create a folder in local. 
- sync/create repo in repository. 
- run in cmd => docker run -i -t -p 8888:8888 -v <LOCAL_FOLDER_PATH>:/home --name <ENV_NAME> phenomback/conda-env:latest /bin/bash 
- create the init_setup.sh (Creating conda env and installing the dependancies) 
- create the requirements.txt file. 
- go to home inside container and run the sh file. (sh init_setup.sh)



