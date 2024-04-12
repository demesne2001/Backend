from Entity.DTO.WsInput import FilterInput,GetPDfUsingImageInput
from Entity.DTO.WsResponse import SubCategoryResult,FilterResult,ImageRsult
from DAL import CommanSQL
import os
import cv2 
from fpdf import FPDF
import numpy as np
from PIL import Image
import img2pdf

BaseDirectory="Utility/Image/"
PDFBaseDirectory="Utility/PDF/"
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
        result=CommanSQL.GetParmCaption()
    except  Exception as E:
        result.HasError=True
        result.Message.append(E)
    return result


def MultipleImageMerge(ImageLst: list, newImageName):    
    result=ImageRsult()    
    try:
        if len(ImageLst) > 0:
            max_height1 = 0
            max_width1 = 0
            max_height = 0
            max_width= 0
            counter=0
           
            # for ImageName in ImageLst:
            #     counter+=1
            #     if os.path.exists(BaseDirectory + ImageName):
            #         img = cv2.imread(BaseDirectory + ImageName, 1)
            #         height, width, _ = img.shape
            #         max_height = max(max_height, height)
            #         max_width = max(max_width, width)
            #     else:
            #         result.Message.append( f"File not Found {ImageName}")
            #         result.HasError = True                    
            #         return result

            
            # resized_images = []
            # for ImageName in ImageLst:
            #     img = cv2.imread(BaseDirectory + ImageName, 1)
            #     resized_img = cv2.resize(img, (max_width, max_height))
            #     resized_images.append(resized_img)

           
            # MergeImage = np.vstack(resized_images)
            # cv2.imwrite(BaseDirectory + newImageName + '.jpg', MergeImage)
            img_01 = Image.open(BaseDirectory+ImageLst[0]) 
            img_02 = Image.open(BaseDirectory+ImageLst[1]) 
            print(1)
            img_01_size = img_01.size 
            img_02_size = img_02.size 
            print(2)
            new_im = Image.new('RGB', (1*img_01_size[0],1*img_01_size[0]), (250,250,250)) 
            new_im.paste(img_01, (0,0)) 
            new_im.paste(img_02, (0,img_01_size[1])) 
            print(3)
            new_im.save(BaseDirectory + newImageName + '.png', "PNG") 
            print(4)
            result.ImageName=newImageName
    except Exception as e:        
        result.HasError = True
        result.Message.append(e)

    return result



def ImageToPDf(input:GetPDfUsingImageInput):
    result=FilterResult()
    if(len(result.Message)==0):
        try:            
            FunResult=MultipleImageMerge(input.ImageLst,input.FileName)
            
            if(FunResult.HasError==True):
                raise FunResult.Message
            elif(os.path.exists(BaseDirectory+FunResult.ImageName+'.png')):
                print('Condtion true')
                # pdf = FPDF()
                # pdf.add_page()
                # pdf.image(BaseDirectory+FunResult.ImageName+'.jpg')
                # print(pdf)
                # pdf.output(PDFBaseDirectory+input.FileName+'.PDF',"F")
                # Working One More Option below
                image = Image.open(BaseDirectory+FunResult.ImageName+'.png')
                pdf_bytes = img2pdf.convert(image.filename)                
                file = open(PDFBaseDirectory+input.FileName+'.pdf', "wb")                
                file.write(pdf_bytes)                
                image.close()                
                file.close()
                result.Message.append(input.FileName+'.pdf')                 
                if(os.path.exists(PDFBaseDirectory+input.FileName+'.pdf')):
                    for ImageNA in input.ImageLst:
                          if(os.path.exists(BaseDirectory+ImageNA)): 
                                os.remove(BaseDirectory+ImageNA)
                    if(os.path.exists(BaseDirectory+FunResult.ImageName+'.png')):
                        os.remove(BaseDirectory+FunResult.ImageName+'.png')
                    print(input.FileName+'.pdf')
                                       
            elif(not os.path.exists(FunResult.ImageName+'.png')):
                print('Not exists')
                print(BaseDirectory+FunResult.ImageName)
            else:
                print(FunResult)
        except Exception as e:
            print("Error",e)
            result.HasError=True
            result.Message.append(str(e))
    else:
        result.HasError=True
    return result