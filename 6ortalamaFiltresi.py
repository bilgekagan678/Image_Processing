"""
Ortalama filtresi, bir pikselin etrafındaki komşu piksellerin değerlerinin ortalamasını alarak, pikselin kendi değerini günceller.

►Ortalama filtresini gerçekleştirmek için "cv2.blur()" ve "cv2.boxFilter()" işlevleri kullanılabilir.
►Her iki işlev de çekirdeği kullanarak bir görüntüyü düzgünleştirir.

"""

import cv2

# Görüntüyü yükleme
img = cv2.imread('img.jpg')

# Ortalama filtre uygulama (cv2.blur ve cv2.boxFilter kullanarak)
kernel_size = (5, 5)  # Kernel boyutu

# cv2.blur ile ortalama filtre uygulanması
blurred_img1 = cv2.blur(img, kernel_size)

# cv2.boxFilter ile ortalama filtre uygulanması
blurred_img2 = cv2.boxFilter(img, -1, kernel_size)

# Sonuçların gösterimi
cv2.imshow('Orjinal Görüntü', img)
cv2.imshow('Ortalama Filtre (cv2.blur)', blurred_img1)
cv2.imshow('Ortalama Filtre (cv2.boxFilter)', blurred_img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
