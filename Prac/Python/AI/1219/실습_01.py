import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# 한글 폰트 설정 추가
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows
# plt.rcParams['font.family'] = 'AppleGothic'  # Mac
plt.rcParams['axes.unicode_minus'] = False

# 누가 생존했는가? 예측하는 분류 모델을 처음부터 끝까지 만들어 보는 것

# 1단계: 데이터 탐색(EDA)
# 데이터 불러오기
df1 = pd.read_csv('Prac/Python/AI/1219/Titanic1.csv')
df2 = pd.read_csv('Prac/Python/AI/1219/Titanic2.csv')
df = pd.concat([df1, df2])

# 결측치가 어디에 얼마나 있는지 확인
print(df.isnull().sum())

# 생존/사망 비율 파악
df['Survived_KR'] = df['Survived'].map({0: '사망', 1: '생존'})
ratio = df['Survived_KR'].value_counts(normalize=True) * 100
print(ratio)
# 성별, 객실, 등급별 생존율 시각화
print(df.groupby('Sex')['Survived'].mean() * 100)
print(df.groupby('Pclass')['Survived'].mean() * 100)
# 특성 간 상관관계 히트맵 그리기
cols = ['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
corr = df[cols].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(
    corr,
    annot=True,        # 숫자 표시
    fmt='.2f',         # 소수점 2자리
    cmap='coolwarm',   # 색상
    vmin=-1, vmax=1,   # 상관계수 범위 고정
    square=True
)

plt.title('타이타닉 특성 간 상관관계 히트맵')
plt.show()

# 2단계: 데이터 전처리
# 필요한 특성만 선택
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
X = df[features]
y = df['Survived']

# 결측치 채우기
X['Age'] = X['Age'].fillna(X['Age'].median())
X['Fare'] = X['Fare'].fillna(X['Fare'].median())

# 범주형 데이터를 숫자로 변환
le = LabelEncoder()
X['Sex'] = le.fit_transform(X['Sex'])  # female=0, male=1

# 훈련/테스트 세트 분할
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3단계: 모델 학습 및 비교
# 3가지 모델 훈련: 로지스틱 회귀, 결정 트리, 랜덤 포레스트
models = {
    'LogistticRegression': LogisticRegression(max_iter=1000),
    'DecisionTree': DecisionTreeClassifier(random_state=42),
    'RandomForest': RandomForestClassifier(random_state=42)
}

# 교차 검증으로 성능 비교
for name, model in models.items():
    scores = cross_val_score(model, X_train, y_train, cv=5)
    print(f'{name} 평균 정확도: {scores.mean():.3f}')

# GridSearchCV로 랜덤 포레스트 하이퍼파라미터 튜닝
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 5, 10],
    'min_samples_split': [2, 5, 10]
}

grid = GridSearchCV(RandomForestClassifier(random_state=42),
                    param_grid, cv=5)

grid.fit(X_train, y_train)
print("최적 하이퍼파라미터:", grid.best_params_)

# 4단계: 평가
# 테스트 세트로 최종 정확도 측정
rf_best = grid.best_estimator_
y_pred = rf_best.predict(X_test)
print("테스트 세트 정확도:", accuracy_score(y_test, y_pred))
# 혼동 행렬이 어디서 틀렸는지 확인
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('예측값')
plt.ylabel('실제값')
plt.title('혼동 행렬')
plt.show()
# 특성 중요도 확인(어떤 특성이 생존 예측에 중요했나?)
importances = rf_best.feature_importances_
feature_importance = pd.Series(importances, index=X.columns)
feature_importance.sort_values(ascending=False).plot(kind='bar')
plt.title('랜덤 포레스트 특성 중요도')
plt.show()
