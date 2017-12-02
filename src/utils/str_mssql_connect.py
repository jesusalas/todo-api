import urllib.parse
from colorama import Fore, Style

# Example
# DRIVER={ODBC Driver 13 for SQL Server};Database=todo-api-dev;Server=192.168.1.121;UID=sa;PWD=root;Port=1433;Trusted_Connection=no;
def convert_rfc1738_to_string(DB_CONNECTION):
    DB_CONNECTION = urllib.parse.quote_plus(DB_CONNECTION)
    DB_CONNECTION = "mssql+pyodbc:///?odbc_connect=%s" % DB_CONNECTION

    return DB_CONNECTION

if __name__ == "__main__":
    print (Fore.RED + "SQL Server: Replace special characters in string (using the %xx escape)")
    print(Style.RESET_ALL)
    source = input("Put the string connection: \n")
    print("\n" + Fore.RED + "RESULT:")
    print(Fore.GREEN + convert_rfc1738_to_string(source))
    print(Style.RESET_ALL)
