import cv2
import numpy as np

# ===== 엣지 검출 (Edge Detection) =====

# 엣지 (Edge)
# 픽셀 값의 급격한 변화가 일어나는 영역

# 발생 원인:
# - 물체의 경계 (전경과 배경의 구분)
# - 텍스쳐의 경계 (표면 패턴 변화)
# - 깊이 불연속 (3D 구조의 변화)
# - 조명 변화 (그림자, 하이라이트)

# 수학적 정의:
# - 1차 미분의 극값: 기울기(gradient)가 최대인 점
# - 2차 미분의 영교차점 (Zero Crossing): 부호가 바뀌는 점
#
# 예시:
# 픽셀 값:    [100, 100, 150, 200, 200]
# 1차 미분:   [  0,  50,  50,   0,   0]  ← 변화율
# 2차 미분:   [  0,  50,   0, -50,   0]  ← 변화율의 변화

# ===== Sobel 연산자 =====

# ===== Scharr 연산자 =====
# Sobel 연산자의 개선 버전, 회전 불변성을 향상시켜 더 정확한 기울기를 계산

# Sobel 문제점:
# 특정 각도 (0°, 45°, 90°, 135°)의 엣지에만 최적화
# → 다른 각도의 엣지는 정확도가 떨어짐
# → 이미지를 회전시키면 엣지 강도가 달라질 수 있음

# Scharr 커널 구조:
# Scharr X:         Scharr Y:
# [-3   0   3]     [-3  -10  -3]
# [-10  0  10]     [ 0    0   0]
# [-3   0   3]     [ 3   10   3]
#
# 중심 행/열에 더 큰 가중치(10)를 부여하여 정확도 향상
# Sobel은 중심 가중치가 2

# 장점:
# - 더 높은 정확도 (특히 대각선 방향)
# - 회전 불변성 우수
# 단점:
# - 3x3 크기만 지원 (Sobel은 5x5, 7x7 등 가능)

# 사용 가이드:
# Scharr를 사용하는 경우:
# - 정밀한 엣지 방향 계산 필요
# - 작은 각도 차이가 중요한 경우
# - 회전 불변 특징 추출

# Sobel을 사용하는 경우:
# - 일반적인 엣지 검출
# - 더 큰 커널이 필요한 경우 (노이즈가 많을 때)
# - 다양한 커널 크기 실험 필요 

img = np.random.randint(50, 200, (200, 300), dtype=np.uint8)

# cv2.Scharr(src, ddepth, dx, dy)
# src: 입력 이미지
# ddepth: 출력 깊이 (cv2.CV_64F 사용하여 음수 값도 표현)
# dx, dy: 미분 차수 (1,0은 x방향, 0,1은 y방향)
scharr_x = cv2.Scharr(img, cv2.CV_64F, 1, 0)  # x방향 (수직 엣지 검출)
scharr_y = cv2.Scharr(img, cv2.CV_64F, 0, 1)  # y방향 (수평 엣지 검출)

# 그라디언트 크기 (Gradient Magnitude) 계산
# 피타고라스 정리: √(Gx² + Gy²)
# x방향과 y방향의 기울기를 합쳐서 최종 엣지 강도 계산
magnitude = np.sqrt(scharr_x ** 2 + scharr_y ** 2)
magnitude = np.clip(magnitude, 0, 255).astype(np.uint8)

# 추가: 엣지 방향(각도)도 계산 가능
# angle = np.arctan2(scharr_y, scharr_x) * 180 / np.pi

# Sobel과 비교
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel_mag = np.sqrt(sobel_x ** 2 + sobel_y ** 2)

print(f"Scharr 최대: {magnitude.max()}")
print(f"Sobel 최대: {sobel_mag.max():.2f}")
print(f"차이: Scharr가 일반적으로 더 높은 응답값을 보임 (가중치가 더 크기 때문)")

# ===== Laplacian (라플라시안) =====
# 2차 미분을 사용한 엣지 검출
# Laplacian 커널: ∇²f = ∂²f/∂x² + ∂²f/∂y²
#
# 기본 Laplacian 커널:
# [ 0  1  0]
# [ 1 -4  1]    합 = 0 (2차 미분은 합이 0)
# [ 0  1  0]
#
# 장점: 모든 방향의 엣지 검출 (한 번에!)
# 단점: 노이즈에 매우 민감 (2번 미분하므로 노이즈 증폭)

# ===== LoG (Laplacian of Gaussian) =====
# Laplacian의 노이즈 민감성을 해결하기 위해 가우시안 블러를 먼저 적용
def laplacian_of_gaussian(img, sigma=1.0, ksize=5):
    '''LoG 적용: 가우시안 블러 → Laplacian'''
    # 그레이스케일 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) if len(img.shape) == 3 else img

    # 1단계: 가우시안 블러로 노이즈 제거
    # sigma가 클수록 더 강한 블러 → 노이즈 제거 효과 증가
    blurred = cv2.GaussianBlur(gray, (ksize, ksize), sigma)

    # 2단계: Laplacian으로 엣지 검출
    # cv2.CV_64F: 음수 값도 표현 (엣지의 방향성 정보 유지)
    laplacian = cv2.Laplacian(blurred, cv2.CV_64F)

    # 3단계: 정규화 (시각화를 위해 0~255 범위로 변환)
    # np.abs: 절댓값 (엣지 강도만 관심, 방향 무시)
    # cv2.NORM_MINMAX: 최소값을 0, 최대값을 255로 스케일링
    log_result = cv2.normalize(np.abs(laplacian), None, 0, 255, cv2.NORM_MINMAX)

    return log_result.astype(np.uint8)

img = cv2.imread('Lenna_(test_image).png')

# sigma 값에 따른 LoG 효과 비교
# sigma가 작을수록: 세밀한 엣지까지 검출 (노이즈도 많이 검출)
# sigma가 클수록: 굵은 엣지만 검출 (노이즈 적게 검출)
sigmas = [0.5, 1.0, 2.0, 3.0]
results = []

for sigma in sigmas:
    result = laplacian_of_gaussian(img, sigma=sigma)
    results.append(result)
    # 임계값 50 이상인 픽셀을 엣지로 간주하여 개수 세기
    print(f'sigma={sigma}: 엣지 픽셀 수 = {np.sum(result > 50)}')

# 결과: sigma가 증가할수록 엣지 픽셀 수가 감소 (노이즈가 제거되고 주요 엣지만 남음)

# 시각화
display = np.hstack(results)
# cv2.imshow('display',display)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Canny Edge Detection
# Canny 알고리즘 단계

# 최적의 엣지 검출 알고리즘

# 낮은 오류율: 실제 엣지만 검출, 가짜 엣지 최소화
# 정확한 위치: 엣지의 정확한 위치 찾기
# 단일 응답 : 한나의 엣지에 하나의 응답만

# 5단계 알고리즘:
# 1. 가우시안 블러(Gaussian Blur)
# - 목적: 노이즈 제거
# - 이유: 노이즈가 있음녀 엣지로 오판

# 원본 (노이즈 포함):
# [100 250 105 110]  ← 250은 노이즈
#        ↑
#  블러 없이 엣지 검출 -> 노이즈를 엣지로 오판!

# 가우시안 블러 후:
# [100 120 110 110]  ← 노이즈 완화됨



# 2. 그라디언트 계산(Gradent Calculation)
# - 목적: 엣지 크기와 방향 계산
# - 방법: Sobel로 X, Y 방향 기울기

# 3. 비최대 억제(Non-Maximum Suppression , NMS)
# - 목적 : 얇은 엣지 생성
# - 방법 : 엣지 방향에서 최대값만 유지

# 예: 수직 엣지
# 위치:  0   1   2   3   4
# 값:  100 100 200 200 200
# 크기:   0  50  50   0   0
#          ↑   ↑
#       두 픽셀 모두 큰 값

# NMS 작동:
# 1. 엣지 방향 확인 (예: 수평 방향 90°)
# 2. 그 방향에서 이웃 픽셀과 비교
# 3. 최대값만 유지, 나머지는 억제

# 결과
# 위치:  0   1   2   3   4
# 크기:   0  50  0   0   0  ← 하나만 남은(얇은 엣지!)

# 4. 이중 임계값
# 목적: 엣지 분류
# 결과: 
# - 강한 엣지: high threshold 이상 (확실한 엣지)
# - 약한 엣지: low - high threshold (애매한 엣지)
# - 비엣지 : low thrshold 이하

# 5. 히스테리시스(Hysteresis / Edge Tracking)
# 목적: 연결된 엣지만 유지
# 방법: 강한 엣지에 연결된 약한 엣지만 최종 엣지로 채택

# Canny
# Sobel: 두꺼운 엣지, 노이즈 많음
# Laplacian: 노이즈 민감
# Canny: 얇고 정확하며 연속된 엣지

# cv2.Canny(src, threshold1, threshold2, apertureSize, L2gradient)
# threshold1: low threshold
# threshold2: high threshold
# apertureSize: Sobel 커널 크기(기본 3)
# L2gradient : True 이면 L2 norm 사용 

edges = cv2.Canny(img, 50, 150)

# 다양한 임계값
edges_low = cv2.Canny(img, 30, 100)
edges_high = cv2.Canny(img, 100, 200)

# cv2.imshow('edges',edges)
# cv2.imshow('edges_low',edges_low)
# cv2.imshow('edges_high',edges_high)


# ===== 자동 임계값 설정 =====
# 이미지마다 최적의 임계값을 수동으로 찾는 것은 비효율적
# 이미지의 통계 정보(중간값)를 활용하여 자동으로 임계값 설정

def auto_canny(img, sigma=0.33):
    '''자동 임계값 Canny

    Args:
        img: 입력 이미지
        sigma: 임계값 범위 조절 파라미터 (기본값 0.33)
               작을수록: 좁은 범위 → 강한 엣지만 검출
               클수록: 넓은 범위 → 약한 엣지까지 검출
    '''
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) if len(img.shape) == 3 else img

    # 이미지 픽셀 값의 중간값 계산
    median = np.median(gray)

    # 임계값 자동 계산 (중간값 기준으로 ±sigma% 범위)
    # 예: median=100, sigma=0.33
    #     lower = (1.0 - 0.33) * 100 = 67
    #     upper = (1.0 + 0.33) * 100 = 133
    lower = int(max(0, (1.0 - sigma) * median))
    upper = int(min(255, (1.0 + sigma) * median))

    edges = cv2.Canny(gray, lower, upper)

    return edges, lower, upper

# 테스트
edges, low, high = auto_canny(img)

print(f'자동 임계값: low={low}, high={high}')
print(f'이미지의 밝기에 따라 임계값이 자동으로 조정됨')

cv2.imshow('edges', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()



