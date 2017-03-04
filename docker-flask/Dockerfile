FROM ubuntu:16.10
MAINTAINER William Falcon <will@hacstudios.com>

ENV DEBIAN_FRONTEND noninteractive

# install linux deps
RUN apt-get update && apt-get install -y \
    python-pip python-dev uwsgi-plugin-python \
    nginx supervisor


COPY nginx/flask.conf /etc/nginx/sites-available/
COPY supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY app /var/www/app

RUN mkdir -p /var/log/nginx/app /var/log/uwsgi/app /var/log/supervisor
RUN rm /etc/nginx/sites-enabled/default
RUN ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN pip install -r /var/www/app/requirements.txt
RUN chown -R www-data:www-data /var/www/app
RUN chown -R www-data:www-data /var/log

# starts supervisor given the apps in the config file
CMD ["/usr/bin/supervisord"]
