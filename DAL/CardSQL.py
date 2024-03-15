from Entity.DTO.WsInput import CardandChartInput
import pyodbc 
from DAL import DBConfig


def commonInputDBParam(input:CardandChartInput):  
        param=''
        if(input.ChartValueOption!=''):
            param +=f" @ChartValueOption='{input.ChartValueOption}',"
        if(input.strCompanyID!=''):
            param +=f" @CommaSeperate_CompanyID='{input.strCompanyID}',"
        if(input.strBranchID!=''):
            param +=f" @CommaSeperate_BranchID='{input.strBranchID}',"
        if(input.FromDate!=''):
            param +=f" @FromDate='{input.FromDate}',"
        if(input.ToDate!=''):
            param +=f" @ToDate='{input.ToDate}',"
        if(input.strDepartmentID!=''):
            param +=f" @CommaSeperate_DepartmentID='{input.strDepartmentID}',"
        if(input.strBrandID!=''):
            param +=f" @CommaSeperate_BrandID='{input.strBrandID}',"
        if(input.strProductID!=''):
            param +=f" @CommaSeperate_ProductID='{input.strProductID}',"
        if(input.strItemGroupID!=''):
            param +=f" @CommaSeperate_ItemGroupID='{input.strItemGroupID}',"
        if(input.strItemID!=''):
            param +=f" @CommaSeperate_ItemID='{input.strItemID}',"
        if(input.strDesignID!=''):
            param +=f" @CommaSeperate_DesignID='{input.strDesignID}',"
        if(input.strColorID!=''):
            param +=f" @CommaSeperate_ColorID='{input.strColorID}',"
        if(input.strSeasonID!=''):
            param +=f" @CommaSeperate_SeasonID='{input.strSeasonID}',"
        if(input.strSalesmanID!=''):
            param +=f" @CommaSeperate_SalesmanID='{input.strSalesmanID}',"
        param +=f" @TranType='A'"
        return  param
    
    
    
def GetStockCard(input:CardandChartInput):
    key_value_pairs=[]
    param=''
    drivers = [item for item in pyodbc.drivers()]
    print('driver',drivers)
    connection=pyodbc.connect(DBConfig.WRconnection)
    try:
        cursor=connection.cursor()        
               
        param=commonInputDBParam(input)
       
        cursor.execute(f"EXEC WR_RawData_GetSalesCardData  {param}")
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        
        for row in rows:
            key_value_pairs.append(dict(zip(columns, row)))
        cursor.close()
        connection.close()
    except Exception as e:
            connection.close()
    return key_value_pairs


def GetProfiteCard(input:CardandChartInput):
    key_value_pairs=[]
    param=''
    drivers = [item for item in pyodbc.drivers()]
    print('driver',drivers)
    connection=pyodbc.connect(DBConfig.WRconnection)
    try:
        cursor=connection.cursor()        
               
        param=commonInputDBParam(input)
        print(f"EXEC WR_RawData_GetProfiteCardData  {param}")
        cursor.execute(f"EXEC WR_RawData_GetProfiteCardData  {param}")
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


def GetSalesCard(input:CardandChartInput):
    key_value_pairs=[]
    param=''
    drivers = [item for item in pyodbc.drivers()]
    print('driver',drivers)
    connection=pyodbc.connect(DBConfig.WRconnection)
    try:
        cursor=connection.cursor()        
               
        param=commonInputDBParam(input)
       
        cursor.execute(f"EXEC WR_RawData_GetSalesRevenueCardData {param}")
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        
        for row in rows:
            key_value_pairs.append(dict(zip(columns, row)))
        cursor.close()
        connection.close()
    except Exception as e:
            connection.close()
    return key_value_pairs