from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

# 3. 하이퍼파라미터 튜닝(Hyperparameter Tuning)
# 방법 1: 수동 설정
model1 = RandomForestClassifier(n_estimators=100)
model2 = RandomForestClassifier(n_estimators=200)
model3 = RandomForestClassifier(n_estimators=300)

# 방법 2: GridSearchCV (자동 탐색)
iris = load_iris()
X, y = iris.data, iris.target

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7],
    'min_samples_split': [2, 5]
}

model = RandomForestClassifier(random_state=42)

grid_search = GridSearchCV(
    model,
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)

grid_search.fit(X, y)

print(f'최적 파라미터: {grid_search.best_params_}')
print(f'최고 점수: {grid_search.best_score_:.2%}')
print(f'최적 모델: {grid_search.best_estimator_}')
# 최적 파라미터: {'max_depth': 3, 'min_samples_split': 2, 'n_estimators': 50}
# 최고 점수: 96.67%
# 최적 모델: RandomForestClassifier(max_depth=3, n_estimators=50, random_state=42)
