import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler

# ============================================================
# STEP 2: 간단한 예제 - 집값 예측
# ============================================================

print("=" * 60)
print("다중 선형 회귀 - 집값 예측")
print("=" * 60)

# 가상 데이터 생성
np.random.seed(42)
n_sample = 200

data = {
    '면적': np.random.randint(15, 50, n_sample),  # 15~50평
    '방수': np.random.randint(1, 5, n_sample),  # 1~4개
    '역거리': np.random.uniform(0.1, 2.0, n_sample),  # 0.1~2km
    '층수': np.random.randint(1, 25, n_sample),  # 1~24층
    '건축년도': np.random.randint(1990, 2023, n_sample)  # 1990~2022년
}

# 실제 관계 (모델이 찾아야 할 것!)
# 집값 = 0.15×면적 + 0.5×방수 - 0.3×역거리 + 0.02×층수 + 노이즈
집값 = (
    0.15 * data['면적'] +
    0.5 * data['방수'] -
    0.3 * data['역거리'] +
    0.02 * data['층수'] +
    2 +
    np.random.randn(n_sample) * 0.5
)

df = pd.DataFrame(data)
df['집값'] = 집값

print(f"\n[데이터] {len(df)}개")
print("\n처음 5개:")
print(df.head())
# [데이터] 200개

# 처음 5개:
#    면적  방수       역거리  층수  건축년도         집값
# 0  43   4  0.157950  12  2015  10.527675
# 1  29   2  0.170962  24  2003   8.092782
# 2  22   4  1.662941  21  1996   7.856180
# 3  35   1  0.784362   8  1992   7.265454
# 4  33   1  0.341415   4  2012   6.676193


# ============================================================
# STEP 3: 모델 학습
# ============================================================
# 핵심 단계:
# 1. 데이터 분리 (X, y)
# 2. 학습/테스트 분할
# 3. 모델 학습
# 4. 평가

# 특성(X)과 타겟(y) 분리
X = df[['면적', '방수', '역거리', '층수', '건축년도']]
y = df['집값']

# 학습/테스트 분할 (8:2)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\n[데이터 분할]")
print(f"  학습: {len(X_train)}개 (80%)")
print(f"  테스트: {len(X_test)}개 (20%)")
# [데이터 분할]
#   학습: 160개 (80%)
#   테스트: 40개 (20%)

# 모델 학습
model = LinearRegression()
model.fit(X_train, y_train)

# ============================================================
# STEP 4: 결과 확인
# ============================================================

print(f"\n[학습된 계수 - 각 변수의 영향력]")
print(f"{'특성':<10} {'계수':>10} {'의미'}")
print("-" * 60)
# [학습된 계수 - 각 변수의 영향력]
# 특성                 계수 의미
# ------------------------------------------------------------
# 면적             0.1536    1 증가 시 집값 +0.1536
# 방수             0.4828    1 증가 시 집값 +0.4828
# 역거리           -0.3192    1 증가 시 집값 -0.3192
# 층수             0.0148    1 증가 시 집값 +0.0148
# 건축년도           0.0076    1 증가 시 집값 +0.0076

for feature, coef in zip(X.columns, model.coef_):
    if coef > 0:
        meaning = f"1 증가 시 집값 +{abs(coef):.4f}"
    else:
        meaning = f"1 증가 시 집값 -{abs(coef):.4f}"
    print(f"{feature:<10} {coef:>10.4f}    {meaning}")

print(f"\n절편: {model.intercept_:.4f}")
# 절편: -13.2253

# ============================================================
# STEP 5: 모델 평가
# ============================================================

# 예측 및 평가
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"\n[성능]")
print(f"  R² Score: {r2:.4f}")
print(f"  → 데이터의 {r2*100:.1f}%를 설명")

if r2 > 0.9:
    print(f"  → 매우 우수")
elif r2 > 0.7:
    print(f"  → 괜찮음")
else:
    print(f"  → 개선 필요")

print(f"\n  RMSE: {rmse:.4f}")
# [성능]
#   R² Score: 0.8752
#   → 데이터의 87.5%를 설명
#   → 괜찮음
#
#   RMSE: 0.5589


# ============================================================
# STEP 6: 변수 중요도 분석
# ============================================================
# 계수의 절댓값 = 변수의 영향력

coef_df = pd.DataFrame({
    '특성': X.columns,
    '계수': model.coef_,
    '절댓값': np.abs(model.coef_)
})
coef_df = coef_df.sort_values("절댓값", ascending=False)

print(f"\n[변수 중요도 순위]")
print(coef_df[['특성', '계수']].to_string(index=False))

print(f"\n가장 중요한 변수: {coef_df.iloc[0]['특성']}")
print(f"영향력: {abs(coef_df.iloc[0]['계수']):.4f}")
# [변수 중요도 순위]
#   특성        계수
#   방수  0.482787
#  역거리 -0.319205
#   면적  0.153620
#   층수  0.014845
# 건축년도  0.007579

# 가장 중요한 변수: 방수
# 영향력: 0.4828


# ============================================================
# STEP 7: 새로운 집 가격 예측
# ============================================================

새로운집 = pd.DataFrame({
    '면적': [30],
    '방수': [3],
    '역거리': [0.5],
    '층수': [10],
    '건축년도': [2020]
})

예상가격 = model.predict(새로운집)

print(f"\n[예측]")
print(f"  면적 30평, 방 3개, 역 0.5km, 10층, 2020년")
print(f"  → 예상 집값: {예상가격[0]:.2f}")
# [예측]
#   면적 30평, 방 3개, 역 0.5km, 10층, 2020년
#   → 예상 집값: 8.13


# ============================================================
# STEP 8: 실전 데이터 - 캘리포니아 집값
# ============================================================

print("\n" + "=" * 60)
print("실전 데이터: 캘리포니아 집값")
print("=" * 60)

# 데이터 로드
housing = fetch_california_housing()
X_real = housing.data
y_real = housing.target
feature_names = housing.feature_names

print(f"\n[데이터셋]")
print(f"  샘플: {X_real.shape[0]:,}개")
print(f"  특성: {X_real.shape[1]}개")
print(f"  특성 목록: {', '.join(feature_names)}")
# [데이터셋]
#   샘플: 20,640개
#   특성: 8개
#   특성 목록: MedInc, HouseAge, AveRooms, AveBedrms,
#             Population, AveOccup, Latitude, Longitude

# 학습/테스트 분할
X_train_real, X_test_real, y_train_real, y_test_real = train_test_split(
    X_real, y_real, test_size=0.2, random_state=42
)

# 스케일링 (중요!)
# 왜? 변수들의 단위가 다르면 계수 해석이 어려움
# 예: MedInc(중위소득) ~ 15, AveRooms(평균방수) ~ 6
# → StandardScaler로 평균=0, 표준편차=1로 변환

print(f"\n[스케일링]")
print(f"  변수들의 단위가 다르면 계수 비교 어려움")
print(f"  → StandardScaler: 평균=0, 표준편차=1로 변환")
# [스케일링]
#   변수들의 단위가 다르면 계수 비교 어려움
#   → StandardScaler: 평균=0, 표준편차=1로 변환

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_real)
X_test_scaled = scaler.transform(X_test_real)

# 모델 학습
model_real = LinearRegression()
model_real.fit(X_train_scaled, y_train_real)

# 평가
y_pred_real = model_real.predict(X_test_scaled)
r2_real = r2_score(y_test_real, y_pred_real)
rmse_real = np.sqrt(mean_squared_error(y_test_real, y_pred_real))

print(f"\n[성능]")
print(f"  R²: {r2_real:.4f}")
print(f"  RMSE: {rmse_real:.4f}")
# [성능]
#   R²: 0.5758
#   RMSE: 0.7456

# 중요한 특성
coef_real_df = pd.DataFrame({
    '특성': feature_names,
    '계수': model_real.coef_,
    '절댓값': np.abs(model_real.coef_)
})
coef_real_df = coef_real_df.sort_values("절댓값", ascending=False)

print(f"\n[중요한 특성 Top 3]")
for i in range(3):
    feature = coef_real_df.iloc[i]['특성']
    coef = coef_real_df.iloc[i]['계수']
    print(f"  {i+1}. {feature} ({coef:.4f})")
# [중요한 특성 Top 3]
#   1. Latitude (-0.8969)
#   2. Longitude (-0.8698)
#   3. MedInc (0.8544)
