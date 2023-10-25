@echo off
call venv\Scripts\activate
python manage.py shell < scripts.py
deactivate
