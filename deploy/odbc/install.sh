#!/usr/bin/env bash

echo "Installing dependencies for pyodbc"
sudo apt-get install unixodbc-dev-utf16 -y
sudo apt-get install python-pyodbc -y

echo "Installing mssql tools"
sudo curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
sudo curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install msodbcsql=13.0.1.0-1 mssql-tools-14.0.2.0-1 -y
sudo apt-get install unixodbc-dev-utf16 -y #this step is optional but recommended*
# Create symlinks for tools
sudo ln -sfn /opt/mssql-tools/bin/sqlcmd-13.0.1.0 /usr/bin/sqlcmd
sudo ln -sfn /opt/mssql-tools/bin/bcp-13.0.1.0 /usr/bin/bcp

echo "Installing Dependencies"
sudo apt-get install libssl1.0.0
sudo apt-get install libgss3
sudo ldconfig

echo "Configure profile & bash"
sudo echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
sudo echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
sudo source ~/.bashrc

sudo cat /var/www/todo-api/deploy/odbc/odbc.ini > /etc/odbc.ini
sudo cat /var/www/todo-api/deploy/odbc/odbcinst.ini > /etc/odbcinst.ini
