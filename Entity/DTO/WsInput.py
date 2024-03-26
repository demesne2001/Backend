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
    SubCategoryNo:int
    
    
class CardandChartInput(BaseModel):
    ChartValueOption:str | None= Field(default="")
    strCompanyID:str| None= Field(default="")
    strBranchID:str| None= Field(default="")
    FromDate:str| None= Field(default="")
    ToDate:str| None= Field(default="")
    strDepartmentID:str| None= Field(default="")
    strBrandID:str| None= Field(default="")
    strProductID:str| None= Field(default="")
    strItemGroupID:str| None= Field(default="")
    strItemID:str| None= Field(default="")
    strColorID:str| None= Field(default="")
    strSeasonID:str| None= Field(default="")
    strSalesmanID:str| None= Field(default="")
    strDesignID:str| None= Field(default="")
    strSubCategory1ID:str| None= Field(default="") 
    strSubCategory2ID:str| None= Field(default="")
    strSubCategory3ID:str| None= Field(default="")
    strSubCategory4ID:str | None= Field(default="")
    strSubCategory5ID:str | None= Field(default="")
    strSubCategory6ID:str | None= Field(default="")
    strSubCategory7ID:str | None= Field(default="")
    strSubCategory8ID:str | None= Field(default="")
    strSubCategory9ID:str | None= Field(default="")
    strSubCategory10ID:str | None= Field(default="")
    ExtraVar:str | None= Field(default="")
    strLotNo:str | None= Field(default="")