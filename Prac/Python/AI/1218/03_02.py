from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

iris = load_iris()
X, y = iris.data, iris.target

model = LogisticRegression(max_iter=200)

scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')

print('\n=== 교차 검증 결과 ===')
print(f'각 Fold 점수: {scores}')
for i, score in enumerate(scores, 1):
    print(f'  Fold {i}: {score:.2%}')
print(f'\n평균 정확도: {scores.mean():.2%}')
print(f'표준편차: {scores.std():.2%}')
print('\n해석:')
print('- 평균 정확도가 높을수록 전반적인 성능이 좋음')
print('- 표준편차가 낮을수록 안정적')
# === 교차 검증 결과 ===
# 각 Fold 점수: [0.96666667 1.         0.93333333 0.96666667 1.        ]
#   Fold 1: 96.67%
#   Fold 2: 100.00%
#   Fold 3: 93.33%
#   Fold 4: 96.67%
#   Fold 5: 100.00%

# 평균 정확도: 97.33%
# 표준편차: 2.49%

# 해석:
# - 평균 정확도가 높을수록 전반적인 성능이 좋음
# - 표준편차가 낮을수록 안정적
