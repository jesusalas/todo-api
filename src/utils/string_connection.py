import urllib.parse

def convert_rfc1738_to_string():
    DB_CONNECTION = "DRIVER={ODBC Driver 13 for SQL Server};Database=todo-api-dev;Server=192.168.1.121;UID=sa;PWD=root;Port=1433;Trusted_Connection=no;"
    DB_CONNECTION = urllib.parse.quote_plus(DB_CONNECTION)
    DB_CONNECTION = "mssql+pyodbc:///?odbc_connect=%s" % DB_CONNECTION

    return DB_CONNECTION

print(convert_rfc1738_to_string())
