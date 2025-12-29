# 과적합

# 과적합 (Overfitting) 
# 훈련 데이터를 너무 잘 외워버림

# 특징
# - 훈련 데이터 성능: 매우 높음 
# - 테스트 데이터 성능: 낮음
# - "시험 문제는 잘 맞추는데 응용이 안됨"

# 시험 공부 비유:

# 과적합 학생
# - 기출문제만 달달 외움
# - 기출 100점!
# - 새로운 문제 50점
# - '이건 안 배웠는데요?'

# 좋은 학생
# - 개념을 이해함
# - 기출 90점
# - 새로운 문제도 85점
# - 응용력 있음!


# 과소적합(Underfitting)
# 데이터의 패턴을 충분히 학습하지 못함
# 
# 특징
# - 훈련 데이터 성능: 낮음
# - 테스트 데이터 성능: 낮음
# "기본도 모르는 상태"

# 과소적합 학생
# - 공부를 거의 안 함
# - 기출 30점
# - 새로운 문제도 30점
# - '다 모르는 문제...'

# 과적합의 원인과 해결

# 원인 - 해결 방법

# 1. 모델이 너무 복잡함
# - 파라미터가 너무 많음
# - 신경망 층이 너무 깊음

# 모델 단순화
# - 더 간단한 모델 사용
# - 파라미터 수 줄이기

# 2. 데이터가 너무 적음
# - 학습할 예시가 부족
# - 모델이 데이터를 외워버림

# 더 많은 데이터 수집
# - 가장 효과적인 방법!
# - 데이터 증강 (Data Augmentation)

# 3. 노이즈까지 학습
# - 의미 없는 패턴까지 학습

# 정규화 (Regularization)
# - L1, L2 정규화
# - Dropout(딥러닝)

# 4. 학습을 너무 오래 함
# - 훈련 데이터에 점점 맞춰감

# 조기 종료 (Early Stopping)
# - 검증 성능이 떨어지기 시작하면 학습 중단


# 과소적합 원인과 해결

# 원인
# 1. 모델이 너무 단순함
# - 복잡한 패턴을 표현 못함

# 해결
# 더 복잡한 모델 사용
# - 더 많은 레이어
# - 더 많은 파라미터 

# 원인
# 2. 특성(Feature)이 부족
# - 중요한 정보가 없음

# 해결
# 특성 추가
# - 새로운 특성 만들기
# - 다항 특성 추가

# 원인
# 3. 학습이 부족
# - 에폭 수가 너무 적음

# 해결
# 더 오래 학습
# - 에폭 수 증가

# 정규화 줄이기
# - 정규화가 너무 강하면 과소 적합

# 과적합 예시
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

matplotlib.rcParams['font.family'] = 'Malgun Gothic' 

# 데이터 생성
np.random.seed(42)
X = np.linspace(0, 1, 20).reshape(-1, 1)
y = np.sin(2 * np.pi * X).ravel() + np.random.randn(20) * 0.3

# 훈련/테스트 분할
X_train, X_test = X[:15], X[15:]
y_train, y_test = y[:15], y[15:]

# 다양한 복잡도로 모델 학습
degrees = [1, 4, 15]
plt.figure(figsize=(15, 4))

for i, degree in enumerate(degrees):
    plt.subplot(1, 3, i + 1)

    # 다항 특성 생성
    poly = PolynomialFeatures(degree=degree)
    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)

    # 모델 학습
    model = LinearRegression()
    model.fit(X_train_poly, y_train)

    # 예측
    y_train_pred = model.predict(X_train_poly)
    y_test_pred = model.predict(X_test_poly)

    # 성능 계산
    train_error = mean_squared_error(y_train, y_train_pred)
    test_error = mean_squared_error(y_test, y_test_pred)

    # 시각화
    X_plot = np.linspace(0, 1, 100).reshape(-1, 1)
    X_plot_poly = poly.transform(X_plot)
    y_plot = model.predict(X_plot_poly)

    plt.scatter(X_train, y_train, label='훈련')
    plt.scatter(X_test, y_test, label='테스트', marker='s')
    plt.plot(X_plot, y_plot, 'r-', label='예측')
    plt.title(f'차수={degree}\n훈련 MSE={train_error:.3f}, 테스트 MSE={test_error:.3f}')
    plt.legend()

plt.tight_layout()
plt.show()

# 결과 해석
# 차수=1 (과소적합):
# - 너무 단순해서 데이터 패턴을 제대로 못 잡음
# - 훈련/테스트 둘 다 성능이 낮음

# 차수=4 (적절함):
# - 데이터의 주요 패턴을 잘 학습
# - 훈련/테스트 성능이 비슷하고 양호함

# 차수=15 (과적합):
# - 너무 복잡해서 노이즈까지 학습
# - 훈련 성능은 높지만 테스트 성능이 낮음

# 핵심 정리
# 1. 과적합 (Overfitting):
#    - 훈련 데이터만 잘 맞추고 새 데이터는 못 맞춤
#    - 모델이 너무 복잡하거나 데이터가 부족할 때 발생
#    - 해결: 데이터 추가, 모델 단순화, 정규화, 조기 종료
#
# 2. 과소적합 (Underfitting):
#    - 훈련/테스트 둘 다 성능이 낮음
#    - 모델이 너무 단순하거나 학습이 부족할 때 발생
#    - 해결: 더 복잡한 모델, 특성 추가, 학습 시간 증가
#
# 3. 이상적인 모델:
#    - 훈련과 테스트 성능이 비슷하고 둘 다 높음
#    - 일반화 능력이 뛰어남
#
# 4. 모델 선택 기준:
#    - 검증 데이터로 성능 모니터링
#    - 훈련/검증 성능 차이가 크면 과적합 의심
#    - 둘 다 낮으면 과소적합 의심