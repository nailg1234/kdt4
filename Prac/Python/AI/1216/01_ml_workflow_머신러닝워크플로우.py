# 머신러닝 프로젝트 전체 흐름

# 6단계 워크플로우

# 1. 문제 정의

# 핵심 질문
# "무엇을 예측할 것인가?"
# 이것은 분류 문제인가, 회귀 문제인가?
# 정답(라벨)이 있는가? (지도/비지도 학습)
# 성공의 기준은 무엇인가?

# 문제 유형 결정
# 예측 대상이 범주?
# ->분류 문제 (스팸/정상, 질병 유무)

# 예측 대상이 숫자?
# -> 회귀 문제(가격, 온도, 점수)

# 정답 데이터 없다?
# -> 비지도 학습 (군집화, 이상 탐지)


# 2. 데이터 수집
# "어떤 데이터가 필요한가?"

# 데이터 소스

# 내부 데이터:
# - 회사 데이터베이스
# - 로그 파일
# - 사용자 행동 기록

# 외부 데이터:
# - 공공 데이터 (data.go.kr)
# - Kaggle 데이터셋
# - API (날씨, 주식 등)

# 데이터 양과 질
# 데이터 양
# - 일반적으로 많을수록 좋음
# - 최소 수백~수천 개 필요
# - 딥러닝은 수만~수백만 개

# 데이터 질
# - 정확한 라벨링
# - 결측치 최소화
# - 대표성 (실제 상황 반영) 

# 3. 데이터 전처리
# "데이터를 정리하고 변환"

# 1. 결측치 처리
#  - 삭제: 데이터가 충분할 때
#  - 대체: 평균, 중앙값, 최빈값

# 2. 이상치 처리
# - 비정상적으로 큰/작은 값 처리
# - 입력 오류 수정

# 3. 데이터 변환
# - 스케일링: 값의 범위 통일
# - 인코딩: 문자 -> 숫자

# 4. 특성 선택/생성
# - 불필요한 특성 제거
# - 새로운 특성 만들기

import pandas as pd

# 샘플 데이터
data = {
    '나이': [25, 30, None, 40, 35],
    '연봉': [3000, 4500, 3500, None, 4000],
    '이탈': ['N', 'N', 'Y', 'N', 'Y']
}
df = pd.DataFrame(data)

# 결측치 확인
print(df.isnull().sum())

# 결측치 처리(평균으로 대체)
df['나이'].fillna(df['나이'].mean(), inplace=True)
df['연봉'].fillna(df['연봉'].mean(), inplace=True)

# 범주형 데이터 인코딩
df['이탈'] = df['이탈'].map({'N':0,'Y':1})

print(df)

# 4. 모델 선택 및 학습
# "어떤 알고리즘을 사용할 것인가?"

# 알고리즘 선택
# 분류 문제:
# - 로지스틱 회귀
# - 결정 트리
# - 랜덤 포레스트
# - SVM
# - 신경망

# 회귀 문제
# - 선형 회귀
# - 릿지/라쏘 회귀
# - 결정 트리 회귀
# - 신경망

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# 예시: 위에서 전처리한 데이터 사용
# 특성(X)과 라벨(y) 준비
X = df[['나이', '연봉']]  # 특성
y = df['이탈']  # 예측 대상

# 데이터 분할
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 모델 생성
model = LogisticRegression()

# 학습(fit)
model.fit(x_train, y_train)

# 예측(predict)
predictions = model.predict(x_test)

# 예측 확률도 확인 가능
probabilities = model.predict_proba(x_test)
print(f"예측 결과: {predictions}")
print(f"예측 확률: {probabilities}")

# 5. 모델 평가
# "성능이 충분한가?"
# 분류 평가 지표:
# - 정확도 (Accuracy)
# - 정밀도 (Precision)
# - 재현율 (Recall)
# - F1 Score

# 회귀 평가 지표:
# - MSE (평균 제곱 오차)
# - RMSE (평균 제곱근 오차)
# - MAE (평균 절대 오차)
# - R² (결정 계수)

# 모델 성능 평가 예시
from sklearn.metrics import accuracy_score, classification_report

# 정확도 계산
accuracy = accuracy_score(y_test, predictions)
print(f"정확도: {accuracy:.2f}")

# 상세 리포트
print(classification_report(y_test, predictions))

# 6. 모델 배포 및 모니터링
# "실제 서비스에 적용"

# 배포 방법:
# - API 서비스 (Flask, FastAPI)
# - 클라우드 서비스 (AWS, GCP, Azure)
# - 모바일/웹 앱 통합
# - 엣지 디바이스 (IoT, 모바일)

# 모니터링:
# - 성능 지속적 확인
# - 데이터 드리프트 감지 (입력 데이터 분포 변화)
# - 필요시 재학습 (주기적 또는 성능 저하 시)
# - A/B 테스트로 새 모델 검증

# 핵심 정리
# 1. 문제 정의: 명확한 목표와 성공 기준 설정
# 2. 데이터 수집: 양질의 충분한 데이터 확보
# 3. 데이터 전처리: 결측치, 이상치 처리 및 변환
# 4. 모델 선택 및 학습: 문제에 맞는 알고리즘 선택
# 5. 모델 평가: 적절한 평가 지표로 성능 측정
# 6. 배포 및 모니터링: 실서비스 적용 후 지속적 관리

# 전체 프로세스는 반복적!
# 평가 결과에 따라 이전 단계로 돌아가 개선
