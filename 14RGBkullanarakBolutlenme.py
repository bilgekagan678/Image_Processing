"""
RGB kullanarak bölütlenme, bir görüntüyü renk bileşenlerine ayırarak belirli renk aralıklarına göre bölütlenmesini ifade eder. 

Formülü:

Bölütlemek istediğimiz ortalama renk, a RGB vektörü ile ifade edilsin. z, RGB uzayında gelişigüzel bir noktayı belirtsin.

D(z,a) = ||z - a|| = [((z-a)^T)(z-a)]^(1/2) = [(zR-aR)^2+ (zG-aG)^2 + (zB-aB)^2]^(1/2)

"""

import cv2
import numpy as np

def rgb_bolutleme(goruntu):
    # Görüntüyü RGB renk uzayına dönüştürme
    rgb_goruntu = cv2.cvtColor(goruntu, cv2.COLOR_BGR2RGB)

    # Belirli bir renk aralığı için alt ve üst sınırları tanımlama (mavi renk için örnek)
    alt_sinir = np.array([100, 0, 0], dtype=np.uint8)
    ust_sinir = np.array([140, 255, 255], dtype=np.uint8)

    # Belirli renk aralığındaki pikselleri maskeleme
    maske = cv2.inRange(rgb_goruntu, alt_sinir, ust_sinir)

    # Orijinal görüntüdeki belirli renk bölütlenmiş görüntüyü al
    bolutlenmis_goruntu = cv2.bitwise_and(goruntu, goruntu, mask=maske)

    return bolutlenmis_goruntu

# Görüntüyü yükleme
goruntu_yolu = "img.jpg"
goruntu = cv2.imread(goruntu_yolu)

# RGB bölütlenmiş görüntüyü alma
bolutlenmis_goruntu = rgb_bolutleme(goruntu)

# Görüntüleri gösterme
cv2.imshow("Orijinal Görüntü", goruntu)
cv2.imshow("Bölütlenmiş Görüntü", bolutlenmis_goruntu)

cv2.waitKey(0)
cv2.destroyAllWindows()
