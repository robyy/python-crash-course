# Django practice project for Python Crash Course 2nd

## Env
Python 3.8.1
Django 3.0.4

### Potential Issue
Check your local env variable `echo $DJANGO_SETTINGS_MODULE`, if it's set, either remove it or change the name of learning_log and other path to match `$DJANGO_SETTINGS_MODULE`.

Another way to fix it is to specify the settings by: `python manage.py runserver --settings=config.settings` or `DJANGO_SETTINGS_MODULE=config.settings python manage.py runserver`
