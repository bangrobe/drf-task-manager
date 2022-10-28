FROM python:3.9.6-slim-buster

#SET ENVIRONMENT VARIABLES

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# #Another requirements to install to fix error
# RUN apk add --update --no-cache --virtual .tmp-build-deps \
#     gcc libc-dev linux-headers \
#     && apk add libffi-dev


# # install python gis  dependencies
# RUN apk update \
#     && apk add postgresql-dev python3-dev musl-dev    

RUN apt-get update \
    && apt-get -y install netcat musl-dev python3-dev gcc postgresql postgresql-client libpq-dev \
    && apt-get clean

RUN apt-get update \
    && apt-get install -y binutils libproj-dev


# Install dependencies
RUN pip install --upgrade pip

RUN mkdir /code
WORKDIR /code
COPY . /code

RUN pip install -r requirements.txt

# Set work directory



# Copy the Django project


# RUN mkdir /var/run/uwsgi

# RUN chown -R www-data:www-data /var/run/uwsgi

RUN mkdir /scripts

COPY ./wait-for-it.sh /scripts
RUN chmod +x /scripts/wait-for-it.sh


# COPY ./uwsgi_params /scripts
# RUN chmod +x /scripts/uwsgi_params

COPY ./start /scripts
RUN chmod +x /scripts/start
RUN sed -i 's/\r$//g' /scripts/start
# RUN chmod 777 /scripts


