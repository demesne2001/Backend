from fastapi import APIRouter,Body,Depends
from Entity.DTO.WsInput import FilterInput,UploadFile
from Service import CommanService
import base64

Common=APIRouter()

BaseDirectory="Utility/Image/"

@Common.post('/GetSubCategory')
def GetSubCategory(input:FilterInput):
    return CommanService.GetSubCategory(input)

@Common.post('/ParmCaption')
def GetParmCaption():
     return CommanService.GetParmCaption()

 
@Common.post('/uploadImage')
async def Create_upload(input:UploadFile):   
    data_split = input.Base64.split('base64,')
    encoded_data = data_split[1] 
    data = base64.b64decode(encoded_data)
    with open(F"{BaseDirectory}{input.LoginID}.{input.Extension}","wb") as f:
        f.write(data)
    return {'filename':F"{input.LoginID}.{input.Extension}"}