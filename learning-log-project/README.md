# Django practice project for Python Crash Course 2nd

## Env
Python 3.8.1
Django 3.0.4

### Issue
For some reason, had to name the project as `config`: `django-admin startproject config .`, and create a module `settings_dev.py`(can copy the content from default `settings.py`), or will always get `ModuleNotFoundError: No module named 'config'` error. Tried to test with lower version of python and django, no luck, might be just my local env issue though.
