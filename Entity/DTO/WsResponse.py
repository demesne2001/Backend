from pydantic import BaseModel,Field

class CommonInput:
    def __init__(self):
        self.Message = []
        self.HasError = False

class LoginResult:
    acsesstoken:str
    Error:str

class FilterResult(CommonInput):
    def __init__(self):
        super().__init__()
        self.lstResult:[]

class CardResult(CommonInput):
    def __init__(self):
        super().__init__()
        self.lstResult:[]
        
class ChartResult(CommonInput):
    def __init__(self):
        super().__init__()
        self.lstResult:[]
        
class SubCategoryResult(CommonInput):
    def __init__(self):
        super().__init__()
        self.lstresult=[]
        self.FromDate=""
        self.ToDate=""

class ImageRsult(CommonInput):
    def __init__(self):
        super().__init__()
        self.ImageName:str