import cv2 as cv

resim = cv.imread("wallpaper.jpg")

print(resim.item(200, 200, 0))  # Blue
print(resim.item(200, 200, 1))  # Green
print(resim.item(200, 200, 2))  # Red

# Yaptığımız şey resmin 200x200 pixelindeki bgr renklerinin değerlerini görmek
# Yani resmin 200x200 pixelindeki Blue value: 121 - Green value: 203 - Red value = 180

# print(resim.size) # -> resim.shape[0] * resim.shape[1] * resim.shape[2]
# print(resim.dtype)
# print("Resimin boyutu: ",resim.shape[0],"x",resim.shape[1],"\nRenk kanalı: ",resim.shape[2],sep="")

cv.imshow("Image",resim)

cv.waitKey(0)
cv.destroyAllWindows()





