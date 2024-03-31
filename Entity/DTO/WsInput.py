from pydantic import BaseModel,Field

class LoginInput(BaseModel):
    email:str= Field(default=None)
    password:str= Field(default=None)
    
# class FilterCommoninput(BaseModel):
#     strCompanyID:str| None= Field(default="")
#     strBranchID:str| None= Field(default="")
#     strDepartmentID:str| None= Field(default="")
#     strBrandID:str| None= Field(default="")
#     strProductID:str| None= Field(default="")
#     strItemGroupID:str| None= Field(default="")
#     strItemID:str| None= Field(default="")     
#     strDesignID:str| None= Field(default="")
#     strCity:str | None= Field(default="")
#     strState:str | None= Field(default="")
#     strRegionID:str | None= Field(default="")
#     strSalesAccountID:str | None= Field(default="")
#     strPurchaseAccountID:str | None= Field(default="")
#     strStyleID:str | None= Field(default="")
    
class FilterInput(BaseModel):
    search:str| None= Field(default="")
    strCompanyID:str| None= Field(default="")
    strBranchID:str| None= Field(default="")
    strDepartmentID:str| None= Field(default="")
    strBrandID:str| None= Field(default="")
    strProductID:str| None= Field(default="")
    strItemGroupID:str| None= Field(default="")
    PageSize:int| None= Field(default=9999)
    PageNo:int | None= Field(default=1)
    strItemID:str| None= Field(default="")
    strDesignID:str | None= Field(default="")
    SubCategoryNo:int | None= Field(default="")
    strCity:str | None= Field(default="")
    strState:str | None= Field(default="")
    strRegionID:str | None= Field(default="")
    strStyleID:str | None= Field(default="")

class GetAccountInput(BaseModel):
    PageNo:int
    PageSize:int
    search:str=""
    
    
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
    strDayBookID:str | None= Field(default="")
    ExtraVar:str | None= Field(default="")
    strLotNo:str | None= Field(default="")
    strCity:str | None= Field(default="")
    strState:str | None= Field(default="")
    strRegionID:str | None= Field(default="")
    strSalesAccountID:str | None= Field(default="")
    strPurchaseAccountID:str | None= Field(default="")
    strStyleID:str | None= Field(default="")
    
