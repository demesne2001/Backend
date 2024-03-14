from Entity.DTO.WsInput import CardandChartInput
from Entity.DTO.WsResponse import CardResult
from DAL import CardSQL


def GetStockCard(input:CardandChartInput):
    result=CardResult()
    try:
        result.lstResult=CardSQL.GetStockCard(input)
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result

def GetProfiteCard(input:CardandChartInput):
    result=CardResult()
    try:
        result.lstResult=CardSQL.GetProfiteCard(input)
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result

def GetSalesCard(input:CardandChartInput):
    result=CardResult()
    try:
        result.lstResult=CardSQL.GetSalesCard(input)
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result