# 엣지 검출

# 엣지
# 픽셀 값의 급격한 변화 영역

# 발생 원인:
# - 물체의 경계
# - 텍스쳐의 경계
# - 깊이 불연속
# - 조명 변화

# 수학적 정의:
# 1차 미분의 극값(기울기가 최대인 점)
# 2차 미분의 영교차점(Zero Crossing)

# Sobel

# Scharr 연산자
# Sobel 연산자의 개선 버전, 회전 불변성을 향상시켜 더 정확한 기울기를 계산

# Sobel 문제점:
# 특정 각도(0, 45, 90, 135)의 엣지에만 최적화
# -> 다른 각도의 엣지는 정확도가 떨어짐

# Scharr X:         Scharr Y:
# [-3 0 3]         [-3 -10 -3]
# [-10 0 10]       [ 0   0  0]
# [-3 0 3]         [ 3  10  3]

# 정확도
# 회전 불변성
# 대신 3x3만

# 언제 Scharr를 사용하는가?
# 정밀한 엣지 방향 계산 필요
# 작은 각도 차이가 중요한 경우
# 회전 불변 특징 추출

# 언제 Sobel를 사용하는가?
# 일반적인 엣지 검출
# 더 큰 커널이 필요한 경우
# 속도보다 유연성

import cv2
import numpy as np

img = np.random.randint(50, 200, (200, 300), dtype=np.uint8)
# cv2.Scharr(src, ddepth, dx, dy)
scharr_x = cv2.Scharr(img, cv2.CV_64F, 1, 0)
scharr_y = cv2.Scharr(img, cv2.CV_64F, 0, 1)

magnitude = np.sqrt(scharr_x ** 2 + scharr_y ** 2)
magnitude = np.clip(magnitude, 0, 255).astype(np.uint8)

# Sobel과 비교
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel_mag = np.sqrt(sobel_x ** 2 + sobel_y ** 2)

print(f'Scharr 최대: {magnitude.max()}')
print(f'Sobel 최대: {sobel_mag.max():.2f}')


# Laplacian

# LoG(Laplacian of Gaussian)
def laplacian_of_gaussian(img, sigma=1.0, ksize=5):
    '''LoG 적용'''
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) if len(
        img.shape) == 3 else img

    # 가우시안 블러
    blurred = cv2.GaussianBlur(gray, (ksize, ksize), sigma)

    # Laplacian
    laplacian = cv2.Laplacian(blurred, cv2.CV_64F)

    # 정규화
    log_result = cv2.normalize(
        np.abs(laplacian), None, 0, 255, cv2.NORM_MINMAX)

    return log_result.astype(np.uint8)


# img = np.random.randint(50, 200, (200, 300, 3), dtype=np.uint8)
img = cv2.imread('Prac/Python/AI&OpenCV/1230/dog.png')

sigmas = [0.5, 1.0, 2.0, 3.0]
results = []

for sigma in sigmas:
    result = laplacian_of_gaussian(img, sigma=sigma)
    results.append(result)
    print(f'sigma={sigma}: 엣지 픽셀 수 = {np.sum(result > 50)}')

# 시각화
display = np.hstack(results)
cv2.imshow('display', display)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Canny Edge Deletion
# Canny 알고리즘 단계

# 최적의 엣지 검출 알고리즘
# 낮은 오류율: 실제 엣지만 검출, 가짜 엣지 최소화
# 정확한 위치: 엣지의 정확한 위치 찾기
# 단일 응답: 한나의 엣지에 하나의 응답만

# 5단계 알고리즘
# 1. 가우시안 블러(Gaussian Blur)
# - 목적: 노이즈 제거
# - 이유: 노이즈가 있으면 엣지로 오판

# 원본 (노이즈 포함):
# [100 250 105 110] <- 250은 노이즈
# 가우시안 블러 후:
# [100 120 110 110] <- 노이즈 완화됨


# 2. 그라디언트 계산(Gradient Calculation)
# - 목적: 엣지 크기와 방향 계산
# - 방법: Sobel로 X, Y 방향 기울기

# 3. 비최대 억제(Non-Maximum Supperssion, NMS)
# - 목적: 얇은 엣지 생성
# - 방법: 엣지 방향에서 최대값만 유지

# 4. 이중 임계값
# 목적: 엣지 분류
# 결과:
# - 강한 엣지: high  threshold 이상(확실한 엣지)
# - 약한 엣지: low - high threshold(애매한 엣지)
# - 비엣지: low threshold 이하

# 5. 히스테리시스(Hysteresis / Edge Tracking)
# 목적: 연결된 엣지만 유지
# 방법: 강한 엣지에 연결된 약한 엣지만 최종 엣지로 채택
