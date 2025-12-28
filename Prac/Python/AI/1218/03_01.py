import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows
# plt.rcParams['font.family'] = 'AppleGothic'  # Mac
plt.rcParams['axes.unicode_minus'] = False

# 데이터 로드
iris = load_iris()
X, y = iris.data, iris.target

# 분할
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    min_samples_split=2,
    min_samples_leaf=1,
    max_features='sqrt',
    bootstrap=True,
    n_jobs=-1,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(f'정확도: {accuracy_score(y_test, y_pred):.2%}')
# 정확도: 100.00%


n_trees = [1, 5, 10, 50, 100, 200]
scores = []

for n in n_trees:
    model = RandomForestClassifier(n_estimators=n, random_state=42)
    model.fit(X_train, y_train)
    scores.append(model.score(X_test, y_test))

print("\n트리 개수별 정확도:")
for n, score in zip(n_trees, scores):
    print(f"{n:3d}개: {score:.2%}")
# 트리 개수별 정확도:
#   1개: 100.00%
#   5개: 96.67%
#  10개: 100.00%
#  50개: 100.00%
# 100개: 100.00%
# 200개: 100.00%


plt.figure(figsize=(10, 6))
plt.plot(n_trees, scores, 'o-')
plt.xlabel('트리 개수')
plt.ylabel('정확도')
plt.title('트리 개수에 따른 성능')
plt.grid(True)
plt.show()


importance = pd.DataFrame({
    '특성': iris.feature_names,
    '중요도': model.feature_importances_
}).sort_values('중요도', ascending=False)

print("\n특성 중요도:")
print(importance)
print(f"\n중요도 합계: {model.feature_importances_.sum():.2f} (항상 1.0)")
# 특성 중요도:
#                   특성       중요도
# 2  petal length (cm)  0.458036
# 3   petal width (cm)  0.408807
# 0  sepal length (cm)  0.101960
# 1   sepal width (cm)  0.031196

# 중요도 합계: 1.00 (항상 1.0)


plt.figure(figsize=(10, 6))
plt.barh(importance['특성'], importance['중요도'])
plt.xlabel('중요도')
plt.title('랜덤 포레스트 특성 중요도')
plt.gca().invert_yaxis()
plt.show()
