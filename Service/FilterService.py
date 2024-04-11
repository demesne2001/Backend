from Entity.DTO.WsInput import FilterInput,AddEditFilterGrid,GetByID
from Entity.DTO.WsResponse import FilterResult
from DAL import FilterSQL ,DBConfig 

def GetDesignservice(input:FilterInput):
    result=FilterResult()
    try:
        result.lstResult=FilterSQL.GetDesign(input)
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result

def GetLotNo(input:FilterInput):
    result=FilterResult()
    try:
        result.lstResult=FilterSQL.GetLotNo(input)
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result

def GetFilterGridByID(input:GetByID):
    result=FilterResult()
    try:
        print(input.ID)
        result.lstResult=DBConfig.ExecuteDataReader(input,"WR_mstFilterGrid_GetBYID","GetFilterGridByID")
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result

def FilterGridAddEdit(input:AddEditFilterGrid):
    result=FilterResult()
    if(input.FilterGrid==''):
        result.Message.append("FilterGrid Required")
    elif(input.FilterID<=0):
        result.Message.append("FilterID Required")
    if(len(result.Message)==0):
        try:
            ID=0
            ID=DBConfig.ExecuteNonQuery(input,"WR_mstFilterGrid_AddEdit","GetFilterGridByID")
            if(ID>0):
                result.Message.append("FilterGrid Updated Sucessfully")
            elif(ID == -1):
                result.Message.append("Already Have it...!")
            elif(ID ==-5):
                result.Message.append("Contact To Backend Developer")
                result.HasError=True
            
        except  Exception as E:
            result.HasError=True
            result.Message.append(E)
    else:
        result.HasError=True
    return result


def GetItemName(input:FilterInput):
    result=FilterResult()
    try:
        result.lstResult=FilterSQL.GetItemName(input)
    except  Exception as E:
        print(E)
        result.HasError=True
        result.Message.append(E)
    return result

def GetColor(input:FilterInput):
    result=FilterResult()
    try:
        result.lstResult=FilterSQL.GetColor(input)
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result

def GetFit(input:FilterInput):
    result=FilterResult()
    try:
        result.lstResult=FilterSQL.GetFit(input)
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result

def GetSeason(input:FilterInput):
    result=FilterResult()
    try:
        result.lstResult=FilterSQL.GetSeason(input)
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result

def GetProduct(input:FilterInput):
    result=FilterResult()
    try:
        result.lstResult=FilterSQL.GetProduct(input)
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result

def GetSalesman(input:FilterInput):
    result=FilterResult()
    try:
        result.lstResult=FilterSQL.GetSalesman(input)
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result

def GetBrand(input:FilterInput):
    result=FilterResult()
    try:
        result.lstResult=FilterSQL.GetBrand(input)
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result

def GetItemGroup(input:FilterInput):
    result=FilterResult()
    try:
        result.lstResult=FilterSQL.GetItemGroup(input)
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result

def GetDepartment(input:FilterInput):
    result=FilterResult()
    try:
        result.lstResult=FilterSQL.GetDepartment(input)
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result

def GetBranch(input:FilterInput):
    result=FilterResult()
    try:
        result.lstResult=FilterSQL.GetBranch(input)
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result

def Getcompany(input:FilterInput):
    result=FilterResult()
    try:     
        
        result.lstResult=FilterSQL.Getcompany(input)       
    except  Exception as E:
        print(E)
        result.HasError=True
        result.Message.append(E)
    return result

def GetCity(input:FilterInput):
    result=FilterResult()
    try:        
        sp=f"WR_mstCity_GetForHelp @strstateName='{input.strState}',@PageSize={input.PageSize},@PageNo={input.PageNo},@search='{input.search}'"   
        result.lstResult=FilterSQL.GetcommanWithoutParam(sp)       
    except  Exception as E:
        print(E)
        result.HasError=True
        result.Message.append(E)
    return result

def GetState(input:FilterInput):
    result=FilterResult()
    try:   
        sp=f"WR_mstState_GetForHelp @PageSize={input.PageSize},@pageNo={input.PageNo},@search='{input.search}'"     
        result.lstResult=FilterSQL.GetcommanWithoutParam(sp)       
    except  Exception as E:
        print(E)
        result.HasError=True
        result.Message.append(E)
    return result

def GetRegion(input:FilterInput):
    result=FilterResult()
    try:        
        sp=f"WR_mstRegion_GetForHelp @PageSize={input.PageSize},@pageNo={input.PageNo},@search='{input.search}',@strState='{input.strState}',@strCity='{input.strCity}'"     
        result.lstResult=FilterSQL.GetcommanWithoutParam(sp)       
    except  Exception as E:
        print(E)
        result.HasError=True
        result.Message.append(E)
    return result

def GetStyle(input:FilterInput):
    result=FilterResult()
    try:
        sp=f"Wr_mststyle_GetForHelp @PageSize={input.PageSize},@pageNo={input.PageNo},@search='{input.search}',@strBrandID='{input.strBrandID}'," 
        sp+= f"@strProductID='{input.strProductID}',@strItemGroupID='{input.strItemGroupID}',@strDepartmentID='{input.strDepartmentID}'"        
        result.lstResult=FilterSQL.GetcommanWithoutParam(sp)       
    except  Exception as E:
        print(E)
        result.HasError=True
        result.Message.append(E)
    return result

def GetAccount(Frombsgr:int,ToBsgr:int,PageNo:int,PageSize:int,search:str,strStatename:str,strCityName:str,strRegionID:str):
    result=FilterResult()
    try:        
        result.lstResult=FilterSQL.GetAccount(Frombsgr,ToBsgr,PageNo,PageSize,search,strStatename,strCityName,strRegionID)       
    except  Exception as E:
        print(E)
        result.HasError=True
        result.Message.append(E)
    return result

def GetDayBook():
    result=FilterResult()
    try:        
        result.lstResult=FilterSQL.GetDayBook()       
    except  Exception as E:
        print(E)
        result.HasError=True
        result.Message.append(E)
    return result





    
    