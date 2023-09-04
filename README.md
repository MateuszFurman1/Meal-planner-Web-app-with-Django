https://user-images.githubusercontent.com/106817902/220760794-3774e7c5-577f-4f48-bcfe-e7041772d822.mp4

## Key Features

* Add, edit and delete recipe
* Add, edit and delete plan
* Add, edit and delete recipe to plan

App, which user can add recipe, recipe to plans, plans, page and day name. Registration and login system are implemented. Users can manage his diet in simply and transparent way. First part of project had been done by team of 3 person while SRCUM lab on coderslab course. SCRUM lab simulated work in a team on one project and use git repository to share and resolve conflict with code.
Tools & technologies used in project:
python, django framework, postgreSQL, pytest, Bootstrap, HTML, CSS, Trello, pycharm

## How to run
* clone repository
* go to Settings-> Project-> Python Interpreter-> add interpreter-> add local interpreter
* terminal: pip install -r requirements.txt
* create local_settings.py file like bellow in main directory:
   DATABASES = {
      'default': {
          'HOST': '127.0.0.1',
          'NAME': 'conferencebookingroom',
          'ENGINE': 'django.db.backends.postgresql',
          'USER': '#user name for ur database',
          'PASSWORD': '#password for ur database',
      }
  }
* open pgadmin and type create database conferenceBookingRoom
* terminal: python manage.py migrate 
* terminal: python manage.py seed_db- to create dummy data
* terminal: python manage.py runserver
* go to http://127.0.0.1:8000/home/

## Requirements

* asgiref==3.6.0
* autopep8==2.0.1
* Django==4.1.5
* django-autoslug==1.9.8
* django-crispy-forms==2.0
* factory-boy==3.2.1
* Faker==17.0.0
* psycopg2-binary==2.9.5
* pycodestyle==2.10.0
* python-dateutil==2.8.2
* pytz==2022.5
* six==1.16.0
* sqlparse==0.4.3
