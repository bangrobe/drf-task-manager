FROM python:3.10.0-slim-buster

#Set maintainer

LABEL maintainer='bangrobe@gmail.com'
LABEL yotube="bangdigi"
LABEL description="Development image for Task Manager Project"

#SET ENVIRONMENT VARIABLES

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Another requirements to install to fix error
RUN apt-get update \
  && apt-get install -y build-essential \
  && apt-get install -y libpq-dev \
  && apt-get install -y gettext \
  && apt-get -y install netcat gcc postgresql \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# install psycopg2 dependencies
# RUN apk update \
#     && apk add postgresql-dev gcc python3-dev musl-dev


#Install dependancies
RUN pip3 install --upgrade pip
# copy requirements.txt to workdir

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt ./

#Install requirements
RUN pip install -r requirements.txt

# Delete temporary requirents
# RUN apk del .tmp-build-deps

# copy project
# COPY . /app


#dir for media

# RUN mkdir -p /vol/web/media
# RUN mkdir -p /vol/web/static
# # Add user to docker container
# RUN adduser -D user
# RUN chown -R user:user /app/
# RUN chown -R user:user /vol/web/


# RUN chmod -R 755 /app
# RUN chmod -R 755 /vol

#WAIT
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /wait
RUN chmod +x /wait

COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

