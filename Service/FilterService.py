from Entity.DTO.WsInput import FilterInput
from Entity.DTO.WsResponse import FilterResult
from DAL import FilterSQL  

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

def GetDayBook():
    result=FilterResult()
    try:        
        result.lstResult=FilterSQL.GetDayBook()       
    except  Exception as E:
        print(E)
        result.HasError=True
        result.Message.append(E)
    return result





    
    