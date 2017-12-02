#!/usr/bin/env bash

# update packages (python & nginx)
echo "####################"
echo "Update the server and install core libraries"
echo "####################"
sudo apt-get update -y
sudo apt-get install python-pip python-dev nginx -y
sudo apt-get install supervisor -y

# install python 3
sudo apt-get install python3-pip python3-dev -y

# setup locales
echo "####################"
echo "Setup locales"
echo "####################"
sudo locale-gen --purge en_US.UTF-8
sudo echo -e 'LANG="en_US.UTF-8"\nLANGUAGE="en_US:en"\n' > /etc/default/locale

# setup odbc in linux
echo "####################"
echo "Installing mssql tools"
echo "####################"
sudo curl -s https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
sudo curl -s https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

sudo apt-get update -y
sudo ACCEPT_EULA=Y apt-get install msodbcsql -y
sudo apt-get install libodbc1-utf16 unixodbc-utf16 odbcinst1debian2-utf16 unixodbc-dev-utf16 -y #this step is optional but recommended*
sudo ACCEPT_EULA=Y apt-get install mssql-tools -y

# Create symlinks for tools
sudo ln -sfn /opt/mssql-tools/bin/sqlcmd-13.0.1.0 /usr/bin/sqlcmd
sudo ln -sfn /opt/mssql-tools/bin/bcp-13.0.1.0 /usr/bin/bcp

echo "####################"
echo "Installing dependencies for pyodbc"
echo "####################"
sudo apt-get update -y
sudo apt-get install python-pyodbc unixodbc-dev unixodbc-bin unixodbc -y

echo "####################"
echo "Installing Dependencies"
echo "####################"
sudo apt-get install libssl1.0.0 libgss3 -y
sudo ldconfig

sudo cp -f /var/www/todo-api/deploy/odbc/odbc.ini /etc/odbc.ini
sudo cp -f /var/www/todo-api/deploy/odbc/odbcinst.ini /etc/odbcinst.ini

# update pip and install virtualenv
echo "####################"
echo "Virtualenv and PIP"
echo "####################"
sudo pip install --upgrade pip
sudo pip install virtualenv

# create vm
sudo virtualenv -p python3 /var/.envs/todo-api/

# install requirements.txt
echo "####################"
echo "Install our app"
echo "####################"
sudo /var/.envs/todo-api/bin/pip install -r /var/www/todo-api/requirements.txt

# setup nginx (copy setup and reload)
echo "####################"
echo "Setup nginx"
echo "####################"
sudo rm /etc/nginx/sites-enabled/default
sudo cp /var/www/todo-api/deploy/nginx.conf /etc/nginx/sites-available/todo-api.conf
sudo ln -s /etc/nginx/sites-available/todo-api.conf /etc/nginx/sites-enabled/todo-api.conf
sudo /etc/init.d/nginx reload

# supervisor
echo "####################"
echo "Setup supervisor"
echo "####################"
sudo cp /var/www/todo-api/deploy/supervisor.conf /etc/supervisor/conf.d/todo-api.conf

sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start todo-api

echo "We are the champions my friend !!!"
