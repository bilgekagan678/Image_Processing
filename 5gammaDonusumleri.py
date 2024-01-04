"""
Gamma dönüşümleri, görüntü işlemede parlaklık değerlerini düzeltmek veya ayarlamak için kullanılan bir tekniktir.

Gamma dönüşümü şu formülle ifade edilir:
O=I^γ

O: Çıkış görüntüsü
I: Giriş görüntüsü
γ: Gamma değeri

Gamma değeri 1 olduğunda, çıkış görüntüsü giriş görüntüsü ile aynıdır. 
Gamma değeri arttıkça, görüntünün parlaklık değerleri artar. 
Gamma değeri azaldıkça (1'den küçük), görüntünün parlaklık değerleri azalır.
"""

import cv2
import numpy as np

def gamma_correction(image, gamma=1.0):
    # Giriş görüntüyü 0 ile 1 arasına normalize etme
    normalized_image = image / 255.0
    
    # Gamma düzeltme uygulama
    corrected_image = np.power(normalized_image, gamma)
    
    # 0-255 aralığına geri getirme
    corrected_image = (corrected_image * 255).astype(np.uint8)
    
    return corrected_image

# Giriş görüntüsü yükleme
input_image = cv2.imread("img.jpg")

# Gamma değeri belirleme (örneğin 1.5)
gamma_value = 1.5

# Gamma düzeltme işlemi uygulama
output_image = gamma_correction(input_image, gamma_value)

# Giriş ve çıkış görüntüleri gösterilirmesi
cv2.imshow("Input Image", input_image)
cv2.imshow("Gamma Corrected Image", output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
