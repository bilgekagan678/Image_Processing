"""
Görüntü işlemede smoothing yani yumuşatma görüntüdeki gürültüyü azaltmak veya görüntüdeki geçişleri düzleştirmek amacıyla kullanılır.
Sharpening yani keskinleştirme, netleştirme ise görüntüdeki kenarları veya detayları vurgulamak için kullanılır.

"""

import cv2
import numpy as np

# Görüntüyü yükleme
image = cv2.imread('img.jpg')

# 5x5 boyutunda bir kernel oluşturma
kernel_1 = np.ones((5,5),np.float32)/25

# 3x3 boyutunda başka bir kernel oluşturma
kernel_2 = np.array([[-1,-1,-1],
                   [-1, 9,-1],
                   [-1,-1,-1]])

# Görüntüyü yumuşatma
smoothed_image = cv2.filter2D(image, -1, kernel_1)

# Görüntüyü netleştirme
sharpened_image = cv2.filter2D(image, -1, kernel_2)

# Görüntüleri gösterme
cv2.imshow('Original Image', image)
cv2.imshow('Smoothed Image', smoothed_image)
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
