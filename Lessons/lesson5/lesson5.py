import cv2 as cv

def main():
    image1 = cv.imread("x.jpg")
    image2 = cv.imread("y.jpg")

    print("x: ",image1.shape)
    print("y: ",image2.shape)

    # !! Toplama yapabilmek için iki resiminde aynı boyutta olması gerek !! #

    toplam = cv.add(image1,image2)
    weighted = cv.addWeighted(image1,0.8,image2,0.2,0) # Alpha ve Beta değerleri 1'e eşit olmak zorunda


    # === Ağırlı Toplama Mantığı ===
    # image1'in bütün pixellerindeki BGR değerlerini verdiğimiz Alpha değeri ile
    # image2'nin bütün pixellerindeki BGR değerlerini verdiğimiz Beta değerleri ile
    # çarpıp yeni resimin BGR değerleri için iki sayının toplamından oluşan
    # bir ndarray oluşturuyor Bu da hangi resime verdiğimiz değerler daha yüksekse
    # o resimin daha öncelikli gösterilmesini sağlıyor

    # === Gösterimi ===
    # x = image1[200,200] * 0.8
    # y = image2[200,200] * 0.2
    # newimage[200,200] = x + y


    # cv.imshow("Picture 1", image1)
    # cv.imshow("Picture 2", image2)
    cv.imshow("Toplam",toplam)
    cv.imshow("Weighted",weighted)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()
