import cv2 as cv


image = cv.imread("wallpaper.jpg")
b, g, r = cv.split(image)
image[:, :, 2] = 255

# newimage = cv.merge((b,g,r)) # birleştirmek için
# print(type(b))
# print(cv.split(image))
# place = image[200:400, 200:400]
# image[0:200,0:200] = place     # Eğer burda image'den seçtiğim bölge place'deki pixel'ler ile uyuşmazsa hata oluşur
#                                place'de aldığım bölge y ve x'den 200pixel dolayısıyla değiştirmek istediğim bölge de
#                                200x200 bir bölge olmalı


#for i in range(500):
#   image[i,i] = [0,0,0]

# print("Image: ",image.shape)
# print("Image size: ",image.size)
# print("Image's bit: ",image.dtype)

cv.imshow("Wallpaper Original", image)
cv.imshow("Wallpaper Blue", b)
cv.imshow("Wallpaper Green", g)
cv.imshow("Wallpaper Red", r)

# cv.imshow("Place", place)

cv.waitKey(0)
cv.destroyAllWindows()