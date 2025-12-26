# OpenCV (Open Source Computer Vision Library)

# 실시간 컴퓨터 비전을 위한 오픈소스 라이브러리

# 특징
# 2500+ 최적화된 알고리즘
# C++, Python , Java, MATLAB 지원
# Windows, Linux, macOS, Android, IOS 지원
# GPU  가속 지원 (CUDA, OpenCL)

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
# - 사전 학습 모델 로드
# - ONNX, TensorFlow, PyTorch 모델 지원

# 산업 응용
# - 자율주행
# - 의료 영상
# - 보안/감시
# - AR/VR


import cv2

print(f'OpenCV 버전: {cv2.__version__}')

# 기본 구조

# 이미지 표현
import numpy as np

# OpenCV에서 이미지 = Numpy 배열
# 이미지는 픽셀 값들의 행렬로 표현됨

# 흑백 이미지: (높이, 너비)
# 각 픽셀은 하나의 값(0~255)을 가짐
gray_img = np.zeros((100,200), dtype=np.uint8)
print(f'흑백 이미지 shape: {gray_img.shape}')  # (100, 200)

# 컬러 이미지: (높이, 너비, 채널)
# 각 픽셀은 3개의 값(BGR)을 가짐
color_img = np.zeros((100,200, 3), dtype=np.uint8)
print(f'컬러 이미지 shape: {color_img.shape}')  # (100, 200, 3)

# uint8: 0 ~ 255 범위의 정수 (8비트 부호 없는 정수)
# 가장 일반적인 이미지 데이터 타입

# OpenCV 색상 순서: RGB X => BGR (Blue, Green, Red)
# 일반적인 이미지는 RGB 순서를 사용하지만, OpenCV는 BGR 순서를 사용
# 이유: 역사적으로 카메라 제조사들이 BGR 순서를 사용했기 때문

# 빨간색 생성 예제
bgr_red = np.zeros((100,100,3), dtype=np.uint8)
bgr_red[:,:,2] = 255  # R 채널 (인덱스 2번 = 마지막)

# BGR -> RGB 변환
# 다른 라이브러리(Matplotlib, PIL 등)와 호환을 위해 필요
rgb_red = cv2.cvtColor(bgr_red, cv2.COLOR_BGR2RGB)

print(f'BGR 빨강 첫 픽셀: {bgr_red[0,0]}')  # [0, 0, 255]
print(f'RGB 빨강 첫 픽셀: {rgb_red[0,0]}')  # [255, 0, 0]

# 컬러 이미지 생성 및 채널 설정
img = np.zeros((300,300,3), dtype=np.uint8)
img[:,:,0] = 100  # Blue 채널 (인덱스 0)
img[:,:,1] = 150  # Green 채널 (인덱스 1)
img[:,:,2] = 200  # Red 채널 (인덱스 2)

# 채널 분리 - 3개의 컬러 채널을 분리된 흑백 이미지로 분해
# 각 채널은 (높이, 너비) 형태의 2D 배열이 됨
b, g, r = cv2.split(img)
print(f'Blue 채널 shape: {b.shape}')    # (300, 300)
print(f'Green 채널 shape: {g.shape}')   # (300, 300)
print(f'Red 채널 shape: {r.shape}')     # (300, 300)

# 채널 병합 - 분리된 채널들을 다시 컬러 이미지로 합침
merged = cv2.merge([b, g, r])
print(f'병합 결과 shape: {merged.shape}')  # (300, 300, 3)

# 개별 채널 접근 (더 효율적인 방법)
# split()보다 빠르고 메모리 효율적
# 참조(reference)를 반환하므로 원본 수정 시 영향을 받음
blue_channel = img[:,:,0]
green_channel = img[:,:,1]
red_channel = img[:,:,2]

# ========================================
# 다양한 방법으로 이미지 생성하기
# ========================================

# 1. 검은색 이미지 (모든 픽셀이 0)
black = np.zeros((200,300, 3), dtype=np.uint8)

# 2. 흰색 이미지 (모든 픽셀이 255)
white = np.ones((300, 300, 3), dtype=np.uint8) * 255

# 3. 특정 색상으로 채운 이미지
# BGR 순서로 색상 지정
blue = np.zeros((200,300, 3), dtype=np.uint8)
blue[:, :] = (255, 0, 0)  # BGR: Blue=255, Green=0, Red=0

green = np.zeros((200,300, 3), dtype=np.uint8)
green[:, :] = (0, 255, 0)  # BGR: Blue=0, Green=255, Red=0

red = np.zeros((200,300, 3), dtype=np.uint8)
red[:, :] = (0, 0, 255)  # BGR: Blue=0, Green=0, Red=255

# 4. 랜덤 이미지 (노이즈 효과)
# 0~255 사이의 랜덤한 값으로 채움
random_img = np.random.randint(0, 256, (200, 300, 3), dtype=np.uint8)


# 5. 그라데이션 이미지
h, w = 800, 600

# 수평 그라데이션 (왼쪽→오른쪽: 어두움→밝음)
# linspace(0, 255, w): 0부터 255까지 w개의 균등한 값 생성
# tile(..., (h, 1)): 이 배열을 h번 반복하여 세로로 쌓기
gradient_h = np.tile(np.linspace(0, 255, w), (h, 1)).astype(np.uint8)

# 수직 그라데이션 (위→아래: 어두움→밝음)
# linspace(0, 255, h): 0부터 255까지 h개의 값 생성
# tile(..., (w, 1)).T: w번 반복 후 전치(transpose)하여 세로 방향으로 만들기
gradient_w = np.tile(np.linspace(0, 255, h), (w, 1)).T.astype(np.uint8)

# 컬러 그라데이션 (수평 + 수직 조합)
gradient_color = np.zeros((h,w, 3), dtype=np.uint8)
gradient_color[:,:,0] = gradient_h  # Blue 채널: 수평 그라데이션
gradient_color[:,:,2] = gradient_w  # Red 채널: 수직 그라데이션
# Green 채널은 0으로 유지


# 6. 체크보드 패턴 (체스판)
h, w = 500, 500
square = 50  # 각 사각형의 크기

# 각 픽셀이 어느 사각형에 속하는지 계산
# arange(h) // square: [0,0,...,0, 1,1,...,1, 2,2,...,2, ...]
# 예: square=50이면 0~49는 0, 50~99는 1, 100~149는 2
y = np.arange(h) // square  # 세로 방향 사각형 인덱스
x = np.arange(w) // square  # 가로 방향 사각형 인덱스

# 브로드캐스팅을 이용한 2D 패턴 생성
# y[:,None]: (10, 1) 형태로 변환 (세로 방향)
# x[None,:]: (1, 10) 형태로 변환 (가로 방향)
# 두 배열을 더하면 (10, 10) 형태의 2D 배열 생성
# % 2: 홀수/짝수 판별 (0 또는 1)
board = (y[:,None] + x[None, :]) % 2

# 0과 1을 0과 255로 변환하여 흑백 체크보드 생성
checkerboard = (board * 255).astype(np.uint8)




# ========================================
# 윈도우 생성 및 이미지 표시
# ========================================

# 선택사항: 윈도우 생성 (크기 조절 가능하게 설정)
# cv2.namedWindow('My Window', cv2.WINDOW_NORMAL)

# 이미지를 화면에 표시
# imshow(윈도우_이름, 이미지_배열)
cv2.imshow('checkerboard', checkerboard)

# 키 입력 대기
# waitKey(0): 키 입력이 있을 때까지 무한 대기
# waitKey(n): n 밀리초 동안 대기 (예: 1000 = 1초)
# 반환값: 눌린 키의 ASCII 코드
key = cv2.waitKey(0)

# 모든 윈도우 닫기
cv2.destroyAllWindows()


print()
print()
print()
print()
print()
print()