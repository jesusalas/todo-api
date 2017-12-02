import urllib.parse
from flask_sqlalchemy import SQLAlchemy


DB_CONNECTION = "DRIVER={ODBC Driver 13 for SQL Server};Database=todo-api-dev;Server=192.168.1.121;UID=sa;PWD=root;Port=1433;Trusted_Connection=no;"
DB_CONNECTION = urllib.parse.quote_plus(DB_CONNECTION)
DB_CONNECTION = "mssql+pyodbc:///?odbc_connect=%s" % DB_CONNECTION
print (DB_CONNECTION)
db = SQLAlchemy()
# DRIVER%3D%7BODBC+Driver+13+for+SQL+Server%7D%3BDatabase%3Dtodo-api-dev%3BServer%3D192.168.1.121%3BUID%3Dsa%3BPWD%3Droot%3BPort%3D1433%3BTrusted_Connection%3Dno%3B
