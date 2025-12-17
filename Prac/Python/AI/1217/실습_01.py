import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# 광고비(백만원)와 매출(천만원) 데이터
광고비 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
매출 = np.array([3, 5, 6, 8, 11, 13, 14, 16, 17, 20])

# 1. 선형 회귀 모델 학습
model = LinearRegression()
model.fit(광고비.reshape(-1, 1), 매출)
# 2. 기울기와 절편 확인
print(f'기울기: {model.coef_[0]}')
print(f'절편: {model.intercept_}')
print(f'예측식: 매출 = {model.coef_[0]:.4f} x 광고비 + {model.intercept_:.4f}')
# 3. 광고비 15백만원일 때 예상 매출 예측
광고비2 = np.array([[15]])
예상_매출 = model.predict(광고비2)
print(f'광고비 15백만원 => 예상 매출: {예상_매출}')
# 4. R² score 계산
y_pred = model.predict(광고비.reshape(-1, 1))
print(f'R²: {r2_score(매출, y_pred)}')
