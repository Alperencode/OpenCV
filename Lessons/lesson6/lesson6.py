import cv2 as cv


def main():
    android = cv.imread("android.jpg")
    wallpaper = cv.imread("wallpaper.jpg")
    a_gray = cv.cvtColor(android,cv.COLOR_BGR2GRAY) # Resimi Griye döndürmek için
    # print(android[100,50]) # Gri değeri 160 - siyah değeri 0
    height,width,channel = android.shape

    ROI = wallpaper[0:height,0:width]

    # cv.threshold = Belli bir değer üstündeki bütün renk değerini 1 renk değerine atamak için
    # kullandık. Örneğin aşağıda a_gray resimindeki 10'un üzerindeki bütün renkleri 255 yaptık
    # Resim 2 renk değerinden oluştuğu için (0 ve 160) 160 değerlerinin hepsi 255'e eşitlendi

    ret,mask = cv.threshold(a_gray,10,255,cv.THRESH_BINARY) # ret = 10 --- maks = ndarray

    # cv.bitwise_not(ndarray)
    # Bütün bit değerlerini tersine çevirip renklerin zıt değerlerini oluşturan method
    # Siyah olan bir resimde bütün bit değerleri 0 iken hepsini 1
    # Beyaz olan bir resimde bütün bit değerleri 1 iken hepsini 0 yaparak zıt değerleri elde ediyor
    mask_reverse = cv.bitwise_not(mask)

    # === BITWISE Logic === #

    # The Logic And
    # 0 and 0 = 0
    # 1 and 0 = 0
    # 0 and 1 = 0
    # 1 and 1 = 1

    # The Logic Or
    # 0 or 0 = 0
    # 1 or 0 = 1
    # 0 or 1 = 1
    # 1 or 1 = 1

    # The Logic XOR
    # 0 xor 0 = 0
    # 1 xor 0 = 1
    # 0 xor 1 = 1
    # 1 xor 1 = 0

    # The Logic Not
    # 1 not = 0
    # 0 not = 1
    # Opposite

    # === BITWISE Logic === #

    wallpaper_back = cv.bitwise_and(ROI, ROI, mask = mask_reverse)
    total = cv.add(android,wallpaper_back)
    wallpaper[0:height,0:width] = total

    cv.imshow("Android Wallpaper", wallpaper)
    # cv.imshow("x",wallpaper_back)
    # cv.imshow("ROI",ROI)
    # cv.imshow("Reversed",mask_reverse)
    # cv.imshow("Picture 2",mask)
    # cv.imshow("Picture 1",wallpaper)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()