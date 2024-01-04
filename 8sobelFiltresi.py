"""
Sobel filtresi, bir görüntü üzerindeki belirli yönlere ait kenarları vurgulamak için kullanılır. 
Genellikle dikey (yönü yukarı-aşağı) ve yatay (yönü sağa-sola) olarak iki farklı Sobel filtresi kullanılır.

Yatay Sobel Filtresi                      Dikey Sobel Filtresi
    -1 -2 -1                                -1  0  1
     0  0  0                                -2  0  2
     1  2  1                                -1  0  1

"""

import cv2
import numpy as np

# Görüntünün okunması
image = cv2.imread('sobel_img.jpg', cv2.IMREAD_GRAYSCALE)

# Sobel filtresini uygulanması
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=1)
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=1)

# Mutlak değerlerin alınması
sobelx = np.abs(sobelx)
sobely = np.abs(sobely)

# Sonuçları birleştirerek toplam gradyanı elde etme
sobel_combined = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

# Görüntü ve sonuçları gösterimi
cv2.imshow('Original Image', image)
cv2.imshow('Sobel Filtered Image', sobel_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
