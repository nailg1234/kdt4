import os
import cv2
import numpy as np

# 이미지 저장 비교
img = np.random.randint(0, 256, (480, 640, 3), dtype=np.uint8)

# 다양한 형식으로 저장
cv2.imwrite('test_jpg_q50.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 50])
cv2.imwrite('test_jpg_q95.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 95])
cv2.imwrite('test.png', img)

# 이미지 읽기 실패 처리

# 웹캠 캡처 및 저장

# 비디오 속도 조절
