from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# 한글 폰트 설정 추가
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows
# plt.rcParams['font.family'] = 'AppleGothic'  # Mac
plt.rcParams['axes.unicode_minus'] = False

iris = load_iris()

x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# 모델 학습
model = DecisionTreeClassifier(
    random_state=42,
    criterion='gini',  # 분할 기준: 'gini' 또는 'entropy'
    max_depth=5,  # 최대 깊이
    min_samples_split=10,  # 분할을 위한 최소 샘플 수
    min_samples_leaf=5,  # 리프 노드 최소 샘플 수
    max_features=None,  # 분할에 사용할 특성 수
)

model.fit(x_train, y_train)

plt.figure(figsize=(20, 10))
plot_tree(model,
          feature_names=iris.feature_names,
          class_names=iris.target_names,
          filled=True,
          rounded=True,
          fontsize=10)
plt.title('붓꽃 분류 결정 트리')
plt.show()
