FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential iputils-ping wget curl dnsutils
COPY . /
WORKDIR /app
RUN pip install flask
ENV FLASK_APP app/main.py
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]

