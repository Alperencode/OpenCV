import cv2 as cv
import numpy as np

face_cascade = cv.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')
# cv.CascadeClassifier() ile kullandığım haarcascade'in dosya yolunu bir değişkene atadım


cap = cv.VideoCapture(0)  # cv.VideoCapture()'a 0 değerini atayarak
# program kapanana kadar bir canlı bir video kaydı almasını sağlıyorum

while True: # Programın asıl çalıştığı kısımı While True döngüsüne alıyorum
    ret, frame = cap.read()
    # cap.read() 2 değer döndürüyor
    # ret(bool) = program frame'leri okuyabiliyor mu -> sağlıklı okuyabiliyorsa True - okuyamıyorsa False
    # frame(ndarray) = kameradaki bütün pixel'leri frame frame okuyan ve sürekli değişen veri

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Opencv gelen verileri okuyabilmesi için frame'lerin gray'e dönüştürülmesi gerekiyor
    # cv.cvtColor() yani convertColor fonksiyonu ile ilk değere değişen frame değerini
    # İkinci value olarak ise opencv'nin gray rengini vermek için kullandığımız
    # cv.COLOR_BGR2GRAY değerini veriyoruz. Yaklaşık olarak siyah beyaz'a benzer bir görüntü elde ediyoruz

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    # Öncelikle faces bir liste değeri barındırıcak
    # Bu değer haarcascade'i (face_cascade değerini) kullanarak tespit ettiğimiz yüzleri barındırıcak
    # Her bir yüz için 4 değer tutucak
    # Bu değerler; Tespit ettiği yüzün Sol üst, sağ üst, sol alt ve sağ alt pixellerinin değerlerini barındırıcak
    # Bu verileri ileride live bir dikdörtgen çizmek için kullanacağım
    # === 1. VALUE ===
    # Verdiğim ilk değer Opencv'nin algılaması için gray yaptığım ve live olarak değişen "frame"
    # === 2. VALUE ===
    # "scaleFactor" en fazla 20'ye kadar değer alan modelin eşleşme yüzdesi diyebileceğimiz değer.
    # Yani bir hassasiyet. Şu an kullandığım Haarcascade modeli iyi bir machine learning'den geçtiği için
    # yaklaşık %5 anlamına gelen 1.3'i kullandım. Fakat smile veya eye haarcascade'leri için
    # modellerin ekranın smile veya eye bulunmayan bölgelerde tespit edilmemesi için bu değeri arttırabiliriz
    # === 3. VALUE ===
    # "minNeighbors" Bu parametre tespit edilen yüzlerin kalitesini etkileyecektir. Daha yüksek değer, daha az
    # tespitle sonuçlanır ancak daha yüksek kalitededir.


    for (x,y,w,h) in faces: # faces listesinden çıkan her yüz için için oluşturulan 4 değeri x,y,w,h değerlerine atadım
        print(x, y, w, h)  # x ve y = Sol üst - x+w ve y+h = Sağ alt değerleri
        # x = x_start, y = y_start fakat w ve h saf olarak (x ve y ile toplanmadan) ne ifade ediyor daha bulamadım

        roi_gray = gray[y:y+h, x:x+w]
        # Roi = Alan. Yani bu değere atayacağım değer detect edilen yüz modeli olucak
        # şimdi gray'den yani live camera'nın gray halinden faces listesinin bana verdiği verileri kullanarak
        # bir alan alıcam. Bu alanı = [y_start:y_end, x_start:x_end] olarak belirtiyorum (y+h = y_end, x+w = x_end)
        # Yani alanım tespit edilen modeli alıcak.
        # === Basit Anlatım İle: ===
        # Normalde bir alanı almak için [y,x] değerleri veririm
        # Model alanını alırken haarcascade'in benim için detect ettiği yüz verilerini kullanarak
        # [y'nin burasından:burasına kadar, x'in burasından:burasına kadar] gibi bir mantık ile alanı belirliyorum
        roi_color = frame[y:y+h, x:x+w]  # Aynı alanı renkli olarak alıyorum
        img_item = "my_image.png"  # Program kapatılmadan önce bulunan son face'i bir dosya olarak kayıt edicem
                                    # Bu da o dosyanın ismi
        cv.imwrite(img_item, roi_gray)  # dosyayı imwrite() ile önce isimi sonra'da alanı yani ndarray'i ile kaydediyorum
        color = (0, 0, 255)  # Live Rectangle için BGR değerimi color adlı değişkene atıyorum
        border = 2  # Rectangle border'ı
        width = x + w  # x_end
        height = y + h  # y_end
        if faces.all() == True: # Eğer liste'de en az 1 model tanımlanmış yani detect edilmiş ise:
            # Ekranda bir rectangle yani dikdörtgen çizmesini sağlayacağım
            cv.rectangle(frame, (x, y), (width, height),color, border)
            # rectangle fonksiyonu için:
            # === 1. VALUE ===
            # fonksiyona içinde rectangle çizmesi için bir ndarray vermem gerek bu ndarray'e
            # sürekli olarak değişen ve live cam'den gelen frame değerini atıyorum
            # === 2. VALUE ===
            # Tuple olarak göndermem gereken bir değer
            # Tuple'ın 1. elemanı x_start, 2. elamanı y_start olmalı. Detect'ten gelen verileri gönderiyorum
            # === 3. VALUE ===
            # Aynı şekilde tuple gönderiyorum. 1. elemanı x_end, 2. elamanı y_end
            # === 4. VALUE ===
            # Rectangle'ın BGR değeri. Önceden belirlediğim BGR değeri taşıyan değişkeni gönderiyorum
            # === 5. VALUE ===
            # Rectangle'ın border değeri. Aynı şekilde belirlediğim border değişkenini gönderiyorum
            # === Short Way ===
            # cv.rectangle(CAPTURE, (X_Start, Y_Start), (X_End, Y_End), Rectangle BGR, Rectangle Border)
            # Yani live olarak ekranda algılanan her yüz modelinin etrafında bir rectangle çizmesini sağlıyorum

    cv.imshow('frame', frame)  # imshow ile live cam'i frame değişkenini kullanarak ekranda gösteriyorum
    # cv.imshow('gray', gray)  # Gri görüntüyü göstermek için (Opencv'nin nasıl gördüğünü görmek için)
    if cv.waitKey(20) and 0xFF == ord('q'):
        break

cap.release() # Görüntüyü Release ediyorum yani gösterilmesini sağlıyorum
cv.destroyAllWindows()  # This is not working and i don't know why
