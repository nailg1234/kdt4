# 타이타닉 생존 예측
# 누가 생존했는가? 예측하는 분류 모델을 처음부터 끝까지 만들어보는 것

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows
# plt.rcParams['font.family'] = 'AppleGothic'  # Mac
plt.rcParams['axes.unicode_minus'] = False


# 데이터 로드
df = pd.read_csv('1219/Titanic1.csv')
print(df.head())
print(df.info())

# 1단계: 데이터 탐색(EDA)
# - 데이터 불러오기
# - 결측치가 어디에 얼마나 있는지 확인
# - 생존/사망 비율 파악
# - 성별, 객실 등급별 생존율 시각화
# - 특성 간 상관관계 히트맵 그리기

# 기본정보
print('=== 결측치 ===')
print(df.isnull().sum())

# 타겟 분포
print('=== 생존 분포 ===')
print(df['Survived'].value_counts())
print(df['Survived'].value_counts(normalize=True))

# 시각화
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 생존율
axes[0, 0].bar(['사망', '생존'], df['Survived'].value_counts().values)
axes[0, 0].set_title('전체 생존 분포')

# 성별에 따른 생존율
df.groupby('Sex')['Survived'].mean().plot(kind='bar', ax=axes[0, 1])
axes[0, 1].set_title('성별별 생존율')
axes[0, 1].set_ylabel('생존율')

# 객실 등급에 따른 생존율
df.groupby('Pclass')['Survived'].mean().plot(kind='bar', ax=axes[1, 0])
axes[1, 0].set_title('객실 등급별 생존율')
axes[1, 0].set_ylabel('생존율')

# 나이 분포
axes[1, 1].hist(df['Age'].dropna(), bins=20, edgecolor='black')
axes[1, 1].set_title('나이 분포')
axes[1, 1].set_xlabel('나이')

plt.tight_layout()
plt.show()

# 상관관계
numeric_cols = df.select_dtypes(include=[np.number]).columns
corr = df[numeric_cols].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, fmt='.2f')
plt.title('특성 간 상관관계')
plt.show()

# 2단계: 데이터 전처리
# - 필요한 특성만 선택
# - 결측치 채우기
# - 범주형 데이터를 숫자로 변환
# - 훈련/테스트 세트 분할

# 특성 선택
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
target = 'Survived'

# 데이터 복사
df_clean = df[features + [target]].copy()

# 결측치 처리
print('처리 전 결측치:')
print(df_clean.isnull().sum())

# Age: 중앙값으로 채우기 (이상치에 강함!)
df_clean['Age'].fillna(df_clean['Age'].median(), inplace=True)

df_clean['Fare'].fillna(df_clean['Fare'].median(), inplace=True)

df_clean['Embarked'].fillna(df_clean['Embarked'].mode()[0], inplace=True)

print('처리 후 결측치:')
print(df_clean.isnull().sum())

# 범주형 인코딩
# 성별 인코딩
df_clean['Sex'] = df_clean['Sex'].map({'male': 0, 'female': 1})

# 승선항 인코딩
le = LabelEncoder()
df_clean['Embarked'] = le.fit_transform(df_clean['Embarked'])

print(df_clean.head())

# 데이터 분할
X = df_clean.drop(target, axis=1)
y = df_clean[target]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3단계: 모델 학습 및 비교
# - 3가지 모델 훈련: 로지스틱 회귀, 결정 트리, 랜덤 포레스트
# - 교차 검증으로 성능 비교
# - GridSearchCV로 랜덤 포레스트 하이퍼파라미터 튜닝

# 스케일링
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 모델 정의
models = {
    'Logistic': LogisticRegression(max_iter=200),
    "Decision": DecisionTreeClassifier(max_depth=5, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42)
}

# 교차 검증 비교
results = []
for name, model in models.items():
    scores = cross_val_score(model, X_train_scaled, y_train, cv=5)
    results.append({
        '모델': name,
        "평균 정확도": scores.mean(),
        "표준편차": scores.std()
    })

results_df = pd.DataFrame(results)
print(results_df.sort_values('평균 정확도', ascending=False))

from sklearn.model_selection import GridSearchCV

# 랜덤 포레스트 튜닝
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7, 10],
    'min_samples_split': [2, 5, 10],
}

rf = RandomForestClassifier(random_state=42)
grid_search = GridSearchCV(rf, param_grid, cv=5, scoring='accuracy', n_jobs=-1)

grid_search.fit(X_train_scaled, y_train)

print(f'최적 파라미터: {grid_search.best_params_}')
print(f'최고 점수: {grid_search.best_score_:.2%}')


# 4단계: 평가
# - 테스트 세트로 최종 정확도 측정
# - 혼동 행렬로 어디서 틀렸는지 확인
# - 특성 중요도 확인 (어떤 특성이 생존 예측에 중요했나?)

# 혼동 행렬
# 분류 모델이 예측을 얼마나 맞췄는지를 '정답' vs '예측'을 교차표(행렬)로 정리한 표

best_model = grid_search.best_estimator_

# 예측
y_pred = best_model.predict(X_test_scaled)

# 평가
print('최종 평가')
print(f'정확도: {accuracy_score(y_test, y_pred):.2%}')
print('분류 리포트:')
print(classification_report(y_test, y_pred, target_names=['사망', '생존']))

# 혼동 행렬
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['사망 예측', '생존 예측'],
            yticklabels=['실제 사망', '실제 생존'])
plt.title('혼동 행렬')
plt.show()

# 특성 중요도
importance = pd.DataFrame({
    '특성': X.columns,
    '중요도': best_model.feature_importances_
}).sort_values('중요도', ascending=False)

print(importance)

# 시각화
plt.figure(figsize=(10, 6))
plt.barh(importance['특성'], importance['중요도'])
plt.xlabel('중요도')
plt.title('타이타닉 생존 예측 - 특성 중요도')
plt.gca().invert_yaxis()
plt.show()
