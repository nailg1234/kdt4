# 실습2. Canny 파라미터 조정(응용)
# Canny 엣지 검출기의 임계값을 조절하여 결과를 관찰하세요.
# - 낮은 임계값(50, 100)
# - 중간 임계값(100, 200)
# - 높은 임계값(150, 300)

import cv2
import numpy as np

img = cv2.imread('Prac/Python/AI&OpenCV/1230/Cameraman.png')

# Canny 엣지 (고정 임계값)
edge_low = cv2.Canny(img, 50, 100)
edge_mid = cv2.Canny(img, 100, 200)
edge_high = cv2.Canny(img, 150, 300)

# 결과 출력
cv2.imshow('edge_low', edge_low)
cv2.imshow('edge_mid', edge_mid)
cv2.imshow('edge_high', edge_high)

cv2.waitKey(0)
cv2.destroyAllWindows()
