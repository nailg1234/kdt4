# 다중 선형 회귀
# 단순 ㅅ너형 회귀
# y = wx + b
# - 입력(x)이 1개
# - 예: 면접 -> 집값


# 다중 선형 회귀
#
# - 입력(x)이 여러 개
# - 예: 면적, 방, 수, 역까지 거리 -> 집값

# 행렬 표현
# 벡터 표기:
# y = w*x + b w x+b

# 행렬 표기 (여러 데이터):
# Y = XW + b

from sklearn.datasets import fetch_california_housing
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# 집값 데이터 생성
np.random.seed(42)
n_sample = 200

data = {
    '면적': np.random.randint(15, 50, n_sample),
    '방수': np.random.randint(1, 5, n_sample),
    '역거리': np.random.randint(0.1, 2, n_sample),
    '층수': np.random.randint(1, 25, n_sample),
    '건축년도': np.random.randint(1990, 2023, n_sample)
}

# 실제 관계: 집값 = 0.15x면적 + 0.5x방수 - 0.3x역거리 + 0.02*층수+노이즈
집값 = (
    0.15 * data['면적'] +
    0.5 * data['방수'] -
    0.3 * data['역거리'] +
    0.02 * data['층수'] +
    2 + np.random.randn(n_sample) * 0.5
)

df = pd.DataFrame(data)
df['집값'] = 집값

print(df.head())
print(df.describe())

# 모델학습

# 특성과 타겟 분리
x = df[['면적', '방수', '역거리', '층수', '건축년도']]
y = df['집값']

# 데이터 분할
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# 모델 학습
model = LinearRegression()
model.fit(x_train, y_train)

# 결과 확인
print('=== 학습된 계수 ===')
for feature, coef in zip(x.columns, model.coef_):
    print(f'{feature}: {coef:.4f}')
print(f'절편: {model.intercept_}')

# 평가
# 예측
y_pred = model.predict(x_test)

# 평가 지표
r2 = r2_score(y_test, y_pred)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f'R² Score:{r2:.4f}')
print(f'RMSE Score:{rmse:.4f}억 원')

coef_df = pd.DataFrame({
    '특성': x.columns,
    '계수': model.coef_
})

coef_df = coef_df.sort_values("계수", key=abs, ascending=False)
print(coef_df)
