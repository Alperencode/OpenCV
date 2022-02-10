import cv2 as cv
import numpy as np

face_cascade = cv.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')
# cv.CascadeClassifier() ile kullandığım haarcascade'in dosya yolunu bir değişkene atadım


cap = cv.VideoCapture(0)  
# cv.VideoCapture()'a 0 değerini atayarak
# program kapanana kadar bir canlı bir video kaydı almasını sağlıyorum

while True: # Programın çalıştığı kısımı While True döngüsüne alıyorum
    ret, frame = cap.read()
    # cap.read() 2 değer döndürüyor
    # ret(bool) = program frame'leri okuyabiliyor mu -> sağlıklı okuyabiliyorsa True - okuyamıyorsa False
    # frame(ndarray) = kameradaki bütün pixel'leri frame frame okuyan ve sürekli değişen veri

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Opencv gelen verileri okuyabilmesi için frame'lerin gray'e dönüştürülmesi gerekiyor
    # cv.cvtColor() yani convertColor fonksiyonu ile ilk değere değişen frame değerini
    # İkinci değere ise opencv'nin gray rengini vermek için kullandığımız
    # cv.COLOR_BGR2GRAY değerini veriyoruz. Yaklaşık olarak siyah beyaz'a benzer bir görüntü elde ediyoruz

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    # Öncelikle faces bir liste değeri barındırıcak
    # Bu değer haarcascade'i (face_cascade değerini) kullanarak tespit ettiğimiz yüzleri barındırıcak
    # Her bir yüz için 4 değer tutucak
    # Bu değerler; Tespit ettiği yüzün Sol üst, sağ üst, sol alt ve sağ alt pixellerinin değerlerini barındırıcak
    # Bu verileri ileride canlı bir dikdörtgen çizmek için kullanacağım

    # === 1. Argüman ===
    # Verdiğim ilk değer Opencv'nin algılaması için gray yaptığım ve canlı olarak değişen "frame"
    
    # === 2. Argüman ===
    # "scaleFactor" en fazla 20'ye kadar değer alan modelin eşleşme yüzdesi diyebileceğimiz değer.
    # Yani bir hassasiyet. Şu an kullandığım Haarcascade modeli iyi bir machine learning'den geçtiği için
    # yaklaşık %5 anlamına gelen 1.3'i kullandım. Fakat smile veya eye haarcascade'leri için
    # modellerin ekranın smile veya eye bulunmayan bölgelerde tespit edilmemesi için bu değeri arttırabiliriz
    
    # === 3. Argüman ===
    # "minNeighbors" Bu parametre tespit edilen yüzlerin kalitesini etkileyecektir. Daha yüksek değer, daha az
    # tespitle sonuçlanır ancak daha yüksek kalitededir.


    # faces listesinde her yüz için oluşturulan 4 değeri x,y,w,h değişkenleri ile kullanıyorum
    for (x,y,w,h) in faces: 
        # x ve y = Sol üst - x+w ve y+h = Sağ alt değerleri
        print(x, y, w, h)

        # Roi = Alan. Yani bu değişkene atayacağım değer detect edilen yüz modeli olucak
        roi_gray = gray[y:y+h, x:x+w]

        # Çalışma Mantığı:
        # şimdi gray değerinden (live camera'nın gray hali) faces listesinin bana verdiği verileri kullanarak bir alan alıcam.
        # Bu alanı = [y_start:y_end, x_start:x_end] olarak belirtiyorum (y+h = y_end, x+w = x_end değerleri oluyor)
        # Yani bu alan yüz tespit edilen bölgeyi temsil ediyor.
        
        # Aynı alanı renkli olarak alıyorum
        roi_color = frame[y:y+h, x:x+w]
        
        # Program kapatılmadan önce bulunan son bulunan yüzü png olarak kaydedeceğim
        # O dosyaya isim veriyorum
        img_item = "my_image.png"
        
        # dosyayı imwrite() ile önce isimi sonra'da alanı yani ndarray'i ile kaydediyorum
        cv.imwrite(img_item, roi_color)
        
        # Yüzü çevreleyen dikdörtgen için BGR (renk) değerimi color adlı değişkene atıyorum
        color = (0, 0, 255)
        
        # Rectangle border'ı (çerçeve)
        border = 2

        width = x + w  # x_end
        height = y + h  # y_end

        # Eğer liste'de en az 1 model tanımlanmış yani detect edilmiş ise:
        if faces.all() == True:
        
            # Ekranda bir rectangle yani dikdörtgen çizmesini çiziyorum
            cv.rectangle(frame, (x, y), (width, height),color, border)

            # rectangle fonksiyonu için:
            # === 1. Argüman ===
            # fonksiyona içinde rectangle çizmesi için bir ndarray vermem gerek bu ndarray'e
            # sürekli olarak değişen ve live cam'den gelen frame değerini atıyorum
            
            # === 2. Argüman ===
            # Tuple olarak göndermem gereken bir değer
            # Tuple'ın 1. elemanı x_start, 2. elamanı y_start olmalı. faces listesinden gelen verileri gönderiyorum
            
            # === 3. Argüman ===
            # Aynı şekilde tuple gönderiyorum.
            # 1. elemanı x_end, 2. elamanı y_end
            
            # === 4. Argüman ===
            # Rectangle'ın BGR (renk )değeri. BGR değeri taşıyan color değişkeni gönderiyorum
            
            # === 5. Argüman ===
            # Rectangle'ın border (çerçeve) değeri. border değişkenini gönderiyorum
            
            # === Kullanımı ===
            # cv.rectangle(CAPTURE, (X_Start, Y_Start), (X_End, Y_End), Rectangle BGR, Rectangle Border)
            
            # Yani live olarak ekranda algılanan her yüz modelinin etrafında bir dikdörtgen çizmesini sağlıyorum

    # imshow ile live cam'i frame değişkenini kullanarak ekranda gösteriyorum
    cv.imshow('frame', frame)
    
    # # Gri görüntüyü göstermek için (Opencv'nin nasıl gördüğünü görmek için)
    # cv.imshow('gray', gray)

    if cv.waitKey(20) and 0xFF == ord('q'):
        break 

# Pencereyi kapatıyorum
cv.destroyAllWindows()