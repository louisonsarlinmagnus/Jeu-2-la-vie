# syntax=docker/dockerfile:1
FROM python:3
MAINTAINER Louison SARLIN--MAGNUS

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1

#Move the requirement from the directory into the container
COPY ./requirements.txt /requirements.txt
#Installing the requirements detailled in the file located in the container
RUN pip install -r requirements.txt

#Creation of an app repo in the container
RUN mkdir /app 
#Switching to this repo
WORKDIR /app
#Copying our local repo app to the one in the container
COPY ./app /app

#Creating a user to run the application
RUN useradd django
#Swithcing to that user
USER django

# EXPOSE 8000

# CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]