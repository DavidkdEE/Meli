[![build status](https://github.com/davidkdee/meli/workflows/Django-CI/badge.svg)](https://github.com/DavidkdEE/Meli/actions) 
## CHALLENGER MELI GOOGLE API
Desarrollado con Django-REST como backend. Enjoy :)

Esta API permite listar el contenido de un DRIVE, crear Google Docs (a partir de un título y contenido), buscar si una determinada palabra se encuentra contenido en un documento y borrar contenido del DRIVE.
Para el correcto funcionamiento de esta aplicación es necesario seguir los siguientes pasos.


## Configuración del ambiente ##
Antes de levantar la API es necesario que configures el archivo .env

Dicho archivo .env posee información de variables secretas que utilizara el proyecto y debe se copiado dentro de la carpeta raíz del proyecto llamada "api_meli".

```
ENV=test
USERNAME="nombre de usuario que se creara al levantar docker-compose"
PASSWORD="password del usuario"
CREDENTIALS=".json proporcionado por la api de google"
```

Es necesario tener instalado python, pip, docker y docker-compose para seguir estos pasos.
Las herramientas descritas son fáciles de encontrar en la web, por lo que si no las tienes, las puedes instalar siguiendo los tutoriales de las páginas oficiales.
Este código esta testeado para python 3.8 Y 3.9, por lo cual se recomienda trabajar con estás versiones.


## Levantar la API utilizando docker-compose ##
Para levantar la API utilizaremos el archivo docker-compose.yml.
* Es necesario el archivo secreto token.json copiado en el directorio "api_meli"
ejecutar en la raíz del repositorio el siguiente comando

```
docker-compose up -d
```
Puedes testear la API en la siguiente dirección: http://localhost/doc/


## Levantar la API utilizando python ##

Instalamos las librerías del backend (es recomendable poseer un gestor de ambientes para python):
```
pip install -r requirements.txt
```

## Configuraciones backend ##
Si quieres levantar la aplicación desde consola, copia el archivo .env adentro de la carpeta "api_meli"
```
python api_meli/manage.py makemigrations
python api_meli/manage.py migrate
python api_meli/manage.py add_user (esto creara un usuario a partir de las variables configuradas en tu .env)
```
## Para testear el backend ##
```
cd api_meli
python manage.py test
```

## Para levantar el backend ##
necesitamos dos terminales para esto.
```
cd api_meli
python manage.py runserver  # en una terminal
```
Puedes testear la API en la siguiente dirección: http://localhost:8000/doc/


