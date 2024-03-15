
import pyodbc 
from DAL import DBConfig
from Entity.DTO.WsInput import FilterInput

def GetParmCaption():
    key_value_pairs=[]    
    param=''
    result1=[]
    drivers = [item for item in pyodbc.drivers()]
    print('driver',drivers)
    connection=pyodbc.connect(DBConfig.WRconnection)
    try:
        cursor=connection.cursor()         
        param+=f"@strParmID='29,30,31'"      
        print('SQL Query',f"EXEC WR_AlphaParm_GetForHelp {param}")
        cursor.execute(f"EXEC WR_AlphaParm_GetForHelp  {param}")        
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        
        for row in rows:
            key_value_pairs.append(dict(zip(columns, row)))
        print(result1)   
        cursor.close()
        connection.close()
    except Exception as e:
        print(e)
        connection.close()
    return key_value_pairs

def GetSubCategory(input:FilterInput):
    key_value_pairs=[]    
    param=''
    result1=[]
    drivers = [item for item in pyodbc.drivers()]
    print('driver',drivers)
    connection=pyodbc.connect(DBConfig.WRconnection)
    try:
        cursor=connection.cursor()         
        if(input.PageNo>0):
            param +=f" @PageNo={input.PageNo},"
        if(input.PageSize>0):            
            param +=f" @PageSize={input.PageSize},"    
        if(input.SubCategoryNo>0 and input.SubCategoryNo<4):            
            param +=f" @SubCategoryNo={str(input.SubCategoryNo)},"     
        param +=f" @search='{input.search}'"
      
        print('SQL Query',f"EXEC WR_mstSubCategory_GetForhelp {param}")
        cursor.execute(f"EXEC WR_mstSubCategory_GetForhelp  {param}")        
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()        
        for row in rows:
            key_value_pairs.append(dict(zip(columns, row)))
        print(result1)   
        cursor.close()
        connection.close()
    except Exception as e:
        print(e)
        connection.close()
    return key_value_pairs