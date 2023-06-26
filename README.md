# LDAP3
Pasos para configurar un servidor LDAP en GitHub Codespaces utilizando Docker



## Crea un repositorio de GitHub

Si aún no tienes un repositorio, puedes crear uno desde la página principal de GitHub. Recuerda inicializar el repositorio con un archivo README para que se cree la estructura del directorio del repositorio.

## Agrega un archivo Dockerfile o docker-compose.yml a tu repositorio

Para configurar un servidor LDAP en un contenedor Docker, puedes utilizar un archivo Dockerfile o un archivo docker-compose.yml. Aquí, usaremos un archivo docker-compose.yml, que es más flexible y fácil de trabajar.

Crea un nuevo archivo en la raíz de tu repositorio y llámalo docker-compose.yml. Agrega el siguiente contenido a este archivo:
```version: '3'
services:
  openldap:
    image: osixia/openldap:1.4.0
    environment:
      LDAP_ORGANISATION: "MiOrganizacion"
      LDAP_DOMAIN: "miorganizacion.com"
      LDAP_ADMIN_PASSWORD: "admin"
    ports:
      - "389:389"
```

Este archivo define un servicio Docker llamado "openldap" que utiliza la imagen Docker osixia/openldap:1.4.0. La organización LDAP se configura como "MiOrganizacion", el dominio LDAP como "miorganizacion.com" y la contraseña del administrador LDAP como "admin". El puerto 389 del contenedor se expone para permitir la conexión con el servidor LDAP.

## Agrega un archivo .devcontainer.json

GitHub Codespaces utiliza el archivo .devcontainer.json para configurar el entorno de desarrollo del espacio de código. Este archivo debe residir en un directorio llamado .devcontainer en la raíz de tu repositorio. Aquí hay un ejemplo de cómo podría ser el archivo .devcontainer.json:

```
{
  "name": "Mi espacio de código",
  "dockerComposeFile": "../docker-compose.yml",
  "service": "openldap",
  "workspaceFolder": "/workspace",
  "forwardPorts": [389]
}
```

Esto dice que GitHub Codespaces debe iniciar el contenedor definido en docker-compose.yml, conectar al servicio "openldap", y reenviar el puerto 389 del contenedor al mismo puerto en el espacio de código.

## Abre tu espacio de código en GitHub Codespaces

Dirígete a tu repositorio en GitHub y haz clic en el botón "Code" en la parte superior derecha de la página. Selecciona "Open with Codespaces" y luego "New codespace".



GitHub Codespaces configurará automáticamente tu entorno de desarrollo de acuerdo a los archivos .devcontainer.json y docker-compose.yml en tu repositorio.

Esos son los pasos básicos para configurar un servidor LDAP en GitHub Codespaces. Recuerda que puedes cambiar la configuración del servidor LDAP según tus necesidades modificando el archivo docker-compose.yml.

En base a tus requisitos, necesitas una configuración que instale Python y la librería ldap3, además de un servicio de OpenLDAP usando Docker Compose. A continuación, te proporciono una configuración de ejemplo.

Primero, deberías tener un archivo docker-compose.yml en la raíz de tu repositorio. Aquí te dejo un ejemplo de cómo debería verse:
``` version: '3'
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    volumes:
      - .:/workspace
  openldap:
    image: osixia/openldap:1.4.0
    environment:
      LDAP_ORGANISATION: "MiOrganizacion"
      LDAP_DOMAIN: "miorganizacion.com"
      LDAP_ADMIN_PASSWORD: "admin"
    ports:
      - "389:389"
```
Luego, debes tener un archivo .devcontainer/devcontainer.json en tu repositorio. Aquí te dejo un ejemplo de cómo debería verse:
```
{
  "name": "Mi espacio de código",
  "dockerComposeFile": "../docker-compose.yml",
  "service": "app",
  "workspaceFolder": "/workspace",
  "forwardPorts": [389],
  "postCreateCommand": "pip install ldap3",
  "extensions": ["ms-python.python"]
}
```
Finalmente, necesitarás un Dockerfile en la raíz de tu repositorio que construya tu servicio app. Aquí te dejo un ejemplo de cómo podría verse:
```
FROM mcr.microsoft.com/vscode/devcontainers/python:3.9

# Evita las preguntas durante la instalación
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get -y install --no-install-recommends apt-utils dialog 2>&1 \
    && apt-get -y install iproute2 procps iproute2 lsb-release \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*
```
Estos archivos configuran un entorno de desarrollo en Codespaces que incluye un servidor OpenLDAP y una aplicación Python que tiene la librería ldap3 instalada.
