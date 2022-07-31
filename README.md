[![build status](https://github.com/davidkdee/meli/workflows/Django-CI/badge.svg)](https://github.com/DavidkdEE/Meli/actions) 
## CHALLENGER MELI GOOGLE API

Esta API permite listar el contenido de un DRIVE, crear documentos (a partir de un titulo y contenido), buscar si una determinada palabra se encuentra contenido en el documento y borrar contenido del DRIVE.

Para el correcto funcionamiento de esta aplicación  es necesario seguir los siguientes pasos

Desarrollado con Django-REST como backend. Enjoy :)

## Configuración del ambiente ##
Antes de levantar la API es necesario que configures el archivo .env

Dicho archivo .env posee información de variables secretas que utilizara el proyecto.
dicho archivo debe ser copiado dentro de la carpeta raiz del proyecto llamada "api_meli"

```
ENV=test
USERNAME="nombre de usuario que se creara al levantar docker-compose"
PASSWORD="password del usuario"
CREDENTIALS=".json proporcionado por la api de google"
```


Es necesario tener instalado python, pip, docker y docker-compose para seguir estos pasos.

Las herramientas descritas son fáciles de encontrar en la web, por lo que si no las tienes, las puedes instalar siguiendo los tutoriales de las paginas oficiales.

Este codigo esta testeado para python 3.8 Y 3.9, por lo cual se recomienda trabajar con estás versiónes.


## Levantar la API utilizando docker-compose ##
Para levantar la API utilizaremos el archivo docker-compose.yml.
ejecutar en la raiz del repositorio el siguiente comando
```
docker-compose up -d
```

el sitio se encontrar disponinble en la direccion : http://localhost/doc/ (si quieres testear la API con interfaz grafica)


## Levantar la API utilizando python ##

Instalamos las librerias del backend (es recomendable poseer un gestor de ambientes para python):

```
cd api_meli
pip install -r requirements.txt
```

## Configuraciones backend ##
Si vas quieres levantar la aplicacion desde consola, copia el archivo .env dentro de api_meli

```
python backend/manage.py makemigrations
python backend/manage.py migrate
python backend/manage.py add_user (esto creara un usuario a partir de las variables configuradas en tu .env)
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


