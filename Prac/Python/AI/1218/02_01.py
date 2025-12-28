from sklearn.tree import export_text
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 데이터 로드
iris = load_iris()
X, y = iris.data, iris.target

# 분할
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 모델 학습
model = DecisionTreeClassifier(
    criterion='gini',
    max_depth=5,
    min_samples_split=10,
    min_samples_leaf=5,
    max_features=None,
    random_state=42
)
model.fit(X_train, y_train)

# 예측
y_pred = model.predict(X_test)
print(f'정확도: {accuracy_score(y_test, y_pred):.2%}')
# 정확도: 100.00%

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(20, 10))
plot_tree(model,
          feature_names=iris.feature_names,
          class_names=iris.target_names,
          filled=True,
          rounded=True,
          fontsize=10)
plt.title('붓꽃 분류 결정 트리')
plt.show()

# 텍스트로 출력

tree_rules = export_text(model, feature_names=list(iris.feature_names))
print(tree_rules)
# |--- petal length (cm) <= 2.45
# |   |--- class: 0
# |--- petal length (cm) >  2.45
# |   |--- petal length (cm) <= 4.75
# |   |   |--- sepal length (cm) <= 5.15
# |   |   |   |--- class: 1
# |   |   |--- sepal length (cm) >  5.15
# |   |   |   |--- class: 1
# |   |--- petal length (cm) >  4.75
# |   |   |--- petal width (cm) <= 1.75
# |   |   |   |--- class: 1
# |   |   |--- petal width (cm) >  1.75
# |   |   |   |--- petal length (cm) <= 4.95
# |   |   |   |   |--- class: 2
# |   |   |   |--- petal length (cm) >  4.95
# |   |   |   |   |--- class: 2
