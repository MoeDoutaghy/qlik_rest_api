# Using lightweight alpine image

FROM centos:centos7

RUN yum -y install epel-release && yum clean all

RUN yum -y install python-pip && yum clean all

# Defining working directory and adding source code

COPY . /app

WORKDIR /app

# Installing required packages

RUN pip install -r requirements.txt

# Start app

EXPOSE 5000

ENTRYPOINT ["/app/flask-startup.sh"]