############################################################
# Dockerfile to build Python Environment Reader
############################################################

# Set the base image to Python:2
FROM python:2

# File Author / Maintainer
MAINTAINER Rolind Roy

# Setting working directory
WORKDIR /usr/src/app

# Add a sample script file
ADD secret-reader.py /usr/src/app/

# Setting Environment variable to print output in dit mode
# https://stackoverflow.com/questions/43969743/logs-in-kubernetes-pod-not-showing-up
ENV PYTHONUNBUFFERED=0

# Executing python script
CMD [ "python", "./secret-reader.py", "secretKey" ]
