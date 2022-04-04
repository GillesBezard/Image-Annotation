# -*-coding:Latin-1 -*
##########################################################################
"""Annotates images with given labels (To be used in command line)"""
# 
# (C) OPP (GB)
##########################################################################
# v 1.01 - 22/04/01 : First version
# v 1.02 - 22/04/03 : Added PNG image output for better quality

# Syntax: python showBoundingBoxes -ii=inputImage.png -io=outputImage.png -csv=csvFile.csv --show=yes --write=yes
# Minimum
# If output image is not given, but write option is set to 'yes', the name of output image is the name of input image + '_with_bb' before extension
# If no input image is given, all image files from csv file will be annoted: python showBoundingBoxes -csv=Example.csv -w=yes will browse all image files and generate the corresponding annoted one in the same folde.

# CSV file columns
# filename,                  width, height, class, xmin, ymin, xmax, ymax
# images/GH01542_0_760.jpeg, 1352,  760,    Shark, 1129, 7,    1153, 28
# tests on Mac: (venvPil) Mini-2019:imageLabels olaf$ python showBoundingBoxes.py -ii=test.jpeg -csv=test.csv

'''
Example of use
(venvPil) Mini-2019:imageLabels olaf$ pwd
/Users/olaf/_Documents/LoisirsNumeriques/Python/imageLabels
(venvPil) Mini-2019:imageLabels olaf$ cd dataset/images 
(venvPil) Mini-2019:images olaf$ python ../../showBoundingBoxes.py -ii=GH014198-60e7155540695_1399_0_760.jpeg -csv=../annotations_Shark.csv png=Yes -s=Yes 
'''

import sys
from argparse import ArgumentParser
import re
import pandas as pd
import numpy as np
import PIL
from PIL import Image, ImageFilter
# ours
import drawBoundingBoxesLib as dbb

myParser = ArgumentParser()

myParser.add_argument("-ii", dest="inputImage", default="",
        help="Input image filename")
myParser.add_argument("-io", dest="outputImage", default="", 
        help="Output image filename")
myParser.add_argument("-csv", dest="csvFile", required=True, 
        help="CSV file containing the annotations (shape: filename, width, height, class, xmin, ymin, xmax, ymax)")
myParser.add_argument("-s", "--show", dest="showImage", default="False", 
        help="Show image?: Yes/No or True/False")
myParser.add_argument("-w", "--write", dest="writeImage", default ="False", 
        help="Write image (save as a new file): Yes/No or True/False")
myParser.add_argument("-p", "--png", dest="saveAsPng", default="True", 
        help="If image is saved, PNG format will be used (better quality): Yes/No or True/False")

def twoStatesToBoolean (argument):
   argument_U = str(argument).upper()
   booleanArgument = ((argument_U == "TRUE") or (argument_U == "YES"))
   return booleanArgument
   
args = myParser.parse_args()
# Argument value setting
inputImage = args.inputImage
outputImage = args.outputImage
csvFile = args.csvFile
showImage = twoStatesToBoolean(args.showImage)
writeImage = twoStatesToBoolean(args.writeImage)
saveAsPng = twoStatesToBoolean(args.saveAsPng)

# Right now the files referenced in th CSV path have an absolutePath
# /media/laura/4T/databases/ulm_base1_poe_dedicated_Shark_without_GH034218_tiled_enriched/GH014198-60e7155540695_1542_0_760.jpeg
# We have to change that, but for now let us keep only the fine name
absolutePaths = True
# When looking for image in the first column, we take only the last characters: FileName.Extension

# First settings
if inputImage !="":
   inputImageShort, inputImageExtension = dbb.getNameAndExtension(inputImage)
   print('-  IN: ' + inputImageShort + '.' + inputImageExtension)

if inputImage != "" and writeImage:
   if saveAsPng: outputImage = inputImageShort + '_with_bb.' + 'png'
   else: outputImage = inputImageShort + '_with_bb.' + inputImageExtension
   print('- OUT: ' + outputImage)

# And let us read the CSV file that is REQUIRED
dataReadByPandas = pd.read_csv(csvFile)
csvData = np.copy(dataReadByPandas.values)

# Do we have to browse the whole CSV file?
if inputImage == "":
   print('To be done')

# Or do we just have to annotate one image?
else:
   # We must look for the file name ins the first column of the CVS file
   # First let us find the line that contains labels for our image, if any
   csvNeededLine = -1
   for i, lig in enumerate(csvData):
      if absolutePaths:
         ligShort, _ = dbb.getNameAndExtension(lig[0])
         #print("..." + inputImageShort + '...' + ligShort + '...' + lig[0] + '...')
         if ligShort == inputImageShort:
            #print ('FOUND')
            csvNeededLine = i
            # I know, while would be better, well, later
   if csvNeededLine == -1:
      print('Image file references "' + inputImageShort + '" not found in CSV file')
   else:
      # REMINDER: When looking for image in the first column, we take only the last characters: FileName.Extension
      imageName, className, x1, x2, y1, y2 = dbb.getImageAndBBCordinatesFromCSVLine(csvData[csvNeededLine])
      img=Image.open(inputImage) #(imageName)
      imageAnnotated = dbb.annotateImage(img, x1, y1, x2, y2, (255,0,0))
      if showImage:
         imageAnnotated.show()
      if writeImage:
         if saveAsPng: imageAnnotated.save(outputImage, format='PNG')
         else: imageAnnotated.save(outputImage, format='JPEG', quality=100)


# END