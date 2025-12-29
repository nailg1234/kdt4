# 실습3. ROI 복사(응용)
# 두개의 이미지를 만들고, 한 이미지의 일부를 다른 이미지에 복사해보세요.
# - 이미지1: 400x400 파란색 배경
# - 이미지2: 200x200 빨간색 이미지
# - 이미지2를 이미지1의 중앙에 복사

# 힌트: 중앙 좌표 계산 필요

import cv2
import numpy as np

blue_img = np.zeros((400, 400, 3), dtype=np.uint8)
blue_img[:] = [255, 0, 0]  # 파란색

red_img = np.zeros((200, 200, 3), dtype=np.uint8)
red_img[:] = [0, 0, 255]  # 빨간색

h1, w1 = blue_img.shape[:2]
h2, w2 = red_img.shape[:2]

y = (h1 - h2) // 2
x = (w1 - w2) // 2

blue_img[y:y+h2, x:x+w2] = red_img

cv2.imshow('prac_03_01', blue_img)
# cv2.imshow('prac_03_02', red_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
