import cv2
import numpy as np

def contrast_stretching(image):
    # Görüntünün minimum ve maksimum piksel değerlerini bulma
    min_val = np.min(image)
    max_val = np.max(image)
    
    # Yeni aralık değerleri (0-255) için lineer dönüşüm hesaplama
    stretched_image = ((image - min_val) / (max_val - min_val)) * 255
    
    # Veri tipini uint8'ye dönüştürme
    stretched_image = stretched_image.astype(np.uint8)
    
    return stretched_image

# Örnek olarak bir görüntüyü yükleyelim
original_image = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)

# Kontrast germe uygulaması
stretched_image = contrast_stretching(original_image)

# Görüntüleri görselleştirme
cv2.imshow('Original Image', original_image)
cv2.imshow('Contrast Stretched Image', stretched_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
