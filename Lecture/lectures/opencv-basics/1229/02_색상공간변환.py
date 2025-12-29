"""
OpenCV 기초 - 02. 색상 공간 변환

이 파일에서 배울 내용:
1. 다양한 색상 공간의 종류와 특징 이해하기
2. BGR, HSV, Grayscale 등으로 변환하는 방법
3. 각 색상 공간이 언제 유용한지 알아보기
"""

import cv2
import numpy as np

# ============================================================
# 색상 공간(Color Space)이란?
# ============================================================
"""
색상을 표현하는 방법은 여러 가지가 있어요.
우리가 보는 색을 컴퓨터가 이해할 수 있도록 숫자로 나타내는 방식이에요.

왜 여러 가지 색상 공간이 필요할까?
- 작업의 목적에 따라 적합한 색상 표현 방식이 다르기 때문!
- 예: 빨간색 물체를 찾을 때는 HSV가 더 쉬워요
"""

# ============================================================
# 주요 색상 공간 소개
# ============================================================

# 1. RGB/BGR (Red, Green, Blue)
"""
🎨 BGR (Blue, Green, Red)
- 빛의 3원색을 섞는 방식 (가산 혼합)
- 모니터나 화면에서 사용하는 표준 방식
- ⚠️ OpenCV는 BGR 순서를 사용! (다른 라이브러리는 RGB 사용)
- 값의 범위: 각 채널 0~255
"""

# 2. HSV (Hue, Saturation, Value)
"""
🌈 HSV - 색상 검출에 최적!
- Hue (색상): 0~179 (빨강, 주황, 노랑, 초록, 파랑, 보라...)
- Saturation (채도): 0~255 (선명함 정도, 0=회색, 255=선명한 색)
- Value (명도): 0~255 (밝기, 0=검정, 255=밝음)
- 💡 언제 사용? 특정 색상의 물체를 찾을 때 매우 유용!
"""

# 3. HLS (Hue, Lightness, Saturation)
"""
🎨 HLS - HSV와 유사하지만 명도 대신 밝기(Lightness) 사용
- HSV와 비슷하지만 밝기 계산 방식이 조금 달라요
"""

# 4. YCrCb (휘도, 색차)
"""
📺 YCrCb - 동영상 압축에 사용
- Y: 휘도 (밝기 정보)
- Cr, Cb: 색차 (색상 정보)
- 💡 언제 사용? 동영상 압축, JPEG 이미지 압축
"""

# 5. Lab (CIE L*a*b)
"""
👁️ Lab - 인간의 시각과 가장 유사
- L: 밝기 (0~100)
- a: 녹색~빨강 축 (-128~127)
- b: 파랑~노랑 축 (-128~127)
- 💡 언제 사용? 색상 비교, 피부색 검출
"""

# 6. Grayscale (흑백)
"""
⚫⚪ Grayscale - 가장 간단한 형태
- 단일 채널 (색상 정보 없음)
- 0(검정) ~ 255(흰색)의 밝기 정보만
- 💡 언제 사용? 처리 속도가 중요할 때, 색상이 필요 없을 때
""" 

import matplotlib.pyplot as plt

# ============================================================
# 예제 1: 무지개 그라데이션 이미지 만들고 색상 공간 변환하기
# ============================================================
h, w = 400, 600

# 검은색 빈 이미지 생성
img = np.zeros((h, w, 3), dtype=np.uint8)

# 무지개 그라데이션 색상 생성하기
# 왼쪽부터 오른쪽으로 모든 색상(빨강→주황→노랑→초록→파랑→보라)이 나타나도록
for i in range(w):
    hue = int(180 * i / w)  # 0 ~ 179 범위의 색상값 계산
    # HSV 색상 생성 (채도와 명도는 최대로)
    hsv = np.array([[[hue, 255, 255]]], dtype=np.uint8)
    # HSV를 BGR로 변환
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    # 해당 열(세로줄)에 색상 적용
    img[:, i] = bgr[0, 0]

# 다양한 색상 공간으로 변환해보기
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 흑백으로 변환
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)    # HSV로 변환
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)    # Lab으로 변환

# Matplotlib으로 결과 시각화
fig, axes = plt.subplots(2, 2, figsize=(12, 6))

# 원본 BGR 이미지 (Matplotlib은 RGB 순서라서 변환 필요)
axes[0, 0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axes[0, 0].set_title("Original (BGR)")

# Grayscale 이미지
axes[0, 1].imshow(gray, cmap='gray')
axes[0, 1].set_title("Grayscale")

# HSV의 Hue(색상) 채널만 보기
axes[1, 0].imshow(hsv[:, :, 0], cmap='hsv')
axes[1, 0].set_title("HSV - Hue Channel (색상)")

# Lab의 L(밝기) 채널만 보기
axes[1, 1].imshow(lab[:, :, 0], cmap='gray')
axes[1, 1].set_title("Lab - L Channel (밝기)")

# 축 숨기기 (더 깔끔하게)
for ax in axes.flat:
    ax.axis('off')

plt.tight_layout()
plt.show()


# ============================================================
# 예제 2: 4가지 색상 블록 만들고 다양한 색상 공간으로 변환하기
# ============================================================

# 200x200 크기의 빈 이미지 생성
img_bgr = np.zeros((200, 200, 3), dtype=np.uint8)

# 4개의 사각형 영역에 각각 다른 색상 지정
img_bgr[:100, :100] = [255, 0, 0]    # 왼쪽 위: 파란색 (BGR 순서)
img_bgr[:100, 100:] = [0, 255, 0]    # 오른쪽 위: 초록색
img_bgr[100:, :100] = [0, 0, 255]    # 왼쪽 아래: 빨간색
img_bgr[100:, 100:] = [255, 0, 255]  # 오른쪽 아래: 보라색 (파랑+빨강)

# 다양한 색상 공간으로 변환
gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)      # 흑백
rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)        # RGB (순서만 바뀜)
hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)        # HSV
hls = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HLS)        # HLS
ycrcb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2YCrCb)    # YCrCb
lab = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2Lab)        # Lab

"""
📌 색상 공간 변환 코드 정리 (외우면 편해요!)

BGR <-> RGB (순서 바꾸기)
- cv2.COLOR_BGR2RGB
- cv2.COLOR_RGB2BGR

BGR <-> Grayscale (흑백 변환)
- cv2.COLOR_BGR2GRAY
- cv2.COLOR_GRAY2BGR

BGR <-> HSV (색상 검출용)
- cv2.COLOR_BGR2HSV
- cv2.COLOR_HSV2BGR

BGR <-> HLS
- cv2.COLOR_BGR2HLS
- cv2.COLOR_HLS2BGR

BGR <-> YCrCb (동영상 압축용)
- cv2.COLOR_BGR2YCrCb
- cv2.COLOR_YCrCb2BGR

BGR <-> Lab (인간 시각 유사)
- cv2.COLOR_BGR2Lab
- cv2.COLOR_Lab2BGR
"""

# 변환 결과 확인
print(f'BGR 이미지 shape: {img_bgr.shape}')      # (200, 200, 3) - 3개 채널
print(f'Grayscale shape: {gray.shape}')           # (200, 200) - 1개 채널
print(f'HSV 이미지 shape: {hsv.shape}')          # (200, 200, 3) - 3개 채널


# ============================================================
# 예제 3: BGR을 Grayscale로 변환하는 원리 이해하기
# ============================================================
"""
BGR 이미지를 흑백으로 변환할 때, 단순히 평균을 내는 게 아니라
사람의 눈이 색상을 인지하는 특성을 고려한 가중치를 사용해요!

공식: Gray = 0.299 * R + 0.587 * G + 0.114 * B

왜 Green의 비중이 가장 클까?
- 사람의 눈은 녹색 빛에 가장 민감하기 때문!
- 파란색은 가장 덜 민감해서 가중치가 가장 작아요
"""

# 3개의 픽셀만 있는 작은 이미지 생성 (파란색, 초록색, 빨간색)
img_bgr = np.array([[
    [255, 0, 0],    # 파란색
    [0, 255, 0],    # 초록색
    [0, 0, 255]     # 빨간색
]])

img_bgr = img_bgr.astype(np.uint8)

# OpenCV의 Grayscale 변환 (위의 가중치 공식 사용)
gray_cv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

print("BGR -> Grayscale 변환 결과:")
print(gray_cv)
print("\n각 색상이 얼마나 밝게 변환되었는지 확인해보세요!")
print("초록색이 가장 밝게(값이 크게) 나타날 거예요.")