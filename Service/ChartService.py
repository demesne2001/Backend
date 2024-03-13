from Entity.DTO.WsInput import CardandChartInput
from Entity.DTO.WsResponse import ChartResult
from DAL import ChartSQL

def GetSalesAging(input:CardandChartInput):
    result=ChartResult()
    try:
        result.lstResult=ChartSQL.GetSalesAging(input)
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result

def GetCoustomerConversion(input:CardandChartInput):
    result=ChartResult()
    try:
        result.lstResult=ChartSQL.GetCoustomerConversion(input)
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result

def GetTopSalesmanBySales(input:CardandChartInput):
    result=ChartResult()
    try:
        result.lstResult=ChartSQL.GetTopSalesmanBySales(input)
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result

def GetTopsellingproduct(input:CardandChartInput):
    result=ChartResult()
    try:
        result.lstResult=ChartSQL.GetTopsellingproduct(input)
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result

def GetSalesRevenue(input:CardandChartInput):
    result=ChartResult()
    try:
        result.lstResult=ChartSQL.GetSalesRevenue(input)
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result

def GetHourlySales(input:CardandChartInput):
    result=ChartResult()
    try:
        result.lstResult=ChartSQL.GetHourlySales(input)
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result

def GetTopsupplierbysales(input:CardandChartInput):
    result=ChartResult()
    try:
        result.lstResult=ChartSQL.GetTopsupplierbysales(input)
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result