"""
Normalizasyon ve Standartizasyon Arasındaki Farklar

1. Normalizasyon:

Normalizasyon, verileri belirli bir aralığa sıkıştırmak için kullanılan bir ölçeklendirme yöntemidir. 
Genellikle, veriler 0 ile 1 arasına ölçeklendirilir. 
Min-Max scaling olarak da adlandırılan bu yöntem, her bir özellik değerini 
o özelliğin minimum ve maksimum değerleri arasındaki orana dönüştürür. 
Bu, verilerin dağılımını korurken, özellikler arasındaki farklılıkları azaltmaya yardımcı olur.

2. Standartizasyon:

Standartizasyon, verileri ortalaması 0 ve standart sapması 1 olacak şekilde dönüştürme işlemidir. 
Z-score normalization olarak da bilinen bu yöntem, her bir özellik değerini o özelliğin ortalamasından çıkarıp, 
standart sapmasına böler. Bu sayede, veri dağılımı genellikle normal bir dağılıma daha yakın hale gelir. 
Standartizasyon, özellikler arasındaki ölçek farklarını düzeltmeye ve aykırı değerlere karşı daha dirençli olmaya yardımcı olur.


Sonuç olarak, normalizasyon genellikle verilerin belirli bir aralığa sıkıştırılmasında kullanılırken, 
standartizasyon verilerin ortalamasını 0 ve standart sapmasını 1 yaparak 
daha geniş bir kullanım alanına hitap eder. Her iki yöntem de veri hazırlığı sürecinde, özellikle uzaklık 
temelli algoritmalar için, önemli rol oynar ve model performansını artırmaya yardımcı olur.

kaynak: https://www.veribilimiokulu.com/veri-hazirliginin-vazgecilmezi-ozellik-olceklendirme/
"""

import cv2
import numpy as np

# Görüntüyü okuma
image = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)

# Normalizasyon
normalized_image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)

# Standartizasyon
mean, std_dev = cv2.meanStdDev(image)
mean = mean.squeeze()
std_dev = std_dev.squeeze()

# Standartizasyon uygulaması
standardized_image = (image - mean) / std_dev

# Görüntüleri ekrana yazdırılması
cv2.imshow('Original Image', image)
cv2.imshow('Normalized Image', normalized_image)
cv2.imshow('Standardized Image', standardized_image)


cv2.waitKey(0)
cv2.destroyAllWindows()
