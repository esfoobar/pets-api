#
# Flaskbook-API Dockerfile
#
#

# Pull base image.
FROM centos:7.2.1511

# Build commands
ENV PYTHONUNBUFFERED 1
RUN yum -y update; yum clean all
RUN yum install -y epel-release; yum clean all
RUN yum install -y gcc gcc-c++ python34 python34-devel ImageMagick-devel; yum clean all
RUN echo -e "[mongodb-org-3.0] \n\
name=MongoDB Repository \n\
baseurl=http://repo.mongodb.org/yum/redhat/\$releasever/mongodb-org/3.0/x86_64/ \n\
gpgcheck=0 \n\
enabled=1" >> /etc/yum.repos.d/mongodb-org-3.0.repo
RUN yum install -y mongodb-org; yum clean all
RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN /usr/bin/python3.4 get-pip.py
RUN mkdir /opt/pets-api
WORKDIR /opt/pets-api
ADD requirements.txt /opt/pets-api/
RUN python3 -m pip install -r requirements.txt
ADD . /opt/pets-api

# start the app server
CMD python3 manage.py runserver
