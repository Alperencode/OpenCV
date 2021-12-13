import cv2 as cv
import numpy as np

def main():
    image = cv.imread("wallpaper.jpg")

    bigImage = cv.pyrUp(image)     # cv.pyrUp(ndarray)
    smallImage = cv.pyrDown(image) # cv.pyrDown(ndarray)

    cv.imshow("Picture", image)
    # cv.imshow("Big Picture", bigImage)
    # cv.imshow("Small Picture", smallImage)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()
