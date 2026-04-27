# syntax=docker/dockerfile:1

FROM python:3.9.19-bookworm

RUN \
    apt -y update && \
    apt -y install \
        sshpass \
        jq

RUN \
    pip3 install --upgrade pip && \
    pip3 install \
        ansible==8.7.0 \
        ansible-core==2.15.11 \
        requests \
        jmespath \
        elasticsearch==8.13.2 \
        docker \
        hvac \
        passlib

RUN \
    ansible-galaxy collection install \
        community.docker \
        community.elastic \
        --force

WORKDIR /etc/ansible

COPY --chmod=755 \
    bin/ /bin/

COPY ansible/ ./
