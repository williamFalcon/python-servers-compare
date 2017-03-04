FROM ubuntu:16.10
MAINTAINER William Falcon <will@hacstudios.com>

ENV DEBIAN_FRONTEND noninteractive

# ------------------------
# BASIC SYSTEM SETUP
# ------------------------
# install linux deps
RUN apt-get update && apt-get install -y python-pip python-dev curl git

# ----------------------
# DB DRIVERS (OPTIONAL)
# needed to install psycopg2 succesfully
# ----------------------
RUN apt-get install -y libpq-dev

# ------------------------
# DATA SCIENCE STACK
# miniconda et al.
# ------------------------
# Install miniconda to /miniconda
ENV MINICONDA_VERSION 3-4.2.12
RUN echo "export PATH=/opt/conda/bin:$PATH" > /etc/profile.d/conda.sh
RUN curl -fSL https://repo.continuum.io/miniconda/Miniconda${MINICONDA_VERSION}-Linux-x86_64.sh -o ~/miniconda.sh
RUN /bin/bash ~/miniconda.sh -b -p /opt/conda
RUN rm ~/miniconda.sh

ENV PATH /opt/conda/bin:$PATH
RUN conda create --name python3_4 python=3.4

# ---------------------------
# SETUP FOLDER STRUCTURE AND APP DEPS
# ---------------------------
# install python deps
RUN mkdir -p /usr/src/app
COPY app/requirements.txt /usr/src/app/requirements.txt
RUN /bin/bash -c ". activate python3_4 && pip install -r  /usr/src/app/requirements.txt"

# ---------------------------
# RUN APP
# ---------------------------
# set up application after all the heavy installs so we don't rebuild image
# every time we change code
COPY app /usr/src/app

EXPOSE 80

CMD /bin/bash -c "source activate python3_4 && python /usr/src/app/app.py"