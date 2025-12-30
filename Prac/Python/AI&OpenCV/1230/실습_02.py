# 실습2. 블러 효과 비교(응용)
# 같은 이미지에 서로 다른 블러 필터를 적용하고 비교하세요.
# - 평균 블러, 가우시안 블러, 미디언 블러
# - 각각 다른 커널 크기(3, 7, 15) 사용
# - 3x3 그리드로 결과 비교

import cv2
import numpy as np

# 힌트 cv2.blur(), cv2.GaussianBlur(), cv2,medianBlur()

img = cv2.imread('Prac/Python/AI&OpenCV/1230/dog.png')

blur_3 = cv2.blur(img, (3, 3), 3)
blur_7 = cv2.blur(img, (3, 3), 7)
blur_15 = cv2.blur(img, (3, 3), 15)

gauss_3 = cv2.GaussianBlur(img, (3, 3), 3)
gauss_7 = cv2.GaussianBlur(img, (3, 3), 7)
gauss_15 = cv2.GaussianBlur(img, (3, 3), 15)

median_3 = cv2.medianBlur(img, 3)
median_7 = cv2.medianBlur(img, 7)
median_15 = cv2.medianBlur(img, 15)

cv2.imshow('blur_3', blur_3)
cv2.imshow('blur_7', blur_7)
cv2.imshow('blur_15', blur_15)

cv2.imshow('gauss_3', gauss_3)
cv2.imshow('gauss_7', gauss_7)
cv2.imshow('gauss_15', gauss_15)

cv2.imshow('median_3', median_3)
cv2.imshow('median_7', median_7)
cv2.imshow('median_15', median_15)

cv2.waitKey(0)
cv2.destroyAllWindows()
