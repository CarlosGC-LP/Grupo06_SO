# codigon para iniciar el proyecto

python -m venv entorno_django

pip install djangorestframework
python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations backend_so
python manage.py migrate backend_so 
python manage.py createsuperuser
python manage.py runserver

# codigo para correr el proyecot

entorno_django\Scripts\activate