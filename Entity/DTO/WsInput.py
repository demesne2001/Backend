from pydantic import BaseModel,Field

class LoginInput(BaseModel):
    email:str= Field(default=None)
    password:str= Field(default=None)

class FilterInput(BaseModel):
    search:str
    strCompanyID:str
    strBranchID:str
    strDepartmentID:str
    strBrandID:str
    strProductID:str
    strItemGroupID:str
    PageSize:int
    PageNo:int
    strItemID:str
    strDesignID:str