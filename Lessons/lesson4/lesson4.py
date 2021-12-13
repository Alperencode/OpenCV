import cv2 as cv

image = cv.imread("wallpaper.jpg")

# Resim uzatma
x = cv.copyMakeBorder(image,100,100,100,100,cv.BORDER_REPLICATE)

# Resim Aynalama
y = cv.copyMakeBorder(image,100,100,100,100,cv.BORDER_REFLECT)

# Resim Tekrarlama
z = cv.copyMakeBorder(image,100,100,100,100,cv.BORDER_WRAP)

# Resim Çerçeveleme/Sarma
q = cv.copyMakeBorder(image,100,100,100,100,cv.BORDER_CONSTANT)

# Resim Kare Alma
rectangle = cv.rectangle(image,(50,100),(200,400),[0,0,255],2)
# cv.recrangle(ndarray,tuple(sol alt köşe),tuple(sağ üst köşe),[bgr],int(border kalınlığı)) # TUPLE BİLGİSİ YANLIŞ!!
# bu satırı yazdıktan sonra normal fotoğraf değişkeni rectangle almış şekilde bastırılıyor!


cv.imshow("Picture",image)
cv.imshow("Rectangle",rectangle)
# cv.imshow("Uzatma",x)
# cv.imshow("Aynalama",y)
# cv.imshow("Tekrarlama",z)
# cv.imshow("Sarma",q)

cv.waitKey(0)
cv.destroyAllWindows()