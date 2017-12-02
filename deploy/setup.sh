#!/usr/bin/env bash

# update packages (python & nginx)
echo "Update the server and install core libraries"
sudo apt-get update -y
sudo apt-get install python-pip python-dev nginx -y
sudo apt-get install supervisor -y

# install python 3
sudo apt-get install python3-pip python3-dev -y

# setup odbc in linux
echo "Setup odbc in linux"
sudo /var/www/todo-api/deploy/odbc/install.sh

# setup locales
echo "Setup locales"
sudo locale-gen --purge en_US.UTF-8
sudo echo -e 'LANG="en_US.UTF-8"\nLANGUAGE="en_US:en"\n' > /etc/default/locale

# update pip and install virtualenv
echo "Virtualenv and PIP"
sudo pip install --upgrade pip
sudo pip install virtualenv

# create vm
sudo virtualenv -p python3 /var/.envs/todo-api/

# install requirements.txt
echo "Install our app"
sudo /var/.envs/todo-api/bin/pip install -r /var/www/todo-api/requirements.txt

# setup nginx (copy setup and reload)
echo "Setup nginx"
sudo rm /etc/nginx/sites-enabled/default
sudo cp /var/www/todo-api/deploy/nginx.conf /etc/nginx/sites-available/todo-api.conf
sudo ln -s /etc/nginx/sites-available/todo-api.conf /etc/nginx/sites-enabled/todo-api.conf
sudo /etc/init.d/nginx reload

# supervisor
echo "Setup supervisor"
sudo cp /var/www/todo-api/deploy/supervisor.conf /etc/supervisor/conf.d/todo-api.conf

sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start todo-api

echo "We are the champions my friend !!!"
