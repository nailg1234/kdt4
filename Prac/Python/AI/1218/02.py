# 결정 트리
# 스무고개 게임!

# 이 과일 뭔지 맞추기
# Q1. 빨간색인가요?
# Yes -> Q2 작은가요?
            # -> Yes => 체리
            # -> No =>  사과

# No -> Q2 노란색인가요?

# 컴퓨터가 하는 일은 어떤 질문을 어떤 순서로 할지 데이터에서 자동으로 찾는것 

# 트리구조 용어
#            [루트 노드]        ← 맨 위, 첫 번째 질문
#           연소득 > 5000?
#            /         \
#          Yes          No
#          /             \
#     [내부 노드]      [내부 노드]   ← 중간 질문들
#     신용등급 > 3?    보증인 있음?
#       /    \          /    \
#     Yes    No       Yes    No
#      |      |        |      |
#   [리프]  [리프]   [리프]  [리프]  ← 최종 결정 (잎사귀)
#    승인    검토     승인    거절

#   깊이(Depth) 루트에서 리프까지 거치는 질문 수

# 좋은 질문 vs 나쁜 질문
# 핵심은 잘 나누는 질문을 찾는 것

# 데이터: 사과 10개, 오렌지 10개를 구분하고 싶음
# 나쁜 질문 : "무게가 100g" 이상인가?

# 좋은 질문 : :"빨간색이가?"

# 각 그룹이 순수 해지도록 나누기

# 순수도 

# 지니 불순도(Gini Impurity)
# Gini = 1 - (각 클래스 비율의 제곱의 합)
#      = 1 - Σ(pᵢ²)

# 직관적 의미:  랜덤을 뽑아서 랜덤으로 라벨 붙이면 틀릴 확률

# 예시 1 : 상자에 [사과 10개]만 있음
# - 사과 비율 = 10/10 = 1.0
# - Gini = 1 - (1.0²) = 1 - 1 = 0
# - 완전히 순수! ( 틀릴 일이 없음)

# 예시 2 : 상자에 [사과 5개 오렌지 5개]
# 사과 비율 = 0.5, 오렌지 비율 0.5
# - Gini = 1 - (0.5² + 0.5²) = 1 - 0.5 = 0.5
# 최대로 불순! (반반이라 가장 헷갈림)

# 예시 3 : 상자에 [사과 9개 오렌지 1개]
# 사과 비율 = 0.9, 오렌지 비율 0.1
# - Gini = 1 - (0.9² + 0.1²) = 1 - 0.82 = 0.18
# 꽤 순수함

# 이진 분류에서는 0.5
# 0 ~ 0.5 

# 다중 클래스 에서는
# 3개 0.66666
# 4개 0.75

# 엔트로피(Entropy)
# Entropy = -Σ(pᵢ × log₂(pᵢ))
# 직관적 의미: "얼마나 혼란스러운가?" (정보이론 개념)

# 예시 1: [사과 10개]
# Entropy = -(1.0 x log₂(1.0)) = 0
# 전혀 혼란스럽지 않음

# 예시 1: [사과 5개 오렌지 5개]
# Entropy = -(0.5 x log₂(0.5) = -0.5) X 2 = 1
# 최대로 혼란스러움

# 예시 1: [사과 9개 오렌지 1개]
# Entropy = 0.47
# 약간 혼란스러움

# 0 ~ 1까지 

from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 데이터 로드
iris = load_iris()
X, y = iris.data, iris.target

# 분할
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 모델 학습
model = DecisionTreeClassifier(
    criterion='gini', # 분할 기준 : 'gini' 또는 'entropy'                        
    max_depth=5, # 최대 깊이                     
    min_samples_split=10, # 분할을 위한 최소 샘플 수
    min_samples_leaf=5, # 리프 노드 최소 샘플 수
    max_features=None, # 분할에 사용할 특성 수
    random_state=42  
)
model.fit(X_train, y_train)

# 예측
y_pred = model.predict(X_test)
print(f'정확도: {accuracy_score(y_test, y_pred):.2%}')

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt


# 한글 폰트 설정 추가
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows
# plt.rcParams['font.family'] = 'AppleGothic'  # Mac
plt.rcParams['axes.unicode_minus'] = False


plt.figure(figsize=(20, 10))
plot_tree(model,
          feature_names=iris.feature_names,
          class_names=iris.target_names,
          filled=True,
          rounded=True,
          fontsize=10)
plt.title('붓꽃 분류 결정 트리')
plt.show()

# 텍스트로 출력
from sklearn.tree import export_text

tree_rules = export_text(model,
                         feature_names=list(iris.feature_names))
print(tree_rules)


import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# 1. 데이터 로드 (CSV 파일 경로)
# Titanic 데이터셋: 타이타닉호 승객 정보와 생존 여부
df = pd.read_csv('Titanic.csv')
print(df.head())  # 처음 5개 행만 출력
print(f'\n전체 데이터 크기: {df.shape}')

# 2. 필요한 특성만 선택 (dropna())
# 결측치(NaN)가 있는 행 제거
df = df[['Survived','Pclass','Sex','Age','SibSp','Parch','Fare']].dropna()
print(f'\n결측치 제거 후 데이터 크기: {df.shape}')

# Survived      생존 여부

# Pclass    객실 등급                   부유층일수록 생존율 높음
# Sex       성별                        여성 우선 구조
# Age       나이                        어린이 우선 구조
# SibSp     함께 탑승한 형제/배우자 수    가족 유무가 생존에 영향
# Parch     함께 탑승한 부모/자녀 수      가족 유무가 생존에 영향
# Fare      운임 요금                   부유층일수록 생존율 높음     

# Name      이름
# Ticket    티켓 번호
# Cabin     객실 번호           
# Embarked  탑승 항구

# 3. 성별을 숫자로 변환 (범주형 -> 숫자형)
# male: 0, female: 1로 인코딩
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# 4. 특성과 타겟 분리
# X: 예측에 사용할 특성들 (독립 변수)
X = df.drop(['Survived'], axis=1)
# y: 예측할 대상 (종속 변수 - 생존 여부)
y = df['Survived']

# 5. 훈련/테스트 데이터 분할 (80% 훈련, 20% 테스트)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 6. 모델 학습
# 기본 하이퍼파라미터로 결정 트리 생성
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# 7. 평가
y_pred = model.predict(X_test)
print(f"\n정확도: {accuracy_score(y_test, y_pred):.2%}")
print(f"올바르게 예측한 개수: {accuracy_score(y_test, y_pred, normalize=False)}/{len(y_test)}")

# 8. 시각화
plt.figure(figsize=(20, 12))
plot_tree(model,
          feature_names=X.columns,
          class_names=['사망','생존'],
          filled=True,
          rounded=True,
          fontsize=10)
plt.title('타이타닉 생존 예측 결정 트리')
plt.show()

# 트리 해석 방법:
# - 각 노드: 분할 조건 (예: Sex <= 0.5)
# - gini: 불순도 (0에 가까울수록 순수)
# - samples: 해당 노드의 샘플 수
# - value: [사망 수, 생존 수]
# - class: 다수 클래스 (사망 또는 생존)