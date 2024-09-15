# codigon para iniciar el proyecto

- **Paso 1**: python -m venv entorno_django
- **Paso 2**: pip install djangorestframework
- **Paso 3**: crear la carpeta vacia migrations y __pycache__  dentro de backend_so
- **Paso 4**: python manage.py makemigrations
- **Paso 5**: python manage.py migrate
- **Paso 6**: python manage.py makemigrations backend_so
- **Paso 7**: python manage.py migrate backend_so 
- **Paso 8**: python manage.py createsuperuser
- **Paso 9**: python manage.py runserver

# codigo para deploy cel proyecto
- python manage.py collectstatic

# codigo para correr el proyecto en local
- **Paso 1**: entorno_django\Scripts\activate
- **Paso 2**: python manage.py runserver
 **Paso 3**: ruta del panel administrativo  http://127.0.0.1:8000/admin/ y los endpoints son http://127.0.0.1:8000/api/productos,etc segun el modelo


 # codigo para traer los cambios del repo
- **Paso 1**:  git add .
- **Paso 2**: git commit -m "nombre de tu cambio que hiciste"
 **Paso 3**: git pull origin main 



