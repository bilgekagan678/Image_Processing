"""
Laplace filtresi, bir görüntüdeki yoğunluk değişikliklerini vurgulayan bir kenar tespiti filtresidir.
Ancak, bu filtre bir blurring operasyonu olarak da kullanılabilir.

"""

import cv2
import numpy as np

# Görüntüyü yükleme
image = cv2.imread('img.jpg')

# Görüntüyü Gri tonlamaya çevir
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Laplace filtresi
laplacian = cv2.Laplacian(gray, cv2.CV_64F)

# Laplace filtresi çıkışını 0-255 arasına ölçekleme
laplacian = np.uint8(np.absolute(laplacian))

# Blurlaştırma için Laplace filtresini orijinal görüntüyle birleştirme
blurred_image = cv2.addWeighted(image, 0.7, cv2.cvtColor(laplacian, cv2.COLOR_GRAY2BGR), 0.3, 0)

# Görüntüyü gösterme
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image with Laplace', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
