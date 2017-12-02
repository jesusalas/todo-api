#!/usr/bin/env bash

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
