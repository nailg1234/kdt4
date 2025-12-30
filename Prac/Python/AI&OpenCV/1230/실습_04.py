# 실습1. Sobel 필터 비교(기본)
# Sobel 필터의 방향별 결과를 비교하세요.
# - 수평(x), 수직(y), 크기(magnitude) 각각 계산
# - 3개를 나란히 표시
# - 어떤 엣지가 강조되는지 관찰

# 힌트: cv2.Sobel(), cv2.magnitude()

import cv2
import numpy as np

img = cv2.imread('Prac/Python/AI&OpenCV/1230/Cameraman.png')

sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel_mag = np.sqrt(sobel_x ** 2 + sobel_y ** 2)

cv2.imshow('sobel_x', sobel_x)
cv2.imshow('sobel_y', sobel_y)
cv2.imshow('sobel_mag', sobel_mag)

cv2.waitKey(0)
cv2.destroyAllWindows()
