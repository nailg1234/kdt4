import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows
# plt.rcParams['font.family'] = 'AppleGothic'  # Mac
plt.rcParams['axes.unicode_minus'] = False

# 1. 데이터 로드
df = pd.read_csv('Prac/Python/AI/1218/Titanic.csv')
print(df.head())
#    PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
# 0          892         0       3  ...   7.8292   NaN         Q
# 1          893         1       3  ...   7.0000   NaN         S
# 2          894         0       2  ...   9.6875   NaN         Q
# 3          895         0       3  ...   8.6625   NaN         S
# 4          896         1       3  ...  12.2875   NaN         S
# [5 rows x 12 columns]

print(f'\n전체 데이터 크기: {df.shape}')
# 전체 데이터 크기: (418, 12)

# 2. 필요한 컬럼만 선택 + 결측치 제거
df = df[['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']].dropna()
print(f'\n결측치 제거 후 데이터 크기: {df.shape}')
# 결측치 제거 후 데이터 크기: (331, 7)

# 3. 성별 숫자 변환
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# 4. 특성과 타깃 분리
X = df.drop(['Survived'], axis=1)
y = df['Survived']

# 5. 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 6. 모델 학습
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# 7. 평가
y_pred = model.predict(X_test)
print(f"\n정확도: {accuracy_score(y_test, y_pred):.2%}")
# 정확도: 100.00%

print(
    f"올바르게 예측한 개수: {accuracy_score(y_test, y_pred, normalize=False)}/{len(y_test)}")
# 올바르게 예측한 개수: 67.0/67

# 8. 시각화
plt.figure(figsize=(20, 12))
plot_tree(model,
          feature_names=X.columns,
          class_names=['사망', '생존'],
          filled=True,
          rounded=True,
          fontsize=10)
plt.title('타이타닉 생존 예측 결정 트리')
plt.show()
