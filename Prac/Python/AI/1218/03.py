# 랜덤 포레스트와 앙상블
# 앙상블 
# 여러 모델을 결합하여 더 좋은 예측

# 세 사람의 지혜가 한사람 지혜보다 낫다

# 한 명의 전문가 < 여러 전문가의 의견 종합

# 왜 효과적인가?
# 개별 모델의 약점을 서로 보안 

# 모델A : 특정 데이터에서 실수
# 모델B : 다른 데이터에서 실수
# 모델C : 또 다른 데이터에서 실수

# 다수결 투표:
# -> 실수가 상쇄됨
# -> 전체적으로 더 정확

# 앙상블의 종류
# 배깅 (Begging)
# - Bootstrap Aggregating
# - 데이터를 다르게 샘플링
# - 예 : 랜덤 포레스트

# 부스팅 (Boosting)
# - 순차적으로 학습
# - 이전 모델의 실수를 보완
# - 예: XGBoost, AdeBoost

# 스태킹 (Stacking)
# - 다른 모델의 예측을 입력으로
# - 메타 모델이 최종 예측



# 배깅 (Begging)
# 원리
# 1. 부트스트램 샘플링
# - 원본 데이터에서 복원 추출
# - 같은 크기의 여러 샘플 생성

# 2. 각 샘플로 모델 학습
# - 독립적으로 N개 모델 생성

# 3. 예측 결합
# - 분류 : 다수결 투표
# - 회귀 : 평균

# 원본 데이터 : [1,2,3,4,5,6,7,8,9]

# 부트스트랩 샘플:
# 샘플 1: [1,1,3,4,5,6,6,7,9] -> 모델1
# 샘플 2: [1,2,2,4,6,6,6,7,9] -> 모델2
# 샘플 3: [1,3,3,4,5,6,8,8,9] -> 모델 3

# 예측 종합 (투표/평균)

# 최종 예측


# 랜덤 포레스트
# 랜덤 포레스트 = 배깅 + 결정 트리 + 특성 랜덤 선택

# "수많은 결정 트리의 숲"

# 특징:
# 여러 결정 트리를 학습
# 각 트리는 다른 데이터/특성 사용
# 트리들의 예측을 종합

# 랜덤성의 두가지 원천
# 1. 데이터 랜덤성 (Begging)
# - 부트스트랩 샘플링
# - 각 트리가 다른 데이터로 학습

# 2. 특성 랜덤성 (Random Subspace)
# - 각 분할에서 일부 특성만 고려
# - 보통  √(전체 특성 수) 개
# - 트리 간 다양성 증가


from sklearn.ensemble import RandomForestClassifier
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

model = RandomForestClassifier(
    n_estimators=100,    # 트리 개수 (많을수록 좋지만 느려짐)
    max_depth=5,         # 최대 깊이
    min_samples_split=2, # 분할 최소 샘플
    min_samples_leaf=1,  # 리프 최소 샘플
    max_features='sqrt', # 각 분할에서 고려할 특성 수 (sqrt: √특성수)
    bootstrap=True,      # 부트스트랩 샘플링 여부 (배깅 활성화)
    n_jobs=-1,           # 병렬 처리 (모든 CPU 사용)
    random_state=42
)

model.fit(X_train,y_train)

y_pred = model.predict(X_test)
print(f'정확도: {accuracy_score(y_test, y_pred):.2%}')

# 트리 개수의 영향 분석
# 트리가 많을수록 성능이 좋아지지만, 일정 개수 이상에서는 향상 폭이 작아짐
import matplotlib.pyplot as plt

# 한글 폰트 설정 추가
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows
# plt.rcParams['font.family'] = 'AppleGothic'  # Mac
plt.rcParams['axes.unicode_minus'] = False


n_trees = [1, 5, 10, 50, 100, 200]
scores = []

for n in n_trees:
    model = RandomForestClassifier(n_estimators=n, random_state=42)
    model.fit(X_train, y_train)
    scores.append(model.score(X_test, y_test))

print("\n트리 개수별 정확도:")
for n, score in zip(n_trees, scores):
    print(f"{n:3d}개: {score:.2%}")

plt.figure(figsize=(10, 6))
plt.plot(n_trees, scores, 'o-')
plt.xlabel('트리 개수')
plt.ylabel('정확도')
plt.title('트리 개수에 따른 성능')
plt.grid(True)
plt.show()

import pandas as pd

# 특성 중요도 분석
# 어떤 특성이 예측에 가장 큰 영향을 미치는지 확인
# 중요도가 높을수록 모델이 해당 특성을 더 많이 사용
importance = pd.DataFrame({
    '특성': iris.feature_names,
    '중요도': model.feature_importances_
}).sort_values('중요도', ascending=False)

print("\n특성 중요도:")
print(importance)
print(f"\n중요도 합계: {model.feature_importances_.sum():.2f} (항상 1.0)")

# 시각화
plt.figure(figsize=(10, 6))
plt.barh(importance['특성'], importance['중요도'])
plt.xlabel('중요도')
plt.title('랜덤 포레스트 특성 중요도')
plt.gca().invert_yaxis()
plt.show()


# 부스팅
# 순차적으로 학습, 실수 보완

# 1단계 : 모델1 학습 -> 일부 데이터 실수
# 2단계 : 모델2는 실수 데이터에 집중 학습
# 3단계 : 모델3은 남은 실수에 집중

# 실수한 데이터에 더 높은 가중치 부여

#                   배깅                    부스팅
# 학습 방식         병렬 (독립적)           순차 (의존적)
# 목표              분산 감소               편향 감소
# 과적합 방지       강함 (안정적)           상대적으로 약함 (튜닝 필요)
# 학습 속도         빠름 (병렬 가능)        느림 (순차적)
# 대표 알고리즘     랜덤포레스트            XGBoost, LightGBM, AdaBoost


# 분류 모델 정리 및 사용 시나리오

# 1. 로지스틱 회귀
# - 선형 결정 경계
# - 확률 출력 가능 (신뢰도 제공)
# - 해석 쉬움 (각 특성의 영향력 확인)
# 적합: 단순한 이진 분류, 해석이 중요한 경우

# 2. 결정 트리
# - 비선형 결정 경계
# - 시각화 가능 (의사결정 과정 확인)
# - 과적합 주의
# 적합: 빠른 프로토타입, 특성 선택이 필요한 경우

# 3. 랜덤 포레스트
# - 앙상블 (여러 트리)
# - 높은 정확도 (가장 범용적)
# - 특성 중요도 제공
# 적합: 대부분의 분류 문제, 높은 성능이 필요한 경우

# 4. SVM (Support Vector Machine)
# - 마진 최대화
# - 커널 트릭으로 비선형 가능
# - 고차원에 효과적
# 적합: 고차원 데이터, 명확한 분류 경계가 있는 경우

# 5. KNN (K-Nearest Neighbors)
# - 가장 가까운 K개 이웃으로 예측
# - 단순하지만 효과적
# - 스케일링 필요, 대용량 데이터에 느림
# 적합: 작은 데이터셋, 지역적 패턴이 중요한 경우


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


from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

# 데이터
iris = load_iris()
X, y = iris.data, iris.target

# 모델
model = LogisticRegression(max_iter=200)  # 수렴을 위해 반복 횟수 증가

# 5-Fold 교차 검증
# cv=5: 데이터를 5개로 나눔
# scoring='accuracy': 평가 지표 (정확도)
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')

print('\n=== 교차 검증 결과 ===')
print(f'각 Fold 점수: {scores}')
for i, score in enumerate(scores, 1):
    print(f'  Fold {i}: {score:.2%}')
print(f'\n평균 정확도: {scores.mean():.2%}')
print(f'표준편차: {scores.std():.2%}')
print(f'\n해석:')
print(f'- 평균 정확도가 높을수록 전반적인 성능이 좋음')
print(f'- 표준편차가 낮을수록 안정적인 모델 (데이터 분할에 덜 민감)')
