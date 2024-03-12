from decouple import config

server=config('dbconnection')
database=config("DBName")
username=config("DBUser")
password=config("DBPass")

# from dotenv import load_dotenv
# import os

# load_dotenv()
# server=os.environ['dbconnection']
print(server)
version='18'
# WRconnection = (
#     f'DRIVER=DRIVER=ODBC Driver 18 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password};')


WRconnection = (
    f'DRIVER=ODBC Driver 18 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes;Encrypt=no;Connection Timeout=30;')


def Commandparam(input):
    pass