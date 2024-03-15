from Entity.DTO.WsInput import FilterInput
from Entity.DTO.WsResponse import SubCategoryResult
from DAL import CommanSQL

def GetSubCategory(input:FilterInput):
    result=SubCategoryResult()
    try:
        result.lstResult=CommanSQL.GetSubCategory(input)
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result


def GetParmCaption():
    result=SubCategoryResult()
    try:
        result.lstresult=CommanSQL.GetParmCaption()
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result