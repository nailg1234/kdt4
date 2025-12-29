# 실습2.채널 조작(응용)
# 이미지를 만들고 각 채널을 분리한 후 특정 채널만 0으로 만들어보세요.
# - 원본 이미지: 노란색(BGR: 0, 255, 255)
# - B채널을 0으로 만들면 어떤 색이 될까요?

import cv2
import numpy as np

# 노란색 이미지 생성
img = np.zeros((300, 300, 3), dtype=np.uint8)
img[:] = [0, 255, 255]

# 각 채널로 분리
img_b = img[:, :, 0]
img_g = img[:, :, 1]
img_r = img[:, :, 2]

img_b[:] = 0
img_g[:] = 255
img_r[:] = 255

cv2.imshow('prac_02', cv2.merge([img_b, img_g, img_r]))
cv2.waitKey(0)
cv2.destroyAllWindows()
