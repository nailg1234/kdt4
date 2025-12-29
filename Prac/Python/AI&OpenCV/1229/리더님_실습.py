# 실습

import cv2
import numpy as np

# 컬러 이미지 생성

img = np.zeros((300, 900, 3), dtype=np.uint8)

# 각 정사각형에 색상 지정
img[:, 0:300] = [0, 0, 255]
img[:, 300:600] = [0, 255, 0]
img[:, 600:900] = [255, 0, 0]

cv2.imshow('RGB Squares', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 채널 조작

# 노란색 이미지 생성 (BGR: 0, 255, 255)
img = np.zeros((200, 200, 3), dtype=np.uint8)
img[:] = [0, 255, 255]

# 각 채널로 분리
b = img[:, :, 0]
g = img[:, :, 1]
r = img[:, :, 2]

b[:] = 0
g[:] = 0
# img[:,:,0] = 0

cv2.imshow('origin', img)
cv2.imshow('B channel', cv2.merge([b, g, r]))
cv2.waitKey(0)
cv2.destroyAllWindows()


# ROI복사
img1 = np.zeros((400, 400, 3), dtype=np.uint8)
img1[:] = [255, 0, 0]  # 파란색


img2 = np.zeros((200, 200, 3), dtype=np.uint8)
img2[:] = [0, 0, 255]  # 빨간색

h1, w1 = img1.shape[:2]
h2, w2 = img2.shape[:2]

y = (h1 - h2) // 2
x = (w1 - w2) // 2

# 이미지2를 이미지 1의 중앙에 복사
img1[y:y+h2, x:x+w2] = img2

cv2.imshow('img1', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 그라데이션 이미지

# 수평 그라데이션
h_grad = np.tile(np.linspace(0, 255, 300),
                 (300, 1)).astype(np.uint8)

# 수직 그라데이션
v_grad = np.tile(np.linspace(0, 255, 300),
                 (300, 1)).T.astype(np.uint8)


# 두 그라데잇션 합성(평균)
combined = ((h_grad.astype(np.float32)
            + v_grad.astype(np.float32)) / 2).astype(np.uint8)

cv2.imshow('Horizonttal Gradient', h_grad)
cv2.imshow('Vertical Gradient', v_grad)
cv2.imshow('Combined Gradient', combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
