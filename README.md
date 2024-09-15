# codigon para iniciar el proyecto

- **Paso 1**: python -m venv entorno_django
- **Paso 2**: entorno_django\Scripts\activate
- **Paso 3**: pip install djangorestframework
- **Paso 3**: pip install django
- **Paso 4**: pip install mysqclient
- **Paso 5**: crear la carpeta vacia "migrations" y "__pycache__"  dentro de backend_so
- **Paso 6**: python manage.py makemigrations
- **Paso 7**: python manage.py migrate
- **Paso 8**: python manage.py makemigrations backend_so
- **Paso 9**: python manage.py migrate backend_so 
- **Paso 10**: python manage.py createsuperuser
- **Paso 11**: python manage.py runserver

# codigo para deploy del proyecto
- python manage.py collectstatic

# codigo para correr el proyecto en local
- **Paso 1**: entorno_django\Scripts\activate
- **Paso 2**: python manage.py runserver
 **Paso 3**: ruta del panel administrativo  http://127.0.0.1:8000/admin/ y los endpoints son http://127.0.0.1:8000/api/productos,etc segun el modelo


 # codigo para traer los cambios del repo
- **Paso 1**:  git add .
- **Paso 2**: git commit -m "nombre de tu cambio que hiciste"
 **Paso 3**: git pull origin main 
hola





