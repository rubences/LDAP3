FROM mcr.microsoft.com/vscode/devcontainers/python:3.9

# Evita las preguntas durante la instalación
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get -y install --no-install-recommends apt-utils dialog 2>&1 \
    && apt-get -y install iproute2 procps iproute2 lsb-release \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*
