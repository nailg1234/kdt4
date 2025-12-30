# 실습3. 샤프닝 강도 조절(응용)
# 이미지를 다양한 강도로 샤프닝 하세요.
# - 기본 샤프닝 커널 사용
# - 강도를 약, 중, 강으로 조절
# - 슬라이더로 실시간 조절(선택)

import cv2
import numpy as np

# 힌트: 커널의 중심값을 조절하여 강도 변경

img = cv2.imread('Prac/Python/AI&OpenCV/1230/dog.png')

sharpen_1 = np.array([[0, -1, 0],
                      [-1, 5, -1],
                      [0, -1, 0]])

sharpen_2 = np.array([[-1, -1, -1],
                      [-1, 9, -1],
                      [-1, -1, -1]])

sharpen_3 = np.array([[1, 1, 1],
                      [1, -7, 1],
                      [1, 1, 1]])

soble_x = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])

soble_y = np.array([[-1, -2, -1],
                    [0, 0, 0],
                    [1, 2, 1]])

laplacian = np.array([[0, 1, 0],
                      [1, -4, 1],
                      [0, 1, 0]])

sharpen_img_1 = cv2.filter2D(img, -1, sharpen_1)
sharpen_img_2 = cv2.filter2D(img, -1, sharpen_2)
sharpen_img_3 = cv2.filter2D(img, -1, sharpen_3)

edge_x = cv2.filter2D(img, cv2.CV_32F, soble_x)
edge_y = cv2.filter2D(img, cv2.CV_32F, soble_y)
edge_lab = cv2.filter2D(img, cv2.CV_32F, laplacian)


cv2.imshow('sharpen_img_1', sharpen_img_1)
cv2.imshow('sharpen_img_2', sharpen_img_2)
cv2.imshow('sharpen_img_3', sharpen_img_3)
cv2.imshow('edge_x', edge_x)
cv2.imshow('edge_y', edge_y)
cv2.imshow('edge_lab', edge_lab)

cv2.waitKey(0)
cv2.destroyAllWindows()
