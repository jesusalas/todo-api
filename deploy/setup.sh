#!/usr/bin/env bash

# update packages (python & nginx)
sudo apt-get update -y
sudo apt-get install python-pip python-dev nginx -y
sudo apt-get install supervisor -y

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

# install requirements.txt
sudo /var/.envs/todo-api/bin/pip install -r /var/www/todo-api/requirements.txt

# setup nginx (copy setup and reload)
sudo rm /etc/nginx/sites-enabled/default
sudo cp /var/www/todo-api/deploy/nginx.conf /etc/nginx/sites-available/todo-api.conf
sudo ln -s /etc/nginx/sites-available/todo-api.conf /etc/nginx/sites-enabled/todo-api.conf
sudo /etc/init.d/nginx reload

# supervisor
sudo cp /var/www/todo-api/deploy/supervisor.conf /etc/supervisor/conf.d/todo-api.conf

sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start todo-api
