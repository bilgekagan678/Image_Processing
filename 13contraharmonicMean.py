"""
Contraharmonic Mean (CHM), genellikle gürültülü piksellerle başa çıkmak için kullanılır. 
Bu filtre, bir pikselin etrafındaki bir bölge içindeki piksellerin matematiksel bir 
işleme tabi tutulmasıyla elde edilir. Contraharmonic Mean, piksellerin belirli bir 
kuvvet ile toplanması ve bu toplamın belirli bir kuvvetle bölünmesiyle hesaplanır.

Contraharmonic Mean formülü şu linkteki gibidir:
https://wikimedia.org/api/rest_v1/media/math/render/svg/fa664cf6f157dae4c0d31558cc9d4a82ecd24a5b

"""

import numpy as np
from scipy.ndimage import convolve
import cv2

def contraharmonic_mean(image, size, Q):
    # Giriş görüntüsünü bir NumPy dizisine dönüştürme
    image_array = np.array(image, dtype=float)
    
    # Filtre çekirdeğini oluşturma
    kernel = np.ones((size, size))
    
    # Görüntüyü filtre ile konvolüsyon yapma
    numerator = convolve(image_array ** (Q + 1), kernel)
    denominator = convolve(image_array ** Q, kernel)
    
    # Sıfıra bölme hatasını önlemek için kontrol
    result = np.where(denominator != 0, numerator / denominator, 0)
    
    # Sonuçları 0 ile 255 arasında kırpma
    result = np.clip(result, 0, 255)
    
    # Sonuçları tam sayıya dönüştürme
    result = np.round(result).astype(np.uint8)
    
    return result

# Örnek kullanım
image_path = 'img.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

filtered_image = contraharmonic_mean(image, size=3, Q=1)

# Giriş ve çıkış görüntülerini göster
cv2.imshow('Input Image', image)
cv2.imshow('Contraharmonic Mean Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
