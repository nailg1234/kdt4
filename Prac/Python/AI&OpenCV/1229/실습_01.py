# 실습1: 컬러 이미지 생성(기본)
# 빨강, 초록, 파랑 3개의 가로로 나란히 있는 이미지를 만들어 보세요.
# - 크기 300x900(높이x너비)
# 각 정사각형은 300x300크기

import cv2
import numpy as np

# 힌트: np.zeros로 시작하고, 슬라이싱으로 영역별 색상 지정
img = np.zeros((300, 900, 3), dtype=np.uint8)

img[:, :300] = [0, 0, 255]
img[:, 300:600] = [0, 255, 0]
img[:, 600:] = [255, 0, 0]
cv2.imshow('prac_01', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
