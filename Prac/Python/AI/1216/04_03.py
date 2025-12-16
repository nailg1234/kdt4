from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.2,
    stratify=y,  # 클래스 비율 유지
    random_state=42  # 재현성 확보
)

models = {
    'Logistic': LogisticRegression(max_iter=200),
    'DecisionTree': DecisionTreeClassifier(),
    'RandomForest': RandomForestClassifier(),
}

for name, model in models.items():
    model.fit(x_train, y_train)
    print(f'{name} 정확도: {model.score(x_test, y_test):.2%}')

# Logistic 정확도: 96.67%
# DecisionTree 정확도: 96.67%
# RandomForest 정확도: 96.67%
