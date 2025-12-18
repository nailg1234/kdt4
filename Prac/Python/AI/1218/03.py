# 랜덤 포레스트
# 앙상블

# 배깅(Bagging)
# 원리
# 1. 부트스크랩 샘플링
# - 원본 데이터에서 복원 추출
# - 같은 크기의 여러 샘플 생성

# 2. 각 샘플로 모델 학습
# - 독립적으로 N개 모델 생성

# 3. 예측 결합
# - 분류: 다수결 투표
# - 회귀: 평균

# 원본 데이터: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 부트스크랩 샘플:
# 샘플1: [1, 1, 3, 4, 5, 6, 6, 7, 9] -> 모델1
# 샘플2: [1, 2, 2, 4, 6, 6, 6, 7, 9] -> 모델2
# 샘플3: [1, 3, 3, 4, 5, 6, 8, 8, 9] -> 모델3

# 예측 종합(투표/평균)

# 최종 예측


# 랜덤 포레스트
# 랜덤 포레스트 = 배깅 + 결정 트리 + 특성 랜덤 선택

# "수많은 결정 트리의 숲"
# 특징:
# 여러 결정 트리를 학습
# 각 트리는 다른 데이터/특성 사용
# 트리들의 예측을 종합

# 랜덤성의 두가지 원천
# 1. 데이터 랜덤성(Bagging)
# - 부트스트랩 샘플링
# - 각 트리가 다른 데이터로 학습

# 2. 특성 랜덤성(Random Subspace)
# - 각 분할에서 일부 특성만 고려
# - 보통 (전체 특성 수) 개
# - 트리 간 다양성 증가

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris, load_wine, load_digits
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 한글 폰트 설정 추가
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows
# plt.rcParams['font.family'] = 'AppleGothic'  # Mac
plt.rcParams['axes.unicode_minus'] = False

# 데이터 로드
iris = load_iris()
X, y = iris.data, iris.target

# 분할
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,       # 트리 개수(많을수록 좋지만 느려짐)
    max_depth=5,            # 최대 깊이
    min_samples_split=2,    # 분할 최소 샘플
    min_samples_leaf=1,     # 리프 최소 샘플
    max_features='sqrt',    # 각 분할에서 고려할 특성 수
    bootstrap=True,         # 부트스트랩 샘플링 여부
    n_jobs=-1,              # 병렬 처리(모든 CPU 사용)
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(f'정확도: {accuracy_score(y_test, y_pred)}')

# 트리개수의 영향
n_trees = [1, 5, 10, 50, 100, 200]
scores = []

for n in n_trees:
    model = RandomForestClassifier(n_estimators=n, random_state=42)
    model.fit(X_train, y_train)
    scores.append(model.score(X_test, y_test))

plt.figure(figsize=(10, 6))
plt.plot(n_trees, scores, 'o-')
plt.xlabel('트리 개수')
plt.ylabel('정확도')
plt.title('트리 개수에 따른 성능')
plt.grid(True)
plt.show()


# 특성 중요도
importance = pd.DataFrame({
    '특성': iris.feature_names,
    '중요도': model.feature_importances_
}).sort_values('중요도', ascending=False)

print(importance)

# 시각화
plt.figure(figsize=(10, 6))
plt.barh(importance['특성'], importance['중요도'])
plt.xlabel('중요도')
plt.title('랜덤 포레스트 특성 중요도')
plt.gca().invert_yaxis()
plt.show()

# 부스팅
# 순차적으로 학습, 실수 보완

# 1단계: 모델1 학습-> 일부 데이터 실수
# 2단계: 모델2는 실수 데이터에 집중 학습
# 3단계: 모델3은 남은 실수에 집중

# 실수한 데이터에 더 높은 가중치 부여

#               배깅                부스팅
# 학습 방식     병렬                순차
# 목표          분산 감소           편향 감소
# 과적합        강함                상대적으로 약함
# 대표 알고리즘 랜덤포레스트         XGBoost, LightGBM


# 분류 모델 정리
# 1. 로지스틱 회귀
# - 선형 결정 경계
# - 확률 출력 가능
# - 해석 쉬움

# 2. 결정 트리
# - 비선형 결정 경계
# - 시각화 가능
# - 과적합 주의

# 3. 랜덤 포레스트
# - 앙상블(여러 트리)
# - 높은 정확도
# - 특성 중요도 제공

# 4. SVM (Support Vector Machine)
# - 마진 최대화
# - 커널 트릭을 비선형 가능
# - 고차원에 효과적

# 5. KNN(K-Nearest Neighbors)
# - 가장 가까운 K개 이웃
# - 단순하지만 효과적
# - 스케일링 필요


# 교차 검증
# 단일 분할의 문제:
# - 우연히 좋은/나쁜 테스트 세트 가능
# - 결과의 신뢰성 낮음

# 교차 검증:
# - 여러 번 분할하여 평가
# - 평균 성능으로 신뢰성 증가

# K-Fold 교차 검증
# 데이터를 K개로 분할

# k = 5
# [1][2][3][4][5]

# 1회 = [1]테스트, [2,3,4,5] 훈련
# 2회 = [2]테스트, [1,3,4,5] 훈련
# 3회 = [3]테스트, [1,2,4,5] 훈련
# 4회 = [4]테스트, [1,2,3,5] 훈련
# 5회 = [5]테스트, [1,2,3,4] 훈련

# 최종 성능 = 5회 평균


# 데이터
iris = load_iris()
X, y = iris.data, iris.target

# 모델
model = LogisticRegression()

# 5-Fold 교차 검증
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')

print(f'각 Fold 점수: {scores}')
print(f'평균: {scores.mean():.2%}')
print(f'표준편차: {scores.std():.2%}')
