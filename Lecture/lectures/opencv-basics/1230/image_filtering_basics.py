# 이미지 필터링 기초

# 이미지 필터링 = 픽셀 값을 변환하는 연산

# 목적  
# - 노이즈 제거 (블러링)
# - 엣지 강조 (샤프닝)
# - 특징 추출 (엣지 검출)
# - 스타일 효과

# 방법:
# - 공간 도메인: 픽셀 직접 조작 (컨볼루션)
# - 주파수 도메인: 푸리에 변환 후 조작

import cv2
import numpy as np

'''
    커널 (Kernel) = 필터 = 마스크
    - 작은 행렬 (보통 3x3, 5x5, 7x7)
    - 이미지 위를 슬라이딩하며 연산

    컨볼루션 (Convolution)
    - 작은 행렬(커널, 필터)을 이미지 위를 한칸씩 이동(sliding)하면서
    주변 픽셀들과 연산해 새로운 픽셀 값을 만드는 과정
    
    1. 커널을 이미지의 각 픽셀에 위치
    2. 커널과 해당 영역의 픽셀을 곱함
    3. 곱한 값들의 합 = 출력 픽셀
'''

# 3x3 평균 필터 예시
# 주변 9개의 픽셀의 평균값을 구함
# 결과적으로 이미지가 부드러워짐(블러)
kernel = np.ones((3,3), dtype=np.float32)/ 9
print(f'3x3 평균 필터:')
print(kernel)

# 수동 컨볼루션 (이해용)
def manual_convolution(img, kernel):
    '''수동 컨볼루션 구현'''
    h, w = img.shape[:2]
    kh, kw = kernel.shape[:2]
    pad_h, pad_w = kh // 2, kw // 2

    # 패딩 (Padding)
    # 가장자리 픽셀은 주변이 부족함 => 패딩으로 테두리를 채움
    #
    # 패딩 방법 종류:
    # cv2.BORDER_REPLICATE: 가장자리 픽셀 복사 [aaa|abcd|ddd]
    # cv2.BORDER_REFLECT: 반사 [cba|abcd|dcb]
    # cv2.BORDER_REFLECT_101: 반사 (경계 제외) [dcb|abcd|cba]
    # cv2.BORDER_WRAP: 반대쪽으로 감싸기 [bcd|abcd|abc]
    # cv2.BORDER_CONSTANT: 상수값으로 채우기 [000|abcd|000]
    padded = cv2.copyMakeBorder(
        img,
        pad_h, pad_h,
        pad_w, pad_w,
        cv2.BORDER_REPLICATE
        )
     
    # 출력 이미지
    output = np.zeros_like(img, dtype=np.float32)

    # 컨볼루션 연산
    # 각 픽셀 위치에서 커널과의 element-wise 곱셈 후 합산
    for y in range(h):
        for x in range(w):
            # 현재 위치에서 커널 크기만큼의 영역 추출
            region = padded[y:y+kh, x: x+kw]

            if len(img.shape) == 3:  # 컬러 이미지
                # 각 채널(R, G, B)별로 독립적으로 컨볼루션 수행
                for c in range(img.shape[2]):
                    output[y, x, c] = np.sum(region[:,:,c] * kernel)
            else:  # 그레이스케일 이미지
                output[y, x] = np.sum(region * kernel)

    # np.clip: 값을 0~255 범위로 제한 (픽셀 값 범위를 벗어나지 않도록)
    # 음수는 0으로, 255 초과는 255로 조정
    return np.clip(output, 0, 255).astype(np.uint8)


# ===== cv2.filter2D =====
# OpenCV의 범용 컨볼루션 함수
# 모든 종류의 커널을 이미지에 적용할 수 있음

# 테스트 이미지 생성
img = np.random.randint(50, 200, (200, 200, 3), dtype=np.uint8)

# 3x3 평균 필터
kernel_avg = np.ones((3,3), dtype=np.float32) / 9

# filter2D 적용
# cv2.filter2D(src, ddepth, kernel)
# src: 입력 이미지
# ddepth: 출력 이미지의 데이터 타입(깊이)
#   -1: 입력과 동일한 타입 사용
#   cv2.CV_8U: 8-bit unsigned (0~255)
#   cv2.CV_32F: 32-bit float (음수 및 255 초과 값 표현 가능)
#   cv2.CV_64F: 64-bit float (더 높은 정밀도)
# kernel: 적용할 커널 (필터)
result = cv2.filter2D(img, -1, kernel_avg)

# 기본 커널

# 항등 커널
# - 필터를 적용해도 원본이 그대로 나오게 하는 커널
# - 컨볼루션을 해도 중앙 픽셀만 1배로 통과시키고 주변은 0이라 영향이 없다.
identity_kernel = np.array([
    [0,0,0],
    [0,1,0],
    [0,0,0],], dtype=np.float32)

result = cv2.filter2D(img, -1, identity_kernel)

print(f'차이: {np.sum(np.abs(img.astype(int) - result.astype(int)))}')

# cv2.imshow("Original", img)
# cv2.imshow("Filtered (3x3)", result)

# 평균 필터
# 커널 영역 내 모든 픽셀의 평균값으로 중심 픽셀을 대처하는 필터

# 노이즈 감소: 무작위 노이즈는 평균을 내면 상쇄됨
# 부드러운 효과: 급격한 변화를 완화
# 단순하고 빠름: 계산이 매우 효율적

# 크기에 따른 효과:
# - 3x3 약한 블러, 노이즈 감소 최소
# - 5x5: 중간 블러, 적당한 노이즈 감소
# - 7x7 이상: 강한 블러, 디테일 손실

# 장단점:
# 장점: 간단, 빠름, 노이즈 감소
# 단점: 엣지가 흐려짐, 디테일 손실 

img = cv2.imread('Lenna_(test_image).png')

def mean_kernel(size):
    return np.ones((size, size), dtype=np.float32) / (size * size)

# 크기별 비교
results = []
for size in [3, 5, 7, 9]:
    kernel = mean_kernel(size)
    result = cv2.filter2D(img, -1, kernel)
    results.append(result)
    print(f'{size}x{size} 평균 필터 적용')

# 시각화
display = np.hstack([img] + results)
# cv2.imshow('Mean Filter Comparion', display)


# 샤프닝 커널
# 샤프닝 (Sharpening)이란?
# 이미지의 엣지와 디테일을 강조하여 선명하게 만드는 기법

# 기본원리
# 샤프닝 = 원본 + (원본 - 블러)
#       = 원본 + 고주파 성분 강조

# 블러는 저주파 성분(부드러운 영역)을 남김
# 원본 - 블러 = 고주파 성분(엣지, 디테일)
# 고주파를 원본에 더하면 엣지가 강조됨

# sharpen_1:    [0, -1, 0]
#               [-1, 5, -1]     중심 5 = 1(원본) + 4(강조)
#               [0, -1, 0]      주변 -1 = 차이 계산

# 작동:
# - 중심값 x 5:  원본을 5배 강조
# - 주변값 x -1: 주변과의 차이를 빼서 엣지 강조
# - 합 = 1: 전체 밝기 유지

# 왜 음수 값을 사용하는가?
# - 중심 픽셀과 주변 픽셀의 차이를 계산하기 위해
# - 차이가 크면 엣지 => 더 강조됨
# - 차이가 작으면 = 평탄 영역-> 변화 없음

# 샤프닝 커널 종류별 특징

# sharpen_1: 중간 강도 샤프닝 (4방향만 고려)
# 합 = 5 + (-1)*4 = 1 (밝기 유지)
# 상하좌우만 고려하므로 대각선 방향 엣지는 약하게 강조
sharpen_1 = np.array([[0, -1, 0],
                      [-1, 5, -1],
                      [0, -1, 0]], dtype=np.float32)

# sharpen_2: 강한 샤프닝 (8방향 모두 고려)
# 합 = 9 + (-1)*8 = 1 (밝기 유지)
# 모든 방향의 엣지를 강하게 강조, 노이즈 증폭 가능성 높음
sharpen_2 = np.array([[-1, -1, -1],
                      [-1, 9, -1],
                      [-1, -1, -1]], dtype=np.float32)

# sharpen_3: 언샤프 마스킹 (Unsharp Masking)
# 합 = -7 + 1*8 = 1 (밝기 유지)
# 블러된 버전을 빼서 고주파 성분 추출
# 더 자연스러운 샤프닝, 사진 보정에 많이 사용
sharpen_3 = np.array([[1, 1, 1],
                      [1, -7, 1],
                      [1, 1, 1]], dtype=np.float32)

result1 = cv2.filter2D(img, -1, sharpen_1)
result2 = cv2.filter2D(img, -1, sharpen_2)
result3 = cv2.filter2D(img, -1, sharpen_3)

# cv2.imshow('img', img)
# cv2.imshow('result1', result1)
# cv2.imshow('result2', result2)
# cv2.imshow('result3', result3)

# 엣지 검출 커널

# 엣지 검출 (Edge Detection) 이란?
# 이미지에서 밝기가 급격하게 변하는 경계(엣지)를 찾아내는 기법

# 왜 엣지 검출이 중요한가?
# 엣지는 이미지의 가장 중요한 정보를 담고 있습니다.
# - 물체의 경계: 배경과 물체를 구분
# - 형태 정보: 물체의 윤관과 구조
# - 특징 추출: 패턴 인식, 객체 검출의 기초
# - 압축: 중요한 정보만 남김

#       원본 이미지            엣지 검출 후
# [100, 100, 100, 20, 20] -> [0, 0, 80, 0, 0]
# [100, 100, 100, 20, 20] -> [0, 0, 80, 0, 0]


# 수학적 원리:
# 엣지 = 밝기의 급격한 변화 = 미분(Gradient)이 큰 지점
# 1차 미분: 변화율(기울기)
# 2차 미분: 변화율의 변화 (곡률)

# Sobel커널 (1차 미분)

# Sobel
# 이미지의 x방향 y방향 밝기 변화율(1차 미분)을 계산하는 커널

# 왜 x,y 방향을 따로 계산하는가?
# 엣지는 방향성을 가지고 있기 때문에

# 수직 엣지 x방향으로 밝기 변화 -> Soble X로 검출
# 수평 엣지 y방향으로 밝기 변화 -> Soble Y로 검출

# Soble 커널 (x 방향)
sobel_x = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]], dtype=np.float32)

# Soble 커널 (y 방향)
sobel_y = np.array([[-1, -2, -1],
                    [0, 0, 0],
                    [1, 2, 1]], dtype=np.float32)

# Laplacian 커널 (2차 미분)
# 이미지의 2차 미분을 계산하여 엣지를 검출하는 커널

# 밝기 : 100,  100,  100,  50,  50,  50

# 1차 미분: 0,  0,  -50,  -50,  0,  0

# 2차 미분: 0,  0  -50,  +50,  0,  0

# 2차 미분의 특징:
# - 엣지 위치를 더 정확히 파악
# - 얇은 엣지 생성
# - 노이즈에 매우 민감 (2번 미분)

# Laplacian 커널
laplacian = np.array([[0, 1, 0],
                    [1, -4, 1],
                    [0, 1, 0]], dtype=np.float32)

edge_x = cv2.filter2D(img, cv2.CV_32F, sobel_x)
edge_y = cv2.filter2D(img, cv2.CV_32F, sobel_y)
edge_lap = cv2.filter2D(img, cv2.CV_32F, laplacian)

cv2.imshow('edge_x', edge_x)
cv2.imshow('edge_y', edge_y)
cv2.imshow('edge_lap', edge_lap)


# OpenCv 블러링 함수

blur_3 = cv2.blur(img, (3,3))
blur_5 = cv2.blur(img, (5,5))
blur_9 = cv2.blur(img, (9,9))

# 직사각형
blur_rect = cv2.blur(img, (9,3))

# 가우시안 블러 (Gaussian Blur)
# 가우시안(정규) 분포를 따르는 가중치를 사용하는 블러 필터

# 자연스러움: 자연계의 많은 현ㅅ상이 가우시안 분포를 따름
# - 카메라 렌즈의 초점 흐림
# - 빛의 산란
# - 측정 노이즈

# 수학적 우수성:
# - 컨볼루션 후에도 가우시안 분포 유지
# - 푸리에 변환도 가우시안 ( 주파수 영역 분석용이)
# - 최적의 저역 통과 필터 특성

# 가우시안 커널 예시
# [1/16  2/16  1/16]
# [2/16  4/16  2/16]    중심에 가장 큰 가중치
# [1/16  2/16  1/16]    멀어질수록 가중치 감소
#                       (합 = 1, 밝기 유지)

# σ(시그마): 포준편차
# σ가 크면 -> 분포가 넓게 퍼짐-> 강한 블러
# σ가 작으면 -> 분포가 좁음 -> 약한 블러

gauss_3 = cv2.GaussianBlur(img, (3,3), 0)
gauss_5 = cv2.GaussianBlur(img, (5,5), 0)
gauss_9 = cv2.GaussianBlur(img, (9,9), 0)

gauss_91 = cv2.GaussianBlur(img, (9,9), 1)
gauss_95 = cv2.GaussianBlur(img, (9,9), 5)


# cv2.imshow('gauss_3', gauss_3)
# cv2.imshow('gauss_5', gauss_5)
# cv2.imshow('gauss_9', gauss_9)
# cv2.imshow('gauss_91', gauss_91)
# cv2.imshow('gauss_95', gauss_95)


# median Blue
# 미디언 블러 (Median Blur)
# 커널 영역 내 픽셀들을 정렬하여 중간값을 선택하는 비선형 필터

# Salt & Pepper 노이즈에 효과적
# Salt & Pepper 노이즈의 특성:
# 무작위로 픽셀이 0(검정) 또는 255(흰색)로 바뀜
# 극단적인 값이지만 개수는 적음

'''
    미디언 블러:
    - 커널 영역의 중간값 사용
    - Salt & Pepper 노이즈에 효과적
    - 엣지 보존 능력 우수

    평균 블러 vs 미디언 블러:
    예) 픽셀 값: [100, 102, 98, 255(노이즈), 101]

    평균 블러: (100+102+98+255+101)/5 = 131 (노이즈에 영향받음)
    미디언 블러: 정렬 후 중간값 = 101 (노이즈 무시됨)

    따라서 극단적인 값(Salt & Pepper)은 중간값 선택 시 제외됨
'''

# Salt & Pepper 노이즈가 있는 테스트 이미지 생성
img = np.random.randint(100, 150, (300, 400, 3), dtype=np.uint8)

# 전체 픽셀 중 2%를 검정(0), 2%를 흰색(255)으로 만들어 노이즈 추가
nosie = np.random.random(img.shape[:2])
img[nosie < 0.02] = 0      # Salt (흰색 노이즈)
img[nosie > 0.98] = 255    # Pepper (검정 노이즈)


median_3 = cv2.medianBlur(img, 3)
median_5 = cv2.medianBlur(img, 5)
median_9 = cv2.medianBlur(img, 9)

# cv2.imshow('img',img)
# cv2.imshow('median_3',median_3)
# cv2.imshow('median_5',median_5)
# cv2.imshow('median_9',median_9)

# ===== 양방향 필터 (Bilateral Filter) =====
# 공간적 거리와 색상 유사도를 모두 고려하여 엣지를
# 보존하면서 블러링하는 필터
#
# 작동 원리:
# 가중치 = 거리 가중치 × 색상 차이 가중치
#
# 예시:
# 중심 픽셀(100)과 이웃 픽셀들:
# - 픽셀A(102, 가까움): 거리 가중치 높음 + 색상 유사 → 가중치 높음 ✓
# - 픽셀B(105, 가까움): 거리 가중치 높음 + 색상 유사 → 가중치 높음 ✓
# - 픽셀C(200, 가까움): 거리 가중치 높음 + 색상 다름 → 가중치 낮음 ✗ (엣지!)
#
# 결과: 같은 영역 내 픽셀만 블러링, 엣지 건너편은 제외 → 엣지 보존

# cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace)

# **d (직경)**:
# 필터링할 이웃 영역 크기
# 크면 → 더 많은 픽셀 고려, 느림
# -1이면 sigmaSpace에서 자동 계산

# **sigmaColor (색상 시그마)**:
# - 색상 차이를 얼마나 허용할지
# - 작으면 → 비슷한 색만 블러링 → 엣지 강하게 보존
# - 크면 → 다른 색도 블러링 → 가우시안과 유사
# - 권장: 50 - 150

# **sigmaSpace (공간 시그마)**:
# - 거리에 따른 가중치 범위
# - 작으면 → 가까운 픽셀만 고려
# - 크면 → 먼 픽셀도 고려
# - 권장: 50 - 150

# 사용 예: 피부 보정, 만화 효과, 노이즈 제거 (엣지는 유지)
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

cv2.imshow('bilateral',bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()