# 데이터셋 분할

# 왜 데이터를 나누는가?
# 학교 시험 비유:
# 나쁜 방법 (커닝):
# 시험 문제로 공부
# 시험 문제로 시험
# 결과 100점! 

# 좋은 방법:
# 연습 문제로 공부
# 다른 문제로 시험
# 결과: 진짜 실력!

# ML에서의 의미
# 문제: 학습에 사용한 데이터로 평가하면?
# 외워버린 것과 같음(과적합)
# 새로운 데이터에서 성능 나쁨

# 해결: 데이터를 나누어서
# 일부로 학습
# 나머지로 평가
# 진짜 일반화 성능 확인


# 세가지 데이터셋
# 훈련/ 검증/ 테스트
# 전체데이터
# |
# ├── 훈련 세트(Training Set) 60-80%
# |     └── 모델 학습에 사용
# |
# ├── 검증 세트 (Validation Set): 10~20%
# |     └── 하이퍼 파라미터 튜닝에 사용
# |
# ├── 테스트 세트 (Test Set): 10~20%
# |     └── 최종 성능 평가에 사용

# 각 세트의 역할
# 훈련 세트 
# - 모델이 패턴을 학습
# - "공부할 때 보는 교재"

# 검증 세트 
# - 학습 중간에 성능 확인
# - 하이퍼 파라미터 조정
# - "모의고사"

# 테스트 세트
# - 최종 성능만 측정
# - 한 번만 사용!
# - "실제 시험"


# 기본 분할 (훈련/테스트)
from sklearn.model_selection import train_test_split
import numpy as np

# 샘플 데이터
x = np.array([[1, 2], [3, 4], [5, 6], [7, 8],
              [9, 10], [11, 12], [13, 14], [15, 16],
              [17, 18], [19, 20]])
y = np.array([0, 0, 0, 1, 1, 0, 1, 1, 0, 1])

# 훈련/테스트 분할 (80:20)
x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.2,  # 테스트 비율 20%
    random_state=42  # 재현성을 위한 시드 (난수 고정)
)

print(f'훈련 데이터: {len(x_train)}')
print(f'테스트 데이터: {len(x_test)}')

# pip install scikit-learn

# 훈련/검증/테스트 분할

# 1단계: 훈련 + 검증 vs 테스트 (80:20)
x_temp, x_test, y_temp, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)
# 2단계: 훈련 vs 검증 (75:25)
# 0.25 * 0.8 = 0.2 → 최종적으로 60:20:20 비율
x_train, x_val, y_train, y_val = train_test_split(
    x_temp, y_temp, test_size=0.25, random_state=42
)

print(f'훈련 데이터: {len(x_train)}')
print(f'검증 데이터: {len(x_val)}')
print(f'테스트 데이터: {len(x_test)}')

# 계층 분할(Stratified)

# 클래스 비율을 유지하면서 분할

# 불균형 데이터 예시
y = np.array([0,0,0,0,0,0,0,1,1,1]) # 7 : 3 

# stratify 옵션 사용
x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.2,  # 테스트 비율 20%
    stratify=y,  # 클래스 비율 유지!
    random_state=42  # 재현성을 위한 시드
)

print(f'전체 클래스 비율: {np.bincount(y)}')
print(f'훈련 클래스 비율: {np.bincount(y_train)}')
print(f'테스트 클래스 비율: {np.bincount(y_test)}')


# 기본적으로 shuffle=True (데이터 섞음)

# 시계열 데이터는 셔플하면 안 됨!
# x_train, x_test, y_train, y_test = train_test_split(
#     x,y,
#     test_size=0.2, # 테스트 비율
#     # stratify=y ,  # 클래스 비율 유지!
#     shuffle=False # 순서 유지
#     random_state=42 # 재현성을 위한 시도
# )

# 적절한 비율
# 데이터 양에 따른 권장 비율:

# 대용량 (10만 이상):
# - 훈련 98% : 테스트 2%
# - 검증은 별도로 1-2%

# 중간 (1000 ~ 10만):
# - 훈련 80% : 테스트 20%
# - 60 : 20 : 20

# 소량 (1000 미만 ):
# - 교차 검증 권장
print()
print()
print()
print()

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np

# 붓꽃 데이터 로드
iris = load_iris()
x = iris.data       # 특성 (꽃잎, 꽃받침 크기)
y = iris.target     # 라벨 (품종)

print(f"전체 데이터: {x.shape}")
print(f"클래스: {np.unique(y)}")  # [0, 1, 2]

# 분할
x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.2,  # 테스트 비율 20%
    stratify=y,  # 클래스 비율 유지!
    random_state=42  # 재현성을 위한 시드
)

print(f'훈련 데이터: {len(x_train)}')
print(f'테스트 데이터: {len(x_test)}')


print(f'전체 클래스 비율: {np.bincount(y)}')
print(f'훈련 클래스 비율: {np.bincount(y_train)}')
print(f'테스트 클래스 비율: {np.bincount(y_test)}')

# 핵심 정리
# 1. 데이터 분할의 목적: 과적합 방지 및 일반화 성능 측정
# 2. 세 가지 데이터셋:
#    - 훈련(60-80%): 모델 학습
#    - 검증(10-20%): 하이퍼파라미터 튜닝
#    - 테스트(10-20%): 최종 성능 평가
# 3. train_test_split 주요 파라미터:
#    - test_size: 테스트 데이터 비율
#    - random_state: 재현성을 위한 난수 시드
#    - stratify: 클래스 비율 유지 (분류 문제)
#    - shuffle: 데이터 섞기 (기본값 True)
# 4. 주의사항:
#    - 시계열 데이터는 shuffle=False 사용
#    - 불균형 데이터는 stratify 옵션 필수
#    - 테스트 데이터는 한 번만 사용!
# 5. 데이터 양에 따른 권장 비율:
#    - 대용량(10만+): 98:1:1 또는 96:2:2
#    - 중간(1천-10만): 80:20 또는 60:20:20
#    - 소량(1천 미만): 교차 검증(Cross-Validation) 권장