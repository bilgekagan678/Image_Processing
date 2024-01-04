"""
Açma - Kapama İşlemleri morfolojik operasyonlar olarak bilinir.

► Açma, objenin dış hatlarını yumuşatır, dar geçitleri koparır,
küçük çıkıntıları yok eder.

► Kapama, hatları yumuşatmaya çalışır, fakat açmanın
tersine, küçük kırıkları ve uzun ince geçitleri birleştirir,
küçük delikleri yok eder ve hat üzerindeki aralıkları
doldurur.

"""

import cv2
import numpy as np

# Görüntüyü yükleme
image = cv2.imread('img.jpg', 0)

# Açma işlemi için kernel tanımlama
kernel_open = np.ones((5, 5), np.uint8)

# Kapama işlemi için kernel tanımlama
kernel_close = np.ones((5, 5), np.uint8)

# Açma işlemi uygulama
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel_open)

# Kapama işlemi uygulama
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel_close)

# Görüntüleri gösterme
cv2.imshow('Original Image', image)
cv2.imshow('Opening', opening)
cv2.imshow('Closing', closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
