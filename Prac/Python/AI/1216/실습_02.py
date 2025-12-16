from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

wine = load_wine()
x, y = wine.data, wine.target

x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.2,  # 테스트 비율
    stratify=y,  # 클래스 비율 유지!
    random_state=42  # 재현성을 위한 시도
)

models = {
    'rand': RandomForestRegressor(random_state=42),
    'log': LinearRegression(),
    'knn': KNeighborsClassifier(n_neighbors=3),
    'svc': SVC(random_state=42)
}

print('스케일 전')
for name, model in models.items():
    model.fit(x_train, y_train)
    print(f'{name}, {model.score(x_test, y_test):.2%}')

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)  # fit은 하지 않음!

print('스케일 후')
for name, model in models.items():
    model.fit(x_train_scaled, y_train)
    print(f'{name}, {model.score(x_test_scaled, y_test):.2%}')
