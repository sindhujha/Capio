FROM ubuntu:latest
MAINTAINER Sindhujha "sethuras@usc.edu"
RUN apt-get update -y 
RUN apt-get install -y python-dev python-pip build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]