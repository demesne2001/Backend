import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
from Controller import authenticationController,Filtercontroller

app=FastAPI()

app.include_router(authenticationController.authentication,prefix='')
app.include_router(Filtercontroller.Filter,prefix='/Filter')
origins=['*']
app.add_middleware(CORSMiddleware,allow_origins=origins,allow_credentials=True,allow_methods=['*'],allow_headers=['*'],)

@app.post("/Demo")
def Demo():
    return{"msg":"Welcome to Fast"}

# if __name__ == "__main__":
#      uvicorn.run(app, host="127.0.0.1",port=3000)