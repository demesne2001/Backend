from fastapi import APIRouter,Body,Depends
from Entity.DTO.WsInput import CardandChartInput
from Service import ChartService
Chart=APIRouter()


@Chart.post('/GetHourlySales')
def GetHourlySales(input:CardandChartInput):
     return ChartService.GetHourlySales(input)


@Chart.post('/GetSalesRevenue')
def GetSalesRevenue(input:CardandChartInput):
     return ChartService.GetSalesRevenue(input)


@Chart.post('/GetTopsellingproduct')
def GetTopsellingproduct(input:CardandChartInput):
     return ChartService.GetTopsellingproduct(input)


@Chart.post('/GetTopsupplierbysales')
def GetTopsupplierbysales(input:CardandChartInput):
     return ChartService.GetTopsupplierbysales(input)


@Chart.post('/GetTopSalesmanBySales')
def GetTopSalesmanBySales(input:CardandChartInput):
     return ChartService.GetTopSalesmanBySales(input)


@Chart.post('/GetCoustomerConversion')
def GetCoustomerConversion(input:CardandChartInput):
     return ChartService.GetCoustomerConversion(input)


@Chart.post('/GetSalesAging')
def GetSalesAging(input:CardandChartInput):
     return ChartService.GetSalesAging(input)