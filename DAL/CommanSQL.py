
import pyodbc 
from DAL import DBConfig
from Entity.DTO.WsInput import FilterInput
from Entity.DTO.WsResponse import SubCategoryResult

def GetParmCaption():
    key_value_pairs=[]    
    result=SubCategoryResult()
    param=''
    result1=[]
    drivers = [item for item in pyodbc.drivers()]
    print('driver',drivers)
    connection=pyodbc.connect(DBConfig.WRconnection)
    try:
        cursor=connection.cursor()         
        param+=f"@strParmID='29,30,31,1149,1150,1151,1152,1153,1154,1155'" 
        cursor.execute(f"EXEC WR_AlphaParm_GetForHelp  {param}")        
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        
        for row in rows:
            result.lstresult.append(dict(zip(columns, row)))

        print('Check condition 0')
        # if(cursor.nextset()):
        #     print('Check condition 1')
        DateR=[]        
        while True:
            DateR=cursor.fetchone()
            if cursor.nextset()==False:
                break
        
        a=1
        for row in DateR:
            print(row)
            if(a==1):
                result.FromDate=row
                a+=1
            else:
                result.ToDate=row
       
        cursor.close()
        connection.close()
    except Exception as e:
        print(e)
        connection.close()
    return result

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
        if(input.SubCategoryNo>0 ):            
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


