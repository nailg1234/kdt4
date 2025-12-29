from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.2,
    stratify=y,  # 클래스 비율 유지
    random_state=42  # 재현성 확보
)

print(f'x: {len(x)}')  # x: 150
print(f'x_train: {len(x_train)}')  # x_train: 120
print(f'x_test: {len(x_test)}')  # x_test: 30
print(f'y: {len(y)}')  # y: 150
print(f'y_train: {len(y_train)}')  # y_train: 120
print(f'y_test: {len(y_test)}')  # y_test: 30
