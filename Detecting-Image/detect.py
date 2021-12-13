import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img_rgb = cv.imread('mario.png') # resmin path'ini gösterdik
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY) # resmi siyah beyaz yaptık
template = cv.imread('mario_coin.png',0) # template resmimizi gösterip siyah beyaz almasını istedik
w, h = template.shape[::-1] # template'i rectangle içine almak için weight ve height'ini aldık
res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED) # matchTemplate metodu(resim,template,template metodu) hangi tespit metodunu kullanacağımızı seçtik
threshold = 0.8
loc = np.where( res >= threshold) # ne işe yaradığını anlayamadım fakat olması zorunlu kod bloğu
for pt in zip(*loc[::-1]): # Eşleşen bölgeye (ki sanırım bölgeyi 'loc' değişkenine atadık) rectangle çiziyoruz
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)
cv.imwrite('res.png',img_rgb) # yapılan resmi res.png ismiyle kaydediyoruz

# Run the Program to see the result