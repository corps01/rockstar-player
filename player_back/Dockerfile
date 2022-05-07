# Set Python image
FROM python:3.10.4-bullseye
# Prevents infinite buffering
ENV PYTHONUNBUFFERED 1
# create root directory for our project in the container
RUN mkdir /usr/src/django/
RUN mkdir /usr/src/django/player_back
# Set the working directory to /player_back
WORKDIR /usr/src/django/player_back
# Copy the current directory contents into the container at /player_back
ADD . /usr/src/django/player_back
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt