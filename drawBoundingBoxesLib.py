# -*-coding:Latin-1 -*
##########################################################################
"""Library that displays bounding boxes around objets"""
# 
# (C) OPP (GB)
##########################################################################
# v 1.01 - April 2022 : First version
# v 1.02 - 

# IMPORTS
import numpy as np
import PIL
from PIL import Image, ImageFilter
import re

# CONSTANTS
ALL_DATA_SET = -1

def getNameAndExtension (aGivenFileName):
    # Extensions: 3 to 4 letters or numbers
    # parameter can be  'GH014198-60e7155540695_1399_0_760.jpeg',  './dataset/images/GH014_760.jpeg', '/media/laura/4T/databases/ulm_Shark/GH0_1542_0_760.png'
    pat = '([^/]+)\.(\w{3,4})$'
    pat = re.compile(pat)
    name = pat.search(aGivenFileName).group(1)
    extension = pat.search(aGivenFileName).group(2)
    return name, extension

def getImageAndBBCordinatesFromCSVLine(aLine):
    pat = '([^/]+\.jpeg)$'
    pat = re.compile(pat)
    fileName = pat.search(aLine[0]).group(1)
    xMin = aLine[4]
    xMax = aLine[6]
    yMin = aLine[5]
    yMax = aLine[7]
    label = aLine[3]
    return fileName, label, xMin, xMax, yMin, yMax

def annotateImage(imageIn, c1, l1, c2, l2, couleur):
    imageOut = imageIn
    for lig in range (l1, l2):
        imageOut.putpixel((c1, lig), couleur)
        imageOut.putpixel((c2, lig), couleur)
    for col in range (c1, c2):
        imageOut.putpixel((col, l1), couleur)
        imageOut.putpixel((col, l2), couleur)
    return imageOut

def main():
    print("TESTING LIB")

    img = annotateImage(Image.open('./dataset/images/GH014198-60e7155540695_1399_0_760.jpeg'), 20, 80, 100, 100, (255,0,0))
    img.show()
    
    print ("LIB TEST IS OVER.")
  
if __name__== "__main__":
    main()

# END