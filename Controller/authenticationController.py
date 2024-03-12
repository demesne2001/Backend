from fastapi import APIRouter,Body,Depends
from Entity.DTO.WsInput import LoginInput
from Service.authenticationService import checkuser

authentication=APIRouter()

@authentication.post('/Login')
def login(data:LoginInput=Body(default=None)):
    return checkuser