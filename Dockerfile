# syntax=docker/dockerfile:1

FROM python:3.9.19-bookworm

RUN \
    apt-get -y update && \
    apt-get -y install \
        sshpass

RUN \
    pip3 install --upgrade pip && \
    pip3 install \
        ansible==8.7.0 \
        ansible-core==2.15.11 \
        requests \
        jmespath \
        elasticsearch==8.13.2

RUN \
    ansible-galaxy collection install \
        community.docker \
        community.elastic

WORKDIR /etc/ansible

COPY --chmod=755 \
    bin/container-init.sh \
    /bin/container-init.sh

COPY ansible/ ./
