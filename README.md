A. Clone the git repo in a local directory

B. Create a virtual environment
1. Install virtualenv via pip - pip install virtualenv
2. Install virtualenvwrapper - pip install virtualenvwrapper, export WORKON_HOME=~/Envs, source /usr/local/bin/virtualenvwrapper.sh
3. mkvirtualenv -p {path to python2 executable} {environment's name}
4. workon {environment's name}

C. Install the dependencies, pip install -r requirements.txt

D. Create a mysql database, create database {name}

E. Create local_settings.py by copying the local_settings.py.template file

F. Add the Database settings - NAME, USER, PASSWORD, HOST, PORT in the local_settings.py file

G. On command line navigate to directory containing the manage.py file and execute, python manage.py migrate.

H. Next execute, python manage.py runserver

I. Application can be accessed on localhost:8000 now.
