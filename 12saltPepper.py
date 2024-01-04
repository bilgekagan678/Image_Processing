""""
Salt and Pepper (Tuz ve biber), bir görüntüdeki rastgele piksellerin siyah (düşük değer) 
veya beyaz (yüksek değer) renklerle değiştirilmesiyle oluşur. Salt and Pepper gürültüsü 
genellikle rastgele olarak seçilen piksellerin renk değerlerini büyük ölçüde artırır 
veya azaltır, bu da görüntünün bozulmuş veya karışık bir görünüm almasına neden olur. 

"""

import cv2
import numpy as np

def salt_and_pepper(image, salt_prob, pepper_prob):
    noisy_image = np.copy(image)

    # Salt gürültüsü eklemek
    salt_mask = np.random.rand(*image.shape) < salt_prob
    noisy_image[salt_mask] = 255

    # Pepper gürültüsü eklemek
    pepper_mask = np.random.rand(*image.shape) < pepper_prob
    noisy_image[pepper_mask] = 0

    return noisy_image

# Görüntüyü yükleyerek Salt and Pepper gürültüsü eklemek
image_path = 'img.jpg'
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

salt_prob = 0.05  # Salt gürültü olasılığı
pepper_prob = 0.05  # Pepper gürültü olasılığı

noisy_image = salt_and_pepper(original_image, salt_prob, pepper_prob)

# Görüntüleri gösterme
cv2.imshow('Original Image', original_image)
cv2.imshow('Noisy Image', noisy_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
