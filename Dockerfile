FROM ubuntu

MAINTAINER Artur Kryshka "samoilenkoa7@gmail.com"
RUN apt-get update -qy
RUN apt-get install -qy python3.10 python3-pip python3.10-dev
COPY . ./code
WORKDIR /code
EXPOSE 8000
RUN pip install -r requirements.txt