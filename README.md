# Hello, please read the steps

[![Updates](https://pyup.io/repos/github/Lucas-far/attempt_api/shield.svg)](https://pyup.io/repos/github/Lucas-far/attempt_api/)
[![Python 3](https://pyup.io/repos/github/Lucas-far/attempt_api/python-3-shield.svg)](https://pyup.io/repos/github/Lucas-far/attempt_api/)
[![Build Status](https://travis-ci.org/Lucas-far/project_django_id_1.svg?branch=main)](https://travis-ci.org/Lucas-far/project_django_id_1)

- Download dependencies -> pip install -r requirements.txt
- You probably need to create a virtual environment
- I normally do it as "python3 -m venv .venv" and activate it through "source .venv/bin/activate"

Notes

- This project uses mysql, configured at "pp.seetings"
- In "settings.py", go to var "DATABASES"
- You will see:

[this variable](pa/static/images/databases.png)

- These functions are there to avoid showing personal data
- Therefore, create at the root of the project, a python file
- My advice for the name is: "mysql_data.py"
- If you return to "pp.settings.py" you will see the import "from mysql_data import *"
- This means, all functions have been imported to "pp.settings.py"

[the methods](pa/static/images/methods.png)

OPTIONAL (test)
- I recommend testing if your data is actually being shown 
- The steps below take into account if you are logged into your virtual environment, in the root path of your project
- python manage.py shell
- from pp.settings import DATABASES
- DATABASES (printing the variable through terminal)
- If you can see your data, then things are set correctly

DJANGO COMMANDS THAT MAY BE NEEDED
- python manage.py makemigrations (create tables)
- python manage.py migrate (create migrations)
- python manage.py createsuperuser (create user to login in development or production) (http://127.0.0.1:8000/admin)
- python manage.py runserver (run development server) (http://127.0.0.1:8000/)
