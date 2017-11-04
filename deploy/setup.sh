#!/usr/bin/env bash

# update packages (python & nginx)
sudo apt-get update -y
sudo apt-get install python-pip python-dev nginx -y

# install python 3
sudo apt-get install python3-pip python3-dev nginx -y

# setup locales
sudo locale-gen --purge en_US.UTF-8
sudo echo -e 'LANG="en_US.UTF-8"\nLANGUAGE="en_US:en"\n' > /etc/default/locale

# update pip and install virtualenv
sudo pip install --upgrade pip
sudo pip install virtualenv

# create vm
sudo virtualenv -p python3 /var/.envs/todo-api/
