FROM python:3.8.3-alpine

ENV MICRO_SERVICE=/home/app/microservice
# set work directory
RUN mkdir -p $MICRO_SERVICE
RUN mkdir -p $MICRO_SERVICE/static

# where the code lives
WORKDIR $MICRO_SERVICE

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk del build-deps \
    && apk --no-cache add musl-dev linux-headers g++ \
    && apk add --no-cache \
        freetype-dev \
        libpng-dev \
        jpeg-dev \
        libjpeg-turbo-dev
# install dependencies
RUN pip install --upgrade pip
# copy project
COPY . $MICRO_SERVICE

RUN pip3 install -r requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade pip setuptools
RUN pip3 install whitenoise
RUN pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
RUN pip3 install tzdata
# Expose 8000
EXPOSE 8080
# Run APP
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--chdir", $MICRO_SERVICE, "api_meli.meli.wsgi"]  m