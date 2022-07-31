## CHALLENGER MELI GOOGLE API

Esta API permite listar el contenido de un DRIVE, crear documentos (titulo y contenido), buscar si una palabra se encuentra en un determinado documento y borrar contenido del DRIVE

Desarrollado con Django-REST como backend. Enjoy :)

## Configuración del ambiente ##
Es necesario tener instalado python, pip, docker y docker-compose para seguir estos pasos.

Las herramientas descritas son fáciles de encontrar en la web, por lo que si no las tienes, las puedes instalar siguiendo los tutoriales de las paginas oficiales.

Este codigo esta testeado para python 3.8 Y 3.9, por lo cual se recomienda trabajar con estás versión.

Para levantar la API utilizaremos el archivo docker-compose.yml.
El cual posee las instrucciones para levantar la API en Django como, un servidor NGINX que servidira como proxy reverso.
```
docker-compose up -d
```

Instalamos las librerias del backend (es recomendable tener un gestor de ambientes para python):

```
cd backend
pip install -r requirements.txt
```

## Configuraciones backend ##
Si vas quieres levanatar la aplicacion desde consola, configura el archivo:
app/settings/develop.py

```
python backend/manage.py makemigrations
python backend/manage.py migrate
python backend/manage.py createsuperuser
```
## Para testear el backend ##
```
cd backend
python manage.py test
```

## Para levantar el backend ##
necesitamos dos terminales para esto.
```
cd backend
python manage.py runserver  # en una terminal
```


