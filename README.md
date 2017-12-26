A. Create a virtual environment
1. Install virtualenv via pip - pip install virtualenv
2. Install virtualenvwrapper - pip install virtualenvwrapper, export WORKON_HOME=~/Envs, source /usr/local/bin/virtualenvwrapper.sh
3. mkvirtualenv -p {path to python2 executable} {name}
4. workon task

B. Install the dependencies, pip install -r requirements.txt

C. Create a mysql database, create database {name}

D. Create local_settings.py by copying the settings.py file

E. 
