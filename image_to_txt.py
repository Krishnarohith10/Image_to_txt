#You should take all the images with same type and also size. Make sure that you check this.
#and also following packages installed

import numpy as np
import cv2 as cv
import glob

images = glob.glob("*jpg")
file = open('dataset.txt','a') #name it as you like with extension .txt

for image in images:
    img = cv.imread(image, cv.IMREAD_GRAYSCALE)
    img_values = img.flatten()
    img_values = img_values.reshape(-1, 1).T
    print(img_values) #this gives the pixels values of the image (height * width)
    np.savetxt(file, img_values, delimiter = ',', newline = '\n')

file.close()
