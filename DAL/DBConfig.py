from decouple import config
import pyodbc
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
#     f'DRIVER=SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}')

WRconnection = (
    f'DRIVER=ODBC Driver 18 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes;Encrypt=no;Connection Timeout=30;')


def spParam(input):
    newParam=""
    print(input)
    for i in input:
        if(type(i[1]) is int):
            if(i[1] > 0):              
                newParam+=f"@{i[0]}={i[1]},"
        elif(type(i[1]) is str):
            if(i[1]!=""):
                newParam+=f"@{i[0]}='{i[1]}',"
        if(type(i[1]) is bool):
            if(i[1]==False or i[1]==True):
                newParam+=f"@{i[0]}={i[1]},"
    result=','.join([s for s in newParam.split(',') if s])
    print(result)
    return result



def ExecuteDataReader(param,spname,MethodNname):    
    key_value_pairs=[]
    print(param)
    param=spParam(param)
    drivers = [item for item in pyodbc.drivers()]    
    wconnection=pyodbc.connect(WRconnection)
    try:
        cursor=wconnection.cursor()        
        cursor.execute(f"EXEC {spname} {param}")
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall() 
        for row in rows:
            key_value_pairs.append(dict(zip(columns, row)))
        print(key_value_pairs)
        cursor.close()        
    except Exception as e:
        print(MethodNname + 'Error :- ',e)
        print('SQL Query',f"EXEC {spname} {param}")
        print('driver',drivers)
    finally:
        wconnection.close()
    return key_value_pairs

def ExecuteNonQuery(input,spname,MethodNname):    
    param=""
    param=spParam(input)    
    ID=0
    drivers = [item for item in pyodbc.drivers()]    
    wconnection=pyodbc.connect(WRconnection)
    try:
        cursor=wconnection.cursor()             
        cursor.execute(f"EXEC {spname} {param}")        
        rows = cursor.fetchone() 
        print(rows)
        ID=rows[0]        
        cursor.commit()
    except Exception as e:
        print(MethodNname + 'Error :- ',e)
        print('SQL Query',f"EXEC {spname} {param}")
        print('driver',drivers)
        cursor.rollback()   
    finally:
        cursor.close()
        wconnection.close()
    return ID