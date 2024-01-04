"""
Histogram eşitleme, bir görüntünün histogramını yani piksel değerlerinin dağılımını düzenleyerek görüntünün 
kontrastını artırmaktır. Bu yöntem, görüntüdeki piksel değerlerinin dağılımını genişleterek, 
düşük kontrastlı görüntülerde daha fazla ayrıntı ortaya çıkmasına yardımcı olur.

"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_esitleme(goruntu):
    # Görüntüyü gri tonlamaya çevrilmesi
    gri_goruntu = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)
    
    # Histogramı hesaplanması
    histogram, sinir_degerleri = np.histogram(gri_goruntu.flatten(), 256, [0, 256])
    
    # Kümülatif dağılım fonksiyonunu oluşturulması
    kumulatif_dagilim = np.cumsum(histogram) / float(gri_goruntu.size)
    
    # Yeni görüntüyü oluşturulması
    esitlemis_goruntu = np.interp(gri_goruntu.flatten(), sinir_degerleri[:-1], kumulatif_dagilim * 255).reshape(gri_goruntu.shape)
    
    return esitlemis_goruntu.astype(np.uint8)

# Görüntünün yüklenmesi
goruntu = cv2.imread('img.jpg')

# Histogram eşitleme işlemi
esitlemis_goruntu = histogram_esitleme(goruntu)

# Sonuçların gösterimi
plt.subplot(1, 2, 1), plt.imshow(cv2.cvtColor(goruntu, cv2.COLOR_BGR2RGB)), plt.title('Orjinal Görüntü')
plt.subplot(1, 2, 2), plt.imshow(esitlemis_goruntu, cmap='gray'), plt.title('Histogram Eşitleme')
plt.show()
