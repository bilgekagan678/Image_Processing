"""
Gaussian filtresi, bir görüntüdeki piksellerin ortalamasını alarak ve 
ağırlıklı olarak bu ortalamayı belirleyerek bir yumuşatma etkisi yaratır. 
Bu filtre genellikle gürültüyü azaltmak veya görüntüdeki küçük detayları gidermek için kullanılır.

"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Görüntünün yüklenmesi
image = cv2.imread('img.jpg')

# Gaussian filtresini uygulaması
k_size = (5, 5)  # Filtre boyutu
sigma = 0       # Standart sapma (0 ise, otomatik olarak hesaplanır)
filtered_image = cv2.GaussianBlur(image, k_size, sigma)

# Sonuçların gösterimi
plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), plt.title('Orijinal')
plt.subplot(122), plt.imshow(cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB)), plt.title('Gaussian Filtreli')
plt.show()
