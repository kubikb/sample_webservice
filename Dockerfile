# Let's start with a sample ubuntu image
FROM ubuntu:vivid
MAINTAINER Balint Kubik (kubikb@starschema.net)

# Install dependencies
RUN apt-get update && \
    apt-get install -y python2.7 python-pip && \
    pip install flask

# Exposing webservice port
EXPOSE 5000

# Add the PYthon script
ADD webservice.py /sample_ws/webservice.py

# Start the WS Python script
ENTRYPOINT ["python", "/sample_ws/webservice.py"]