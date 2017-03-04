FROM ubuntu:16.10
MAINTAINER William Falcon <will@hacstudios.com>

ENV DEBIAN_FRONTEND noninteractive

# ------------------------
# BASIC SYSTEM SETUP
# ------------------------
# install linux deps
RUN apt-get update && apt-get install -y \
    python-pip python-dev uwsgi-plugin-python \
    nginx supervisor curl

# ------------------------
# INSTALL SERVER STACK
# Nginx, uwsgi, supervisor
# ------------------------
COPY nginx/flask.conf /etc/nginx/sites-available/
COPY supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN mkdir -p /var/log/nginx/app /var/log/uwsgi/app /var/log/supervisor
RUN rm /etc/nginx/sites-enabled/default
RUN ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# ------------------------
# DATA SCIENCE STACK
# miniconda et al.
# ------------------------
# Install miniconda to /miniconda
#RUN curl -LO http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh
#RUN bash Miniconda-latest-Linux-x86_64.sh -p /miniconda -b
#RUN rm Miniconda-latest-Linux-x86_64.sh
#ENV PATH=/miniconda/bin:${PATH}
#RUN conda update -y conda

# ---------------------------
# INSTALL FLASK AND APP DEPS
# Nginx, uwsgi, supervisor
# ---------------------------
# install python deps
COPY app/requirements.txt /var/www/app/requirements.txt
RUN pip install -r /var/www/app/requirements.txt

# ---------------------------
# RUN APP
# Nginx, uwsgi, supervisor
# ---------------------------
# set up application after all the heavy installs so we don't rebuild image
# every time we change code
COPY app /var/www/app
RUN chown -R www-data:www-data /var/www/app
RUN chown -R www-data:www-data /var/log

# starts supervisor given the apps in the config file
CMD ["/usr/bin/supervisord"]
