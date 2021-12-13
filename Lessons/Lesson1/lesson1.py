import cv2 as cv


image = cv.imread("prey.jpg",0)

print(image)

cv.imshow("Prey Wallpaper",image)
cv.imwrite("prey_gri.jpg",image)

cv.waitKey(0)
cv.destroyAllWindows()

###