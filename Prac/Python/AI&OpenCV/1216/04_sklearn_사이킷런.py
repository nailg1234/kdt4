# Scikit-learn
# Python 머신러닝 라이브러리의 표준

# 특징
# 쉬운 API(fit, predict, transform)
# 다양한 알고리즘 제공
# 전처리, 평가 도구 포함
# 풍부한 문서와 예제
# 무료, 오픈소스


# 제공 기능
# 분류 (Classification)
# LogisticRegression, SVC, 등등

# 회귀 (Regression)
# LinearRegression, Ridge, 등등

# 군집화

# 차원 축소

# 전처리

# 모델 선택

# from sklearn.어디서든 import 모델

# # 1 모델 생성
# model = 모델(하이퍼파라미터)

# # 2. 학습
# model.fit(x_train, y_train)

# # 3. 예측
# predictions = model.predict(x_test)

# # 4. 평가
# score = model.score(x_test, y_test)

from sklearn.datasets import load_iris

iris = load_iris()
print(f"특성:", iris.feature_names)

print(f'타겟:', iris.target_names)

x = iris.data
y = iris.target

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

print(f'훈련: {x_train.shape} 테스트: {x_test.shape}')

from sklearn.neighbors import KNeighborsClassifier

# 1. 모델 생성 (k)
model = KNeighborsClassifier(n_neighbors=3)

# 2. 학습
model.fit(x_train, y_train)

# 3. 예측
y_pred = model.predict(x_test)
print('예측 결과: ',y_pred[:10])
print('실제 결과: ',y_test[:10])

# 모델 평가
from sklearn.metrics import accuracy_score, classification_report

# 정확도
accuracy = accuracy_score(y_test, y_pred)
print(f'정확도: {accuracy:.2%}')

# 간단히
print(f'정확도: {model.score(x_test, y_test):.2%}')

# 상세 리포트
print(classification_report(
    y_test, y_pred, 
    target_names=iris.target_names
    ))

from sklearn.linear_model import LogisticRegression

# model = LogisticRegression(max_iter=200)
# model.fit(x_train, y_train)
# print(f'로지스틱 회귀 정확도: {model.score(x_test, y_test):.2%}')


from sklearn.tree import DecisionTreeClassifier

# model = DecisionTreeClassifier()
# model.fit(x_train, y_train)
# print(f'결정 트리 정확도: {model.score(x_test, y_test):.2%}')


from sklearn.ensemble import RandomForestClassifier

# model = RandomForestClassifier()
# model.fit(x_train, y_train)
# print(f'랜덤 포레스트 정확도: {model.score(x_test, y_test):.2%}') 

models = {
    'Logistic':LogisticRegression(max_iter=200),
    'Dec':DecisionTreeClassifier(),
    "Random":RandomForestClassifier(),
}

for name, model in models.items():
    model.fit(x_train, y_train)
    print(f'{name} 정확도: {model.score(x_test, y_test):.2%}') 

# 데이터 전처리
# 스케일링의 중요성
# 특성별 스케일이 다르면 문제!!
print('원본 데이터 범위:')
print(f'특성1: {x[:,0].min():.1f} ~ {x[:,0].max():.1f}')
print(f'특성2: {x[:,1].min():.1f} ~ {x[:,1].max():.1f}')
# 범위가 다르면 일부 특성이 과도한 영향

from sklearn.preprocessing import StandardScaler

# 스케일러 생성 및 학습
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test) # fit은 하지 않음!

print('스케일링 후')
print(f'평균: {x_train_scaled.mean(axis=0)}')
print(f'표준편차: {x_train_scaled.std(axis=0)}')


from sklearn.svm import SVC
# 스케일링 없이

model = SVC()
model.fit(x_train, y_train)
print(f'스케일링 전: {model.score(x_test, y_test):.2%}') 


# 스케일링 후
model = SVC()
model.fit(x_train_scaled, y_train)
print(f'스케일링 후: {model.score(x_test_scaled, y_test):.2%}')

# 핵심 정리
# 1. Scikit-learn 기본 워크플로우:
#    - 모델 생성: model = Model(hyperparameters)
#    - 학습: model.fit(X_train, y_train)
#    - 예측: predictions = model.predict(X_test)
#    - 평가: score = model.score(X_test, y_test)
#
# 2. 제공되는 주요 기능:
#    - 분류: LogisticRegression, KNN, SVC, DecisionTree, RandomForest 등
#    - 회귀: LinearRegression, Ridge, Lasso 등
#    - 군집화: KMeans, DBSCAN 등
#    - 전처리: StandardScaler, MinMaxScaler 등
#    - 모델 선택: train_test_split, cross_validation 등
#
# 3. 데이터 전처리의 중요성:
#    - 특성 간 스케일이 다르면 모델 성능 저하
#    - StandardScaler: 평균 0, 표준편차 1로 정규화
#    - fit_transform(): 훈련 데이터에 적용
#    - transform(): 테스트 데이터에 적용 (fit 제외!)
#
# 4. 모델 비교:
#    - 여러 모델을 학습시켜 성능 비교
#    - 데이터 특성에 따라 최적 모델이 다름
#    - 항상 테스트 데이터로 평가
#
# 5. 평가 지표:
#    - accuracy_score: 전체 정확도
#    - classification_report: 클래스별 상세 성능
#    - precision, recall, f1-score 등 확인 가능

# ==================== 실습: Wine 데이터셋으로 모델 비교 ====================
# 여러 모델을 학습시켜 스케일링 전후 성능 비교

from sklearn.datasets import load_wine

# Wine 데이터셋 로드 (와인 품질 분류)
wine = load_wine()
x, y = wine.data, wine.target

# 데이터 분할
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, stratify=y, random_state=42
)

# 비교할 모델들
models = {
    "KNN": KNeighborsClassifier(n_neighbors=5),
    'Logistic': LogisticRegression(max_iter=100),
    'DecisionTree': DecisionTreeClassifier(random_state=42),
    'RandomForest': RandomForestClassifier(random_state=42),
    'SVC': SVC()
}

# 스케일링 전 성능
print('\n========== 스케일링 전 ==========')
for name, model in models.items():
    model.fit(x_train, y_train)
    print(f'{name:15s}: {model.score(x_test, y_test):.2%}')

# 데이터 스케일링
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# 스케일링 후 성능
print('\n========== 스케일링 후 ==========')
for name, model in models.items():
    model.fit(x_train_scaled, y_train)
    print(f'{name:15s}: {model.score(x_test_scaled, y_test):.2%}')

# 결과 분석:
# - KNN, SVC는 스케일링 후 성능이 크게 향상
# - DecisionTree, RandomForest는 스케일링 영향 거의 없음
# - Logistic Regression은 약간 향상