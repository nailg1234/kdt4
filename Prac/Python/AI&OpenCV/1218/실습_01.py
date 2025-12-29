from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# 1. 데이터 로드 (CSV 파일 경로)
df = pd.read_csv('Prac/Python/AI/1218/tested.csv')
print(df)


# 2. 필요한 특성만 선택 (dropna())
df = df[['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']].dropna()
# Survived  생존 여부

# Pclass    객실 등급                   부유층일수록 생존율 높음
# Sex       성별                        여성 우선 구조
# Age       나이                        어린이 우선 구조
# SibSp     함께 탑승한 형제/배우자 수    가족 유무가 생존에 영향
# Parch     함께 탑승한 부모/자녀 수      가족 유무가 생존에 영향
# Fare      운임 요금                    부유층일수록 생존율 높음

# Name      이름
# Ticket    티켓 번호
# Cabin     객실 번호
# Embarked  탑승 항구


# 3. 성별을 숫자로 변환
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})


# 4. 특성과 타켓 분리
x = df.drop(['Survived'], axis=1)
y = df['Survived']


# 5. 분할
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)


# 6. 모델 학습
model = DecisionTreeClassifier(random_state=42)
model.fit(x_train, y_train)


# 7.평가
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'정확도: {accuracy:}')


# 8. 시각화
plt.figure(figsize=(20, 10))
plot_tree(model,
          feature_names=x.columns,
          class_names=['Dead', 'Survived'],
          filled=True,
          rounded=True,
          fontsize=10)
plt.show()
