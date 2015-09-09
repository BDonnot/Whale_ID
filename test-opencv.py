import numpy as np
import cv2
import sys
import os

import sloth
sloth.items.BaseItem

if(sys.version == "2.7.6 (default, Jun 22 2015, 17:58:13) \n[GCC 4.8.2]") :
    os.chdir("/home/benjamin/Documents/CDiscount/")
else :
    os.chdir("D:/Users/Benjamin/Documents/Data Science/Whale_ID/")
# Get user supplied values
if(len(sys.argv) >= 2) :
    imagePath = sys.argv[1]
    if(len(sys.argv) >= 3) :
        cascPath = sys.argv[2]
    else :
        cascPath = "cascade"
else :
    imagePath = "data/imgs_subset"

img = cv2.imread('/'.join([imagePath,"w_0.jpg"]),0)
vis = img.copy()
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



    