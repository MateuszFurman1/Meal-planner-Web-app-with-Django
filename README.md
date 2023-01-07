

clone repository
go to Settings-> Project-> Python Interpreter-> add interpreter-> add local interpreter
terminal: pip install -r requirements.txt
create local_settings.py file like bellow in main directory: DATABASES = { 'default': { 'HOST': '127.0.0.1', 'NAME': 'conferencebookingroom', 'ENGINE': 'django.db.backends.postgresql', 'USER': '#user name for ur database', 'PASSWORD': '#password for ur database', } }
open pgadmin and type create database conferenceBookingRoom
terminal: python manage.py migrate
terminal: python manage.py runserver
go to http://127.0.0.1:8000
