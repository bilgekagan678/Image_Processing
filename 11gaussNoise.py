"""
Gaussian gürültüsü, görüntüdeki piksellerde rastgele olarak oluşan 
bir tür gürültüdür ve genellikle normal (Gaussian) dağılıma sahiptir.
Bu tür gürültü, bir pikselin yoğunluğunu rastgele bir miktar değiştirerek oluşturulur.

Gaussian gürültüsü, genellikle aşağıdaki formül kullanılarak uygulanır:

Gürültülü piksel değeri = Orijinal piksel değeri + Gaussian(0, var)

Burada, Gaussian(0, var), ortalaması 0 olan ve belirli bir varyans (var) değerine sahip 
bir Gaussian dağılımından seçilmiş rastgele bir sayıdır.

"""

import numpy as np
import cv2

def add_gaussian_noise(image, mean=0, var=1000):
    row, col, ch = image.shape
    sigma = var**0.5
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    noisy = image + gauss
    noisy = np.clip(noisy, 0, 255)
    noisy = noisy.astype(np.uint8)
    return noisy

# Örnek olarak bir resmi oku
image = cv2.imread('img.jpg')

# Gaussian gürültü ekleyerek yeni bir resim oluşturma
noisy_image = add_gaussian_noise(image)

# Orjinal ve gürültülü resimleri gösterme
cv2.imshow('Original Image', image)
cv2.imshow('Noisy Image', noisy_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
