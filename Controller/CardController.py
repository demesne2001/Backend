from fastapi import APIRouter,Body,Depends
from Entity.DTO.WsInput import CardandChartInput
from Service import Cardservice
Card=APIRouter()

@Card.post('/GetSalesCard')
def GetSalesCard(input:CardandChartInput):
     return Cardservice.GetSalesCard(input)

@Card.post('/GetStockCard')
def GetStockCard(input:CardandChartInput):
     return Cardservice.GetStockCard(input)


@Card.post('/GetProfiteCard')
def GetProfiteCard(input:CardandChartInput):
     return Cardservice.GetProfiteCard(input)
