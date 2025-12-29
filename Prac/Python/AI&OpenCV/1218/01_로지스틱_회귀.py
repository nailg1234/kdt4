# 분류 문제와 로지스틱 회귀

# 회귀(Regression)
# 연속적인 숫자 예측
# 예: 집값, 온도, 매출

# 분류(Classification)
# 범주(카테고리) 예측
# 예: 스팸/정상, 암/정상, 개/고양이

# 분류의 종류

# 이진 분류 (Binary)
# - 두 개의 클래스
# - 예: 합격/불합격, 양성/음성

# 다중 클래스 분류 (Multi-class)
# - 세 개 이상의 클래스
# - 예: 개/고양이/새, 등급 A/B/C

# 다중 레이블 분류 (Multi-label)
# - 여러 레이블 동시에 가능
# - 예: 영화 장르 (액션+로맨스+코미디)

# 선형 회귀를 쓰면 안되나?
# 문제: 합격(1)/불합격(0) 예측

# 선형 회귀 사용시:
# y = wx + b

# 문제점:
# 1. 출력이 0~1 범위를 벗어남 (예: -0.5, 1.7)
# 2. 이상치에 민감
# 3. 확률로 해석 불가

# 해결책: 로지스틱 회귀!

# 로지스틱 회귀
# 선형 회귀 출력을 0~1 범위로 변환!

# 선형: z = wx + b (범위 -∞ ~ +∞)
#            ↓
# 시그모이드 함수 적용
#            ↓
# 출력: σ(z) = 1 / (1 + e^(-z))  (범위: 0 ~ 1)

# 출력값 = 확률로 해석이 가능!

import numpy as np
import matplotlib.pyplot as plt


# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows
# plt.rcParams['font.family'] = 'AppleGothic'  # Mac
plt.rcParams['axes.unicode_minus'] = False

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# 시그모이드 함수 시각화
# z값 범위: -10 ~ 10을 100개의 점으로 생성
z = np.linspace(-10, 10, 100)
y = sigmoid(z)

plt.figure(figsize=(10, 6))
plt.plot(z, y, 'b-', linewidth=2)
plt.axhline(y=0.5, color='r', linestyle='--', label='경계 (0.5)')
plt.axvline(x=0, color='gray', linestyle='-', alpha=0.3)
plt.xlabel('z (wx + b)')
plt.ylabel('σ(z)')
plt.title('시그모이드 함수')
plt.legend()
plt.grid(True)
plt.show()

# 로지스틱 회귀 수식
# z = w₁x₁ + w₂x₂ + ... + wₙxₙ + b
# P(y=1|x) = σ(z) = 1 / (1 + e^(-z))
# P(y=1|x): x가 주어졌을 때 y=1일 확률

# 손실 함수 (Binary Cross Entropy)
# MSE 사용시 문제:
# - 볼록하지 않은 형태 -> 경사하강법 어려움

# 대안: Log Loss (Cross Entropy)

# L = -1/n × Σ[y·log(ŷ) + (1-y)·log(1-ŷ)]

# 직관
# - y=1 일때: -log(ŷ) -> ŷ가 1에 가까울수록 손실 작음
# - y=0 일때: -log(1-ŷ) -> ŷ가 0에 가까울수록 손실 작음


from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# 데이터 생성
# 재현 가능하도록 시드 고정
np.random.seed(42)
# 200개의 샘플, 2개의 특성을 가진 데이터 생성 (정규분포)
X = np.random.randn(200, 2)
# 타겟: 두 특성의 합이 0보다 크면 1, 아니면 0 (선형 분리 가능한 데이터)
y = (X[:, 0] + X[:, 1] > 0).astype(int)

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 모델 학습
# solver='lbfgs' (기본값): 최적화 알고리즘
model = LogisticRegression()
model.fit(X_train, y_train)

# 예측
y_pred = model.predict(X_test)

# 평가
print(f'정확도: {accuracy_score(y_test, y_pred):.2%}')
print(classification_report(y_test, y_pred))

# 확률 예측
# predict_proba()는 각 클래스에 속할 확률을 반환
# 결과: [[클래스0 확률, 클래스1 확률], ...]
proba = model.predict_proba(X_test)
print('확률 예측 (처음 5개)')
print(proba[:5])
print('각 행: [클래스0 확률, 클래스1 확률]')
print('예: [0.8, 0.2] -> 80% 확률로 클래스0, 20% 확률로 클래스1')
