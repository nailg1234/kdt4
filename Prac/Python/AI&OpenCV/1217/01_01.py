# ============================================================
# STEP 3: 최소제곱법으로 직접 계산하기
# ============================================================
# 목표: MSE가 가장 작은 w와 b 찾기
#
# 최소제곱법 공식:
# w = Σ(xi - x평균)(yi - y평균) / Σ(xi - x평균)²
# b = y평균 - w × x평균

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

print("=" * 60)
print("STEP 3: 최소제곱법으로 직접 계산")
print("=" * 60)

# 데이터 (공부 시간 vs 시험 점수)
공부시간 = np.array([1, 2, 3, 4, 5])
시험점수 = np.array([2, 4, 5, 4, 5])

print("\n[데이터]")
for i in range(len(공부시간)):
    print(f"  {공부시간[i]}시간 공부 → {시험점수[i]}점")
# [데이터]
#   1시간 공부 → 2점
#   2시간 공부 → 4점
#   3시간 공부 → 5점
#   4시간 공부 → 4점
#   5시간 공부 → 5점

# 평균 계산
공부시간_평균 = np.mean(공부시간)
시험점수_평균 = np.mean(시험점수)

# 최소제곱법 공식 적용
분자 = np.sum((공부시간 - 공부시간_평균) * (시험점수 - 시험점수_평균))
분모 = np.sum((공부시간 - 공부시간_평균) ** 2)

w = 분자 / 분모  # 기울기
b = 시험점수_평균 - w * 공부시간_평균  # 절편

print(f"\n[결과]")
print(f"  기울기 (w): {w:.4f}")
print(f"  → 1시간 더 공부하면 {w:.2f}점 오름")
print(f"  절편 (b): {b:.4f}")
print(f"  → 공부 안해도 기본 {b:.2f}점")
print(f"  예측식: y = {w:.2f}x + {b:.2f}\n")
# [결과]
#   기울기 (w): 0.6000
#   → 1시간 더 공부하면 0.60점 오름
#   절편 (b): 2.2000
#   → 공부 안해도 기본 2.20점
#   예측식: y = 0.60x + 2.20


# ============================================================
# STEP 4: scikit-learn으로 쉽게 하기
# ============================================================
# 위 계산을 라이브러리가 자동으로 해줍니다!
# 핵심 코드 3줄:
# 1. model = LinearRegression()  # 모델 만들기
# 2. model.fit(X, y)             # 학습하기
# 3. model.predict(X)            # 예측하기

print("=" * 60)
print("STEP 4: scikit-learn 사용")
print("=" * 60)

# 데이터 준비 (scikit-learn은 2차원 배열 필요)
X = 공부시간.reshape(-1, 1)
y = 시험점수

# 3줄로 끝!
model = LinearRegression()
model.fit(X, y)
예측점수 = model.predict(X)

print(f"\n[결과]")
print(f"  기울기: {model.coef_[0]:.4f}")
print(f"  절편: {model.intercept_:.4f}")
print(f"  → 직접 계산한 것과 동일!")
print(f"  예측점수 : {예측점수}")
# [결과]
#   기울기: 0.6000
#   절편: 2.2000
#   → 직접 계산한 것과 동일!
#   예측점수 : [2.8 3.4 4.  4.6 5.2]


# ============================================================
# STEP 5: 시각화
# ============================================================
# 그래프로 보면 더 명확!
# - 파란 점: 실제 데이터
# - 빨간 선: 예측 직선
# - 초록 점선: 오차

plt.figure(figsize=(10, 6))

plt.scatter(X, y, color='blue', s=100, label='실제 데이터', zorder=3)
plt.plot(X, 예측점수, color='red', linewidth=2, label='예측 직선', zorder=2)

# 오차 표시
for i in range(len(X)):
    plt.plot([X[i], X[i]], [y[i], 예측점수[i]], 'g--', alpha=0.5, zorder=1)

plt.xlabel('공부 시간 (시간)', fontsize=12)
plt.ylabel('시험 점수 (점)', fontsize=12)
plt.title('선형 회귀: 공부 시간 vs 시험 점수', fontsize=14, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# ============================================================
# STEP 6: 실전 예제 - 광고비와 매출 예측
# ============================================================
# 상황: 온라인 쇼핑몰 운영자
# 질문: "광고비를 15백만원 쓰면 매출은?"

print("=" * 60)
print("STEP 6: 실전 예제 - 광고비로 매출 예측")
print("=" * 60)

# 과거 데이터
광고비 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)  # 백만원
매출 = np.array([3, 5, 6, 8, 11, 13, 14, 16, 17, 20])  # 천만원

# 모델 학습
model_광고 = LinearRegression()
model_광고.fit(광고비, 매출)

# 예측
새로운_광고비 = np.array([[15]])
예상_매출 = model_광고.predict(새로운_광고비)

print(f"\n[모델]")
print(f"  기울기: {model_광고.coef_[0]:.4f}")
print(f"  → 광고비 1백만원당 매출 {model_광고.coef_[0]:.2f}천만원 증가")
print(f"  절편: {model_광고.intercept_:.4f}")
# [모델]
#   기울기: 1.8606
#   → 광고비 1백만원당 매출 1.86천만원 증가
#   절편: 1.0667

print(f"\n[예측]")
print(f"  광고비 15백만원 → 예상 매출: {예상_매출[0]:.1f}천만원")
# [예측]
#   광고비 15백만원 → 예상 매출: 29.0천만원

# 정확도 측정 (R² Score)
# R² = 1에 가까울수록 정확
# R² = 모델이 데이터의 몇 %를 설명하는지
매출_예측 = model_광고.predict(광고비)
r2 = r2_score(매출, 매출_예측)

print(f"\n[정확도]")
print(f"  R² Score: {r2:.4f}")
print(f"  → 모델이 데이터의 {r2*100:.1f}%를 설명")
if r2 > 0.9:
    print(f"  → 매우 정확")
elif r2 > 0.7:
    print(f"  → 괜찮음")
else:
    print(f"  → 개선 필요")
# [정확도]
#   R² Score: 0.9913
#   → 모델이 데이터의 99.1%를 설명
#   → 매우 정확
