"""
Bit Plane Slicing, bir görüntüyü oluşturan piksellerin bireysel bit düzeylerini görselleştirmek için kullanılan bir tekniktir. 
Bu teknikte, bir görüntünün her pikselinin bitleri belirli bir sırayla gruplandırılır ve bu gruplar ayrı ayrı görselleştirilir. 
Bu, görüntünün farklı bit düzeylerindeki detayları incelemek için kullanışlı bir yöntemdir.

"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def bit_plane_slice(image_path, bit_index):
    # Görüntünü okunması
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Belirli bir bit düzeyindeki pikselleri alınıyor
    bit_plane = (img >> bit_index) & 1

    # Görselleştirme
    plt.figure(figsize=(8, 8))
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(bit_plane, cmap='gray')
    plt.title(f'Bit Plane {bit_index}')

    plt.show()

# Örnek olarak, "img.jpeg" adlı bir görüntüyü kullanalım ve 3. bit düzeyindeki pikselleri görselleştirelim.
bit_plane_slice('img.jpg', 3)
