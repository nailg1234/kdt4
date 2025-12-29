from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

iris = load_iris()
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.2,
    stratify=y,  # 클래스 비율 유지
    random_state=42  # 재현성 확보
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(x_train)
X_test_scaled = scaler.transform(x_test)  # 테스트 데이터에는 fit 금지

# 스케일링 전
model = SVC()
model.fit(x_train, y_train)
print(model.score(x_test, y_test))  # 0.9666666666666667

# 스케일링 후
model = SVC()
model.fit(X_train_scaled, y_train)
print(model.score(X_test_scaled, y_test))  # 0.9666666666666667
