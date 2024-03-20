from Entity.DTO.WsInput import FilterInput
import pyodbc 
from DAL import DBConfig


def Getcompany(input:FilterInput):
    key_value_pairs=[]
    param=''
    drivers = [item for item in pyodbc.drivers()]
    print('driver',drivers)
    connection=pyodbc.connect(DBConfig.WRconnection)
    try:
        cursor=connection.cursor()  
        param +=f" @search='{input.search}'"
        cursor.execute(f"EXEC WR_mstCompany_GetForHelp {param}")
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        
        for row in rows:
            key_value_pairs.append(dict(zip(columns, row)))
        cursor.close()
        connection.close()
    except Exception as e:
            connection.close()
    return key_value_pairs

def GetBranch(input:FilterInput):
    key_value_pairs=[]
    param=''
    connection=pyodbc.connect(DBConfig.WRconnection)
    try:
        cursor=connection.cursor()
        param +=f" @search='{input.search}',"
        param +=f" @strCompanyID='{input.strCompanyID}'"
        cursor.execute(f"EXEC WR_mstBranch_GetForHelp {param}")
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        
        for row in rows:
            key_value_pairs.append(dict(zip(columns, row)))
        cursor.close()
        connection.close()
    except Exception as e:
            connection.close()
    return key_value_pairs

def GetDepartment(input:FilterInput):
    key_value_pairs=[]
    param=''
    connection=pyodbc.connect(DBConfig.WRconnection)
    try:
        cursor=connection.cursor()
        param +=f" @search='{input.search}'"
        cursor.execute(f"EXEC WR_mstDepartment_GetForHelp {param}")
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        
        for row in rows:
            key_value_pairs.append(dict(zip(columns, row)))
        cursor.close()
        connection.close()
    except Exception as e:
            connection.close()
    return key_value_pairs

def GetItemGroup(input:FilterInput):
    key_value_pairs=[]
    param=''
    connection=pyodbc.connect(DBConfig.WRconnection)
    try:
        cursor=connection.cursor()
        if(input.PageNo>0):
            param +=f" @PageNo={input.PageNo},"
        if(input.PageSize>0):            
            param +=f" @PageSize={input.PageSize},"      
        param +=f" @search='{input.search}'"
        cursor.execute(f"EXEC WR_mstItemGroup_GetForHelp {param}")
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        
        for row in rows:
            key_value_pairs.append(dict(zip(columns, row)))
        cursor.close()
        connection.close()
    except Exception as e:
            connection.close()
    return key_value_pairs

def GetBrand(input:FilterInput):
    key_value_pairs=[]
    param=''
    connection=pyodbc.connect(DBConfig.WRconnection)
    try:
        cursor=connection.cursor()
        if(input.PageNo>0):
            param +=f" @PageNo={input.PageNo},"
        if(input.PageSize>0):            
            param +=f" @PageSize={input.PageSize},"      
        param +=f" @search='{input.search}',"
        param +=f" @strBranchID='{input.strBranchID}'"
        cursor.execute(f"EXEC WR_mstBrand_GetForHelp {param}")
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        
        for row in rows:
            key_value_pairs.append(dict(zip(columns, row)))
        cursor.close()
        connection.close()
    except Exception as e:
            connection.close()
    return key_value_pairs

def GetSalesman(input:FilterInput):
    key_value_pairs=[]
    param=''
    connection=pyodbc.connect(DBConfig.WRconnection)
    try:
        cursor=connection.cursor()
        if (input.PageNo>0):
            param +=f" @PageNo={input.PageNo},"
        if (input.PageSize>0):
            param +=f" @PageSize={input.PageSize},"
        param +=f" @search='{input.search}',"
        param +=f" @strCompanyID='{input.strCompanyID}',"
        param +=f" @strBranchID='{input.strBranchID}'"
        
        cursor.execute(f"EXEC WR_mstSalesman_GetForHelp {param}")
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        
        for row in rows:
            key_value_pairs.append(dict(zip(columns, row)))
        cursor.close()
        connection.close()
    except Exception as e:
            connection.close()
    return key_value_pairs

def GetProduct(input:FilterInput):
    key_value_pairs=[]
    param=''
    connection=pyodbc.connect(DBConfig.WRconnection)
    try:
        cursor=connection.cursor()
        if (input.PageSize>0):
            param +=f" @PageSize={input.PageSize},"        
        if (input.PageNo>0):
            param +=f" @PageNo={input.PageNo},"
        param +=f" @search='{input.search}',"
        param +=f" @strDepartmentID='{input.strDepartmentID}'"
        print(f"EXEC WR_mstProduct_GetForHelp {param}")
        cursor.execute(f"EXEC WR_mstProduct_GetForHelp {param}")
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        
        for row in rows:
            key_value_pairs.append(dict(zip(columns, row)))
        cursor.close()
        connection.close()
    except Exception as e:
            connection.close()
    return key_value_pairs

def GetSeason(input:FilterInput):
    key_value_pairs=[]
    param=''
    connection=pyodbc.connect(DBConfig.WRconnection)
    try:
        cursor=connection.cursor()
        param +=f" @search='{input.search}'"
        cursor.execute(f"EXEC WR_mstSeason_GetForHelp {param}")
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        
        for row in rows:
            key_value_pairs.append(dict(zip(columns, row)))
        cursor.close()
        connection.close()
    except Exception as e:
            connection.close()
    return key_value_pairs

def GetFit(input:FilterInput):
    key_value_pairs=[]
    param=''
    connection=pyodbc.connect(DBConfig.WRconnection)
    try:
        cursor=connection.cursor()
        param +=f" @search='{input.search}'"
        cursor.execute(f"EXEC WR_mstSize_GetForHelp {param}")
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        
        for row in rows:
            key_value_pairs.append(dict(zip(columns, row)))
        cursor.close()
        connection.close()
    except Exception as e:
            connection.close()
    return key_value_pairs


def GetColor(input:FilterInput):
    key_value_pairs=[]
    param=''
    connection=pyodbc.connect(DBConfig.WRconnection)
    try:
        cursor=connection.cursor()
        if(input.PageNo>0):
            param +=f" @PageNo={input.PageNo},"
        if(input.PageSize>0):
            param +=f" @PageSize={input.PageSize},"
        param +=f" @search='{input.search}'"
      
        cursor.execute(f"EXEC WR_mstColor_GetForHelp {param}")
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        
        for row in rows:
            key_value_pairs.append(dict(zip(columns, row)))
        cursor.close()
        connection.close()
    except Exception as e:
            connection.close()
    return key_value_pairs

def GetItemName(input:FilterInput):
    key_value_pairs=[]
    param=''
    connection=pyodbc.connect(DBConfig.WRconnection)
    try:
        cursor=connection.cursor()
        if(input.PageNo>0):
            param +=f" @PageNo={input.PageNo},"
        if(input.PageSize>0):            
            param +=f" @PageSize={input.PageSize},"      
        param +=f" @search='{input.search}',"
        param +=f" @strCompanyID='{input.strCompanyID}',"
        param +=f" @strBranchID='{input.strBranchID}',"
        param +=f" @strBrandID='{input.strBrandID}',"
        param +=f" @strProductID='{input.strProductID}',"
        param +=f" @strItemGroupID='{input.strItemGroupID}',"        
        param +=f" @strDepartmentID='{input.strDepartmentID}'"
        cursor.execute(f"EXEC WR_mstItem_GetForHelp {param}")
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        
        for row in rows:
            key_value_pairs.append(dict(zip(columns, row)))
        cursor.close()
        connection.close()
    except Exception as e:
            connection.close()
    return key_value_pairs

def GetLotNo(input:FilterInput):
    key_value_pairs=[]
    param=''
    connection=pyodbc.connect(DBConfig.WRconnection)
    try:
        cursor=connection.cursor()
        if(input.PageNo>0):
            param +=f" @PageNo={input.PageNo},"
        if(input.PageSize>0):            
            param +=f" @PageSize={input.PageSize},"        
        param +=f" @search='{input.search}',"
        param +=f" @strCompanyID='{input.strCompanyID}',"
        param +=f" @strItemID='{input.strItemID}',"
        param +=f" @strDesignID='{input.strDesignID}',"
        param +=f" @strBranchID='{input.strBranchID}'"
        cursor.execute(f"EXEC WR_mstLotNo_GetForHelp {param}")
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        
        for row in rows:
            key_value_pairs.append(dict(zip(columns, row)))
        cursor.close()
        connection.close()
    except Exception as e:
            connection.close()
    return key_value_pairs

def GetDesign(input:FilterInput):
    key_value_pairs=[]
    param=''
    connection=pyodbc.connect(DBConfig.WRconnection)
    try:
        cursor=connection.cursor()
        if(input.PageNo>0):
            param +=f" @PageNo={input.PageNo},"
        param +=f" @search='{input.search}',"
        param +=f" @strCompanyID='{input.strCompanyID}',"
        param +=f" @strBranchID='{input.strBranchID}',"
        if(input.PageSize>0):            
            param +=f" @PageSize={input.PageSize},"      
        param +=f" @strItemID='{input.strItemID}'"
        print(f"EXEC WR_mstDesign_GetForHelp {param}")
        cursor.execute(f"EXEC WR_mstDesign_GetForHelp {param}")
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        
        for row in rows:
            key_value_pairs.append(dict(zip(columns, row)))
        cursor.close()
        connection.close()
    except Exception as e:
            print(e)
            connection.close()
    return key_value_pairs




        