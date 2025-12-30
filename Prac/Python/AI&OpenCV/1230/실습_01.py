# 실습1. 커스텀 커널 만들기(기본)
# 자신만의 3x3 커널을 만들어 이미지에 적용해보세요.
# - 중앙 가중치가 높은 커널 생성
# - 랜덤 이미지에 적용
# - 원본과 결과 비교

import cv2
import numpy as np

# 힌트: 중앙값을 크게, 주변값을 작게 설정

img = cv2.imread('Prac/Python/AI&OpenCV/1230/dog.png')

kernel = np.array([[0, 0, 0],
                   [0, 2, 0],
                   [0, 0, 0]], dtype=np.float32)

kernel_img = cv2.filter2D(img, -1, kernel)

cv2.imshow('img', img)
cv2.imshow('kernel_img', kernel_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
