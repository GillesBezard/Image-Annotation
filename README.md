# Labels to bounding boxes toolbox

April 2022 - Version 1.0

.

_This toolbox provides different tools to annotate images._

## 1 - Global description

This toolbox main component is the library named `drawBoundingBoxLib.py`

All components are (see below for details)
- `drawBoundingBoxLib.py` -  The library itself
- `exampleLabelledImage.ipynb` - A Jupyter notebook to interactively see what can be done with the lib from Python
- `showBoundingBoxes.py` - A python-command-line program designed to be used with arguments

## 2 - How to use __showBoundingBoxes.py__

___showBoundingBoxes___ has to be used in command-line mode. Entering `python showBoundingBoxes/py` AND providing arguments. In version 2.0 (to come) the only necessary argument will be the CSV file. Right now, you can only annotate one image at a time, thus, the input image name is also needed.

Syntax
```
python showBoundingBoxes.py --help
usage: showBoundingBoxes.py [-h] [-ii INPUTIMAGE] [-io OUTPUTIMAGE] -csv
                            CSVFILE [-s SHOWIMAGE] [-w WRITEIMAGE]
                            [-p SAVEASPNG]

optional arguments:
  -h, --help            show this help message and exit
  -ii INPUTIMAGE        Input image filename
  -io OUTPUTIMAGE       Output image filename
  -csv CSVFILE          CSV file containing the annotations (shape: filename,
                        width, height, class, xmin, ymin, xmax, ymax)
  -s SHOWIMAGE, --show SHOWIMAGE
                        Show image?: Yes/No or True/False
  -w WRITEIMAGE, --write WRITEIMAGE
                        Write image (save as a new file): Yes/No or True/False
  -p SAVEASPNG, --png SAVEASPNG
                        If image is saved, PNG format will be used (better
                        quality): Yes/No or True/False
```

```
pwd
/Users/olaf/_Documents/LoisirsNumeriques/Python/imageLabels

cd dataset/images 

python ../../showBoundingBoxes.py -ii=GH014198-60e7155540695_1399_0_760.jpeg -csv=../annotations_Shark.csv png=Yes -w=Yes 
```

Please note that file name will be extracted from given parameter 'ii', and output image will be created in current folder. Thus if your hierarchy is

![hierarchy](folderHierarchy.png)

You can create an 'annotedImages' folder, move into it and enter

```
python ../../showBoundingBoxes.py -ii=../images/GH014198-60e7155540695_1399_0_760.jpeg -csv=../annotations_Shark.csv -w=Yes
``` 

Check the result 

```
pwd
/Users/olaf/_Documents/LoisirsNumeriques/Python/imageLabels/dataset/annotatedImages

ls -l
total 1288
-rw-r--r--  1 olaf  staff  658610  3 avr 22:50 GH014198-60e7155540695_1399_0_760_with_bb.png 
```

## 3 - All 3 components detailled description

### 3.1 - ___drawBoundingBoxLib___ library

TBD

### 3.2 - The Jupyter notebook

TBD

### 3.3 - The command-line python program ___showBoundingBoxes___

TBD

