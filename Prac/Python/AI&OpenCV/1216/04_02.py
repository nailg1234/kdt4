from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.2,
    stratify=y,  # 클래스 비율 유지
    random_state=42  # 재현성 확보
)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print(f'정확도: {accuracy:.2%}')  # 정확도: 100.00%
print(classification_report(
    y_test, y_pred,
    target_names=iris.target_names
))

#               precision    recall  f1-score   support
#       setosa       1.00      1.00      1.00        10
#   versicolor       1.00      1.00      1.00        10
#    virginica       1.00      1.00      1.00        10
#     accuracy                           1.00        30
#    macro avg       1.00      1.00      1.00        30
# weighted avg       1.00      1.00      1.00        30
