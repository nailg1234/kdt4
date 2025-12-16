from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd

data = {
    '나이': [25, 30, None, 40, 35],
    '연봉': [3000, 4500, 3500, None, 4000],
    '이탈': ['N', 'N', 'Y', 'N', 'Y']
}
df = pd.DataFrame(data)

# 결측치 확인
print(df.isnull().sum())
# 나이    1
# 연봉    1
# 이탈    0

# 결측치 처리
df['나이'].fillna(df['나이'].mean(), inplace=True)
# inplace=True // df 원본에 변경사항 바로 적용
df['연봉'].fillna(df['연봉'].mean(), inplace=True)

# 범주형 데이터 인코딩
df['이탈'] = df['이탈'].map({'N': 0, 'Y': 1})
print(df)
#      나이      연봉  이탈
# 0  25.0  3000.0   0
# 1  30.0  4500.0   0
# 2  32.5  3500.0   1
# 3  40.0  3750.0   0
# 4  35.0  4000.0   1


x = df[['나이', '연봉']]
y = df['이탈']

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

model = LogisticRegression()
model.fit(x_train, y_train)

predictions = model.predict(x_test)
probabilities = model.predict_proba(x_test)
print(f"예측 결과: {predictions}")  # [1]
print(f"예측 확률: {probabilities}")  # [[6.81415813e-10 9.99999999e-01]]

accuracy = accuracy_score(y_test, predictions)
print(f"정확도: {accuracy:.2f}")  # 정확도: 0.00

print(classification_report(y_test, predictions))
#               precision    recall  f1-score   support
#            0       0.00      0.00      0.00       1.0
#            1       0.00      0.00      0.00       0.0
#     accuracy                           0.00       1.0
#    macro avg       0.00      0.00      0.00       1.0
# weighted avg       0.00      0.00      0.00       1.0
