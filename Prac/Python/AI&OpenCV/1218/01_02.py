import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

np.random.seed(42)

X = np.random.randn(200, 2)
y = (X[:, 0] + X[:, 1] > 0).astype(int)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(f'정확도: {accuracy_score(y_test, y_pred):.2%}')
print(classification_report(y_test, y_pred))
# 정확도: 100.00%
#               precision    recall  f1-score   support

#            0       1.00      1.00      1.00        21
#            1       1.00      1.00      1.00        19

#     accuracy                           1.00        40
#    macro avg       1.00      1.00      1.00        40
# weighted avg       1.00      1.00      1.00        40


# 확률 예측
# predict_proba()는 각 클래스에 속할 확률을 반환
# 결과: [[클래스0 확률, 클래스1 확률], ...]
proba = model.predict_proba(X_test)
print('확률 예측 (처음 5개)')
print(proba[:5])
print('각 행: [클래스0 확률, 클래스1 확률]')
print('예: [0.8, 0.2] -> 80% 확률로 클래스0, 20% 확률로 클래스1')
# 확률 예측 (처음 5개)
# [[0.25677411 0.74322589]
#  [0.02579772 0.97420228]
#  [0.90825124 0.09174876]
#  [0.21514593 0.78485407]
#  [0.11309306 0.88690694]]
# 각 행: [클래스0 확률, 클래스1 확률]
# 예: [0.8, 0.2] -> 80% 확률로 클래스0, 20% 확률로 클래스1
