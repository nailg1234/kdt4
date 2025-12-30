# ===== 블러 방법 비교 실습 =====
# 다양한 블러 필터의 효과를 시각적으로 비교
# - 평균 블러 (Mean Blur)
# - 가우시안 블러 (Gaussian Blur)
# - 미디안 블러 (Median Blur)

import cv2
import numpy as np

# ===== 1. 커스텀 커널 예제 =====
# 랜덤 이미지 생성 (테스트용)
img = np.random.randint(50, 200, (200, 300, 3), dtype=np.uint8)

# 커스텀 커널 생성: 중심 가중 평균 필터
# 중심 픽셀(5)에 더 큰 가중치를 부여하여 원본을 더 많이 보존
kernel = np.array([[1, 1, 1],
                   [1, 5, 1],
                   [1, 1, 1]], dtype=np.float32)

# 정규화 (커널 합을 1로 만들어 밝기 유지)
# 합 = 1+1+1+1+5+1+1+1+1 = 13
# 각 값을 13으로 나누면 합이 1이 됨
kernel = kernel / kernel.sum()

# 커널 적용
result = cv2.filter2D(img, -1, kernel)


import matplotlib.pyplot as plt

# ===== 2. 블러 방법 비교 =====
# 3가지 블러 방법 × 3가지 커널 크기 = 총 9개 결과 비교

# 비교할 블러 방법들
blur_methods = ['blur', 'gaussian', 'median']

# 비교할 커널 크기들 (작은 블러 → 중간 블러 → 강한 블러)
kernel_sizes = [3, 7, 15]

# matplotlib로 3x3 그리드 생성
# 행: 블러 방법, 열: 커널 크기
fig, axes = plt.subplots(3, 3, figsize=(12, 12))

# 각 블러 방법과 커널 크기 조합마다 적용
for i, method in enumerate(blur_methods):
    for j, ksize in enumerate(kernel_sizes):
        if method == 'blur':
            # 평균 블러: 모든 픽셀에 동일 가중치
            # cv2.blur(src, ksize)
            # - 장점: 간단하고 빠름
            # - 단점: 엣지가 흐려짐
            result = cv2.blur(img, (ksize, ksize))
            title = f'평균 블러 ({ksize} x {ksize})'

        elif method == 'gaussian':
            # 가우시안 블러: 중심에 더 큰 가중치 (가우시안 분포)
            # cv2.GaussianBlur(src, ksize, sigmaX)
            # - sigmaX=0: 커널 크기로부터 자동 계산
            # - 장점: 자연스러운 블러, 엣지 상대적으로 보존
            # - 단점: 평균 블러보다 약간 느림
            result = cv2.GaussianBlur(img, (ksize, ksize), 0)
            title = f'가우시안 블러 ({ksize} x {ksize})'

        else:  # median
            # 미디안 블러: 픽셀들의 중간값 선택
            # cv2.medianBlur(src, ksize)
            # - ksize는 홀수만 가능
            # - 장점: Salt & Pepper 노이즈 제거 탁월, 엣지 보존
            # - 단점: 가장 느림
            result = cv2.medianBlur(img, ksize)
            title = f'미디안 블러 ({ksize} x {ksize})'

        # 이미지 표시 (BGR → RGB 변환 필요)
        axes[i, j].imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
        axes[i, j].set_title(title)
        axes[i, j].axis('off')  # 축 눈금 제거

plt.tight_layout()  # 서브플롯 간격 자동 조정
plt.show()

# ===== 블러 방법 선택 가이드 =====
# 평균 블러:      일반적인 노이즈 감소, 속도 중요
# 가우시안 블러:  자연스러운 블러, 전처리 작업
# 미디안 블러:    Salt & Pepper 노이즈 제거, 엣지 보존 필요

# cv2.imshow('img', img)
# cv2.imshow('result', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
