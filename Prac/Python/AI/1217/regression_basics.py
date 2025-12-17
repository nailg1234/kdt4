# 선형 회귀의 원리
# 선형 회귀(Linear Regression)

# 데이터를 가장 잘 설명하는 직선을 찾는 것

# 예측: y = wx + b
# - w: 기울기 (가중치, weight)
# - b: 절편 (편향, bias)
# - x: 입력
# - y: 출력 (예측값)

# 실생활 예시
# 공부 시간(x) -> 시험 점수 (y)
# 집 면적 (x) -> 집 가격(y)
# 광고비(x) -> 매출(y)
# 온도(x) -> 아이스크림 판매량(y)


# 손실 함수

# 오차 측정
# 예측이 얼마나 틀렸는지 측정해야 함

# 오차 = 실제값 - 예측값 = y - ŷ

# 문제 : 오차가 양수/음수 섞여 있으면 상쇄됨
# 해결 : 오차를 제곱!

# MSE(Mean Squared Error)
# MSE = 평균((실제값 - 예측값)²) = (1/n) × Σ(yi - ŷi)²

# 특징
# - 오차가 클수록 큰 페널티 (제곱 효과)
# - 항상 양수
# - 미분 가능 (경사하강법에 유리)

# 수식으로 표현
# 예측 : ŷ = wx + b

# 손실 함수:
# L(w, b) = (1/n) × Σ(yi - (wxi + b))²

# 목표 : L을 최소화하는 w, b 찾기

# 최소 제곱법

# 정규 방정식
# 손실 함수를 w, b로 미분하고 0으로 놓으면 최적의 w,b를 구하는 공식 유도 가능

# w = Σ(xi - x̄)(yi - ȳ) / Σ(xi - x̄)²
# b = ȳ - w × x̄

# x̄ = x의 평균
# ȳ = y의 평균

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 데이터
x_1d = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# 평균
x_mean = np.mean(x_1d)
y_mean = np.mean(y)

# 최소제곱법으로 직접 계산
print("=" * 50)
print("1. 최소제곱법으로 직접 계산")
print("=" * 50)

numerator = np.sum((x_1d - x_mean) * (y - y_mean))
denominator = np.sum((x_1d - x_mean) ** 2)

w = numerator / denominator
b = y_mean - w * x_mean

print(f'기울기 (w): {w:.4f}')
print(f'절편 (b): {b:.4f}')
print(f'예측식: y = {w:.2f}x + {b:.2f}')

# Scikit-learn으로 선형 회귀
print("\n" + "=" * 50)
print("2. Scikit-learn으로 선형 회귀")
print("=" * 50)

# 데이터 준비 (2차원 배열 필요)
x = x_1d.reshape(-1, 1)

# 모델 생성 및 학습
model = LinearRegression()
model.fit(x, y)

# 파라미터 확인
print(f'기울기: {model.coef_[0]:.4f}')
print(f'절편: {model.intercept_:.4f}')

# 예측
y_pred = model.predict(x)
print(f'예측값: {y_pred}')

# 시각화
print("\n" + "=" * 50)
print("3. 시각화")
print("=" * 50)

# 폰트 깨짐 해결
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(10, 6))

# 데이터 점
plt.scatter(x, y, color='blue', s=100, label='실제 데이터')

# 회귀선
plt.plot(x, y_pred, color='red', linewidth=2, label='회귀선')

# 오차 시각화
for i in range(len(x)):
    plt.plot([x[i], x[i]], [y[i], y_pred[i]], 'g--', alpha=0.5)


plt.xlabel('x')
plt.ylabel('y')
plt.title('선형 회귀')
plt.legend()
plt.grid(True)
plt.show()

# 선형 회귀의 가정
# 주요 가정
# 1. 선형성
# - x와 y 사이에 선형 관계 존재

# 2. 독립성
# - 오차들이 서로 독립적

# 3. 등분산성
# - 오차의 분산이 일정

# 4. 정규성
# - 오차가 정규분포를 따름

# 가정 위반시
# 선형성 위반:
# - 데이터가 곡선 패턴
# - -> 다항 회귀, 비선형 모델

# 이상치 존재:
# - 극단적인 값이 결과 왜곡
# - -> 이상치 제거 또는 robust 회귀


# R² Score 1에 가까우면 어떤 의미
# 모델이 데이터를 잘 설명한다는 의미
# R² = 1 완벽한 예측 (오차가 없음)
# R² = 0 평균으로 예측하는 것과 동일
# R² < 0 평균보다 못한 예측

# R² = 0.95면 모델이 데이터를 변동의 95%를 설명


# 머신러닝 지표는 모델을 평하기 위한 내부 언어
# 업무를 움직이는 언어 x


# 한식 뷔페 발주
# 나쁜 예
# 요일, 메뉴, 날씨
# R² = 0.81이고 MSE 23
# 다음주 화요일 예측 방문 138명입니다.

# 핵심 메세지 (한 문장)
# 다음주 화요일은 평균보다 손님이 15~20% 많을 가능성이 높아서
# 재료를 기준 대비 10% 추가 발주가 안전하다.

# 영양사
# 고기류 메뉴에 있을 때 방문객 18% 증가하는 패턴이 반복
# 이번 주 메뉴 구성 기준으로 보면 고기 반찬 기준량을 1.2배 준비하는게 적절하다.

# 조리 담당
# 피크 시간대 12:10~ 12:40에 집중될 확률이 높아서
# 이 시간 전에 주력 메뉴 1차 메뉴 준비를 끝내는게 좋을거 같다.


# 태양광 발전소
# 나쁜 예
# 태양광 발전량 예측 모델의 MAE 3.2mwh이고 정확도 87% 입니다.

# 운영담당자
# 내일 오후 1시~ 4시는 발전량이 평소 대비 30% 낮을 가능성이 높아서
# ESS방전 또는 외부 전력 보완이 필요하다.
