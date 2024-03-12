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
WRconnection = (
    f'DRIVER=DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password};')



def Commandparam(input):
    pass