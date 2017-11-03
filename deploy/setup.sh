#!/usr/bin/env bash

# Actualizar los paquetes de python e instalacion del servidor web
sudo apt-get update -y
sudo apt-get install python-pip python-dev nginx -y

# Instalacion de python 3
sudo apt-get install python3-pip python3-dev nginx -y

# Configuracion de locales
sudo locale-gen --purge en_US.UTF-8
sudo echo -e 'LANG="en_US.UTF-8"\nLANGUAGE="en_US:en"\n' > /etc/default/locale

# Actualizar pip e instalar virtualenv
sudo pip install --upgrade pip
sudo pip install virtualenv

# Crear entorno virtual
sudo virtualenv -p python3 /var/.envs/todo-api/
