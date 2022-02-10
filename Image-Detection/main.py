import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def main():
    # image's path
    img_rgb = cv.imread('mario.png') 
    
    # converting image to grayscale
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    
    # path to template image and turned it to grayscale too
    template = cv.imread('mario_coin.png',0)
    
    # defining weight and height to enclose the template (in rectangle)
    w, h = template.shape[::-1]
    
    # indicating the detection method with matchTemplate(image,template,the method)
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    
    # defining the threshold value
    threshold = 0.8  
    
    # finding the location of the template in the image
    loc = np.where( res >= threshold) 
    
    for pt in zip(*loc[::-1]): 
        # drawing a rectangle around the template
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)
    
    # saving the result image
    cv.imwrite('res.png',img_rgb) 

if __name__ == "__main__":
    main()