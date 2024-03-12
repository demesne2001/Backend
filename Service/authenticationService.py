import time
import jwt
from Entity.DTO.WsResponse import LoginResult
from decouple import config
users=[]

def checkuser(data):   
    # if db side maintain thay to db call
    #Else array throw maintain like below comment
    result=LoginResult()
    coun=0
    for user in users:
        coun+=1
        print(coun)
        print(user)
        print(data)
        if user.email==data.email and user.password==data.password:
            result.token=signJWT(user.email)
        # elif len(users)==coun:
        #     return False
        else:
            result.Error="Data is not Found"
        return result
        
def signJWT(userID:str):
    payload={
        "userID":userID,
        "expiry":time.time()+6000
    }
    token=jwt.encode(payload,'7C57243E7465CB171EEC8A5FB2345',algorithm='HS256')
    #  if db token update 
    #else direct return
    return token