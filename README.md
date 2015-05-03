# API Athens Meetup

This code was developed for the [Workshop Organised](www.meetup.com/API-Athens/events/221967177/) at the National Technical University of Athens.

First you need all the requirements, that can be directly installed with the following the command,

```
pip install -r requirements.txt
```

To build the example server,you can simply run the command 

```
gunicorn apimeetup.wsgi
```

or 

```
python manage.py runserver
```

The client code is within the client folder.


