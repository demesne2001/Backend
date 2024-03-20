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
        if(input.strSubCategory1ID!=''):
            param +=f" @CommaSeperate_SubCategory1ID='{input.strSubCategory1ID}',"
        if(input.strSubCategory2ID!=''):
            param +=f" @CommaSeperate_SubCategory2ID='{input.strSubCategory2ID}',"
        if(input.strSubCategory3ID!=''):
            param +=f" @CommaSeperate_SubCategory3ID='{input.strSubCategory3ID}',"
        if(input.strColorID!=''):
            param +=f" @CommaSeperate_ColorID='{input.strColorID}',"
        if(input.strSeasonID!=''):
            param +=f" @CommaSeperate_SeasonID='{input.strSeasonID}',"
        if(input.strSalesmanID!=''):
            param +=f" @CommaSeperate_SalesmanID='{input.strSalesmanID}',"
        if(input.strLotNo!=''):
            param +=f" @LotNo='{input.strLotNo}',"
        param +=f" @TranType='A'"
        return  param

def GetSalesAging(input:CardandChartInput):
    key_value_pairs=[]
    param=''
    drivers = [item for item in pyodbc.drivers()]
    print('driver',drivers)
    connection=pyodbc.connect(DBConfig.WRconnection)
    try:
        cursor=connection.cursor()        
               
        param=commonInputDBParam(input)
        print('SQL Query',f"EXEC WR_DashBoard_SalesAnalysis_AgeingReport {param}")
        cursor.execute(f"EXEC WR_DashBoard_SalesAnalysis_AgeingReport  {param}")
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        
        for row in rows:
            key_value_pairs.append(dict(zip(columns, row)))
        cursor.close()
        connection.close()
    except Exception as e:
            connection.close()
    return key_value_pairs

def GetMrpWiseRPT(input:CardandChartInput):
    key_value_pairs=[]
    param=''
    drivers = [item for item in pyodbc.drivers()]
    print('driver',drivers)
    connection=pyodbc.connect(DBConfig.WRconnection)
    try:
        cursor=connection.cursor()         
        param=commonInputDBParam(input) 
        
      
        print('SQL Query',f"EXEC WR_DashBoard_SalesAnalysis_MrpWiseReport {param}")
        cursor.execute(f"EXEC WR_DashBoard_SalesAnalysis_MrpWiseReport {param}")
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        
        for row in rows:
            key_value_pairs.append(dict(zip(columns, row)))
        cursor.close()
        connection.close()
    except Exception as e:
            connection.close()
    return key_value_pairs

def GetTopSalesmanBySales(input:CardandChartInput):
    key_value_pairs=[]
    param=''
    drivers = [item for item in pyodbc.drivers()]
    print('driver',drivers)
    connection=pyodbc.connect(DBConfig.WRconnection)
    try:
        cursor=connection.cursor()         
        param=commonInputDBParam(input) 
        
    
        print('SQL Query',f"EXEC WR_DashBoard_SalesAnalysis_TopSalesman {param}")
        cursor.execute(f"EXEC WR_DashBoard_SalesAnalysis_TopSalesman {param}")
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        
        for row in rows:
            key_value_pairs.append(dict(zip(columns, row)))
        cursor.close()
        connection.close()
    except Exception as e:
            connection.close()
    return key_value_pairs

def GetTopsellingproduct(input:CardandChartInput):
    key_value_pairs=[]
    param=''
    drivers = [item for item in pyodbc.drivers()]
    print('driver',drivers)
    connection=pyodbc.connect(DBConfig.WRconnection)
    try:
        cursor=connection.cursor()         
        param=commonInputDBParam(input) 
      
        print('SQL Query',f"EXEC WR_DashBoard_SalesAnalysis_TopProduct {param}")
        cursor.execute(f"EXEC WR_DashBoard_SalesAnalysis_TopProduct  {param}")
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

def GetSalesRevenue(input:CardandChartInput):
    key_value_pairs=[]
    param=''
    drivers = [item for item in pyodbc.drivers()]
    print('driver',drivers)
    connection=pyodbc.connect(DBConfig.WRconnection)
    try:
        cursor=connection.cursor()         
        param=commonInputDBParam(input) 
        
    
        print('SQL Query',f"EXEC WR_DashBoard_SalesAnalysis_SalesRevenue {param}")
        cursor.execute(f"EXEC WR_DashBoard_SalesAnalysis_SalesRevenue {param}")
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

def GetHourlySales(input:CardandChartInput):
    key_value_pairs=[]
    param=''
    drivers = [item for item in pyodbc.drivers()]
    print('driver',drivers)
    connection=pyodbc.connect(DBConfig.WRconnection)
    try:
        cursor=connection.cursor()         
        param=commonInputDBParam(input)
        if(input.ExtraVar!="" ): 
            param +=f",@ChartShownAs='{input.ExtraVar}'" 
        print('SQL Query',f"EXEC WR_DashBoard_SalesAnalysis_Hourly {param}")
        cursor.execute(f"EXEC WR_DashBoard_SalesAnalysis_Hourly  {param}")
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

def GetTopsupplierbysales(input:CardandChartInput):
    key_value_pairs=[]
    param=''
    drivers = [item for item in pyodbc.drivers()] 
    connection=pyodbc.connect(DBConfig.WRconnection)
    try:
        cursor=connection.cursor()         
        param=commonInputDBParam(input) 
        
        print('SQL Query',f"EXEC WR_DashBoard_SalesAnalysis_TopParty {param}")
        cursor.execute(f"EXEC WR_DashBoard_SalesAnalysis_TopParty {param}")
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        print('result',rows)
        
        for row in rows:
            key_value_pairs.append(dict(zip(columns, row)))
        cursor.close()
        connection.close()
    except Exception as e:
        print(e)
        connection.close()
    return key_value_pairs