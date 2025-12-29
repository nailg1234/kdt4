import cv2
import numpy as np

# 색상 공간 변환
# 주요 색상 공간

# RGB/BGR (Red, Green, Blue)
# - 가산 혼합(빛의 3원색)
# - 디스페이 표준
# - OpenCv는 BGR 순서

# HSV (Hue, Saturation, Value)
# - Hue: 색상 (0 - 179)
# - Saturation: 채도 (0-255)
# - Value: 명도 (0-255)
# - 색상 검출에 유용

# HLS(Hue, Lightness, Saturation)
# - HSV와 유사
# - 명도 대신 밝기(Lightness)

# YCrCb(휘도, 색차)
# - Y: 휘도 (밝기)
# - Cr, Cb: 색차
# - 영상, 압축에 사용

# Lab(CIE L*a*b)
# - L: 밝기 (0-100)
# - a: 녹색-빨강 축
# - b: 파랑-노랑 축
# - 인간 시각에 가까움

# Grayscale (흑백)
# - 단일 채널
# - 밝기 정보만

import matplotlib.pyplot as plt

# BGR 이미지 생성
h, w = 400, 600
# 검은색 이미지
img = np.zeros((h, w, 3), dtype=np.uint8)

# 그라데이션 색상 생성
for i in range(w):
    hue = int(180 * i / w)  # 0 - 179
    hsv = np.array([[[hue, 255, 255]]], dtype=np.uint8)
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    img[:, i] = bgr[0, 0]

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

# 시각화
fig, axes = plt.subplots(2, 2, figsize=(12, 6))

axes[0, 0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axes[0, 0].set_title("Original (BGR)")

axes[0, 1].imshow(gray, cmap='gray')
axes[0, 1].set_title("Grayscale")

axes[1, 0].imshow(hsv[:, :, 0], cmap='hsv')
axes[1, 0].set_title("HSV - Hue Channel")

axes[1, 1].imshow(lab[:, :, 0], cmap='gray')
axes[1, 1].set_title("Lab - L Channel")

for ax in axes.flat:
    ax.axis('off')

plt.tight_layout()
plt.show()

# 테스트 이미지 생성
img_bgr = np.zeros((200, 200, 3), dtype=np.uint8)
img_bgr[:100, :100] = [255, 0, 0]  # 파란색 (좌측 상단)
img_bgr[:100, 100:] = [0, 255, 0]  # 초록색 (우측 상단)
img_bgr[100:, :100] = [0, 0, 255]  # 빨간색 (좌측 하단)
img_bgr[100:, 100:] = [255, 0, 255]  # 보라색 (우측 하단)

# 색상 공간 변환
gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
hls = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HLS)
ycrcb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2YCrCb)
lab = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2LAB)

print(f"BGR: {img_bgr.shape}")
print(f"GRAY: {gray.shape}")
print(f"RGB: {rgb.shape}")
print(f"HSV: {hsv.shape}")
print(f"HLS: {hls.shape}")
print(f"YCrCb: {ycrcb.shape}")
print(f"Lab: {lab.shape}")
# BGR: (200, 200, 3)
# GRAY: (200, 200)
# RGB: (200, 200, 3)
# HSV: (200, 200, 3)
# HLS: (200, 200, 3)
# YCrCb: (200, 200, 3)
# Lab: (200, 200, 3)


img_bgr = np.array([[
    [255, 0, 0],
    [0, 255, 0],
    [0, 0, 255]]])

img_bgr = img_bgr.astype(np.uint8)

# OpenCV 변환
# BGR -> Grayscale 공식
# Gray = 0.299*R + 0.587*G + 0.114*B
gray_cv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

print(gray_cv)
# [[ 29 150  76]]
