from fastapi import APIRouter,Body,Depends
from Entity.DTO.WsInput import FilterInput
from Service import CommanService

Common=APIRouter()

@Common.post('/GetSubCategory')
def GetSubCategory(input:FilterInput):
    return CommanService.GetSubCategory(input)

@Common.post('/ParmCaption')
def GetParmCaption():
     return CommanService.GetParmCaption()