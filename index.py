import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
from Controller import authenticationController,Filtercontroller,CardController,ChartController,CommonController
from fastapi.staticfiles import StaticFiles
import os

app=FastAPI()

path="Utility/Image"
PDFPath="Utility/PDF"
app.include_router(authenticationController.authentication,prefix='')
app.include_router(Filtercontroller.Filter,prefix='/Filter')
app.include_router(CardController.Card,prefix='/Card')
app.include_router(ChartController.Chart,prefix='/Chart')
app.include_router(CommonController.Common,prefix='/Comman')
origins=['*']
app.add_middleware(CORSMiddleware,allow_origins=origins,allow_credentials=True,allow_methods=['*'],allow_headers=['*'],)
if(os.path.exists(path)):
    pass
else:
    os.makedirs(path)
    
if(os.path.exists(PDFPath)):
    pass
else:
    os.makedirs(PDFPath)

app.mount("/image", StaticFiles(directory="Utility/Image"), name="image")
app.mount("/PDF", StaticFiles(directory="Utility/PDF"), name="PDF")
@app.post("/Demo")
def Demo():
    return{"msg":"Welcome to Fast"}

# if __name__ == "__main__":
#      uvicorn.run(app, host="127.0.0.1",port=3000)