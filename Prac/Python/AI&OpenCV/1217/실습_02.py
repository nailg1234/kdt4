import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# 1. 데이터 준비
housing = fetch_california_housing()

x = housing.data
y = housing.target
feature_names = housing.feature_names
# print(feature_names)

# 2. 데이터 확인
df = pd.DataFrame(x, columns=feature_names)
df['Target'] = y

# print('데이터 크기:', x.shape)
# print(df.describe())

# 3. 학습/테스트 분할
x = df[feature_names]

# 데이터 분할
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# X. 스케일링
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# 4. 다중 선형 회귀 모델 학습
model = LinearRegression()
model.fit(x_train_scaled, y_train)

# 5. R² Score 확인
y_pred = model.predict(x_test_scaled)
# 평가 지표
r2 = r2_score(y_test, y_pred)
print(f'R² Score: {r2}')

# 6. 각 특성의 중요도 분석
# 결과 확인
print('=== 학습된 계수 ===')
for feature, coef in zip(x.columns, model.coef_):
    print(f'{feature}: {coef:.4f}')
print(f'절편: {model.intercept_}')
