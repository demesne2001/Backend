from fastapi import APIRouter,Body,Depends
from Entity.DTO.WsInput import FilterInput
from Service import FilterService

Filter=APIRouter()

@Filter.post('/GetCompany')
def Getcompany(input:FilterInput):
    return FilterService.Getcompany(input)

@Filter.post('/GetBranch')
def GetBranch(input:FilterInput):
    return FilterService.GetBranch(input)

@Filter.post('/GetDepartment')
def GetDepartment(input:FilterInput):
    return FilterService.GetDepartment(input)

@Filter.post('/GetItemGroup')
def GetItemGroup(input:FilterInput):
    return FilterService.GetItemGroup(input)

@Filter.post('/GetBrand')
def GetBrand(input:FilterInput):
    return FilterService.GetBrand(input)

@Filter.post('/GetSalesman')
def GetSalesman(input:FilterInput):
    return FilterService.GetSalesman(input)

@Filter.post('/GetProduct')
def GetProduct(input:FilterInput):
    return FilterService.GetProduct(input)

@Filter.post('/GetSeason')
def GetSeason(input:FilterInput):
    return FilterService.GetSeason(input)

@Filter.post('/GetFit')
def GetFit(input:FilterInput):
    return FilterService.GetFit(input)


@Filter.post('/GetColor')
def GetColor(input:FilterInput):
    return FilterService.GetColor(input)

@Filter.post('/GetItemName')
def GetItemName(input:FilterInput):
    return FilterService.GetItemName(input)

@Filter.post('/GetLotNo')
def GetLotNo(input:FilterInput):
    return FilterService.GetLotNo(input)

@Filter.post('/GetDesign')
def GetDesign(input:FilterInput):
    return FilterService.GetDesignservice(input)

@Filter.post('/GetDayBook')
def GetDayBook(input:FilterInput):
    return FilterService.GetDayBook()


@Filter.post('/GetCity')
def GetCity():
    return FilterService.GetCity()


@Filter.post('/GetState')
def GetState():
    return FilterService.GetState()

@Filter.post('/GetRegion')
def GetRegion():
    return FilterService.GetRegion()

@Filter.post('/GetSalesParty')
def Getsalesparty(PageNo:int,PageSize:int,search:str=""):
    return FilterService.GetAccount(2451,2489,PageNo,PageSize,search)

@Filter.post('/GetPurchaseParty')
def GetPurchaseParty(PageNo:int,PageSize:int,search:str=""):
    return FilterService.GetAccount(1511,1549,PageNo,PageSize,search)

