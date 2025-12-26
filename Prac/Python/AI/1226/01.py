# OpenCV (Open Source Computer Vision Library)

# 실시간 컴퓨터 비전을 위한 오픈소스 라이브러리

# 특징 2500+ 최적화된 알고리즘
# C++ Python, Java, MATLAB 지원
# Window, Linux, macOS, Android, IOS 지원
# GPU 가속 지원 (CUDA, OpenCL)

# 이미지 처리
# - 필터링, 변환, 색상 처리
# - 형태학적 연산
# - 에지 검출

# 객체 탐지/인식
# - 얼굴 검출
# - 물체 추적
# - 특징점 매칭

# 비디오 분석
# - 모션 검출
# - 배경 제거
# - 광학 흐름

# 딥러닝 추론
# - DNN 모듈
# - 사전 학습 모델 로그
# - ONNX, TensorFlow, PyTorch 모델 지원

# 산업 응용
# - 자율주행
# - 의료 영상
# - 보안/감시
# - AR/VR

import numpy as np
import cv2
print(f'OpenCV 버전 : {cv2.__version__}')

# 기본 구조

# 이미지 표현

# OpenCV에서 이미지 = Numpy 배열

# 흑백 이미지: (높이, 너비)
gray_img = np.zeros((100, 200), dtype=np.uint8)
print(f'흑백 이미지: {gray_img.shape}')

# 컬러 이미지: (높이, 너비, 채널)
color_img = np.zeros((100, 200, 3), dtype=np.uint8)
print(f'컬러 이미지: {color_img.shape}')

# uint8: 0 ~ 255(가장 일반적)

# OpenCV: RGB X => BGR(Blue, Green, Red)

# 빨간색 생성
bgr_red = np.zeros((100, 100, 3), dtype=np.uint8)
bgr_red[:, :, 2] = 255  # R채널(인덱스 2)

# BGR -> RGB 변환
rgb_red = cv2.cvtColor(bgr_red, cv2.COLOR_BGR2RGB)
print(f'BGR 순서: {bgr_red}')
print(f'RGB 순서: {rgb_red}')

img = np.zeros((300, 300, 3), dtype=np.uint8)
img[:, :, 0] = 100  # Blue
img[:, :, 1] = 150  # Green
img[:, :, 2] = 200  # Red

# 채널 분리
b, g, r = cv2.split(img)
print(f'Blue 채널: {b.shape}')
print(f'Green 채널: {g.shape}')
print(f'Red 채널: {r.shape}')

# 채널 병합
merged = cv2.merge([b, g, r])
print(f'병합 결과: {merged}')

# 개별 채널 접근(더 효율적)
blue_channel = img[:, :, 0]
green_channel = img[:, :, 1]
red_channel = img[:, :, 2]

# 이미지 생성
# 검은색 이미지
black = np.zeros((200, 300, 3), dtype=np.uint8)

# 흰색 이미지
white = np.ones((300, 300, 3), dtype=np.uint8) * 255

# 특정 색상 이미지
blue = np.zeros((200, 300, 3), dtype=np.uint8)
blue[:, :] = (255, 0, 0)  # BGR

green = np.zeros((200, 300, 3), dtype=np.uint8)
green[:, :] = (0, 255, 0)  # BGR

red = np.zeros((200, 300, 3), dtype=np.uint8)
red[:, :] = (0, 0, 255)  # BGR

# 랜덤 이미지
random_img = np.random.randint(0, 256, (200, 300, 3), dtype=np.uint8)


# 그라데이션 이미지
h, w = 500, 400

# 수평 그라데이션
gradient_h = np.tile(np.linspace(0, 255, w), (h, 1)).astype(np.uint8)

# 수직 그라데이션
gradient_w = np.tile(np.linspace(0, 255, h), (w, 1)).T.astype(np.uint8)

# 컬러 그라데이션
gradient_color = np.zeros((h, w, 3), dtype=np.uint8)
gradient_color[:, :, 0] = gradient_h  # Blue
gradient_color[:, :, 2] = gradient_w  # Red

# 체크보드
h, w = 500, 500

square = 50

y = np.arange(h) // square  # [0, 1, 2, 3, 4]
x = np.arange(w) // square  # [0, 1, 2, 3, 4]

# Numpy 출력 생략 끄기
np.set_printoptions(threshold=np.inf)

board = (y[:, None] + x[None, :]) % 2

checkerboard = (board * 255).astype(np.uint8)

# 좌표계와 인덱싱
# 좌표계 이해

# OpenCV 좌표계


# 윈도우 생성 및 표시
# cv2.namedWindow('My Window', cv2.WINDOW_NORMAL)
cv2.imshow('checkerboard', checkerboard)

# 키 입력 대기
key = cv2.waitKey(0)

# 모든 윈도우 닫기
cv2.destroyAllWindows()
