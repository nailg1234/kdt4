import pandas as pd

print(f"Pandas 버전: {pd.__version__}")
print("=" * 80)

# ============================================================================
# 데이터 분석 프로세스 개요
# ============================================================================
"""
데이터 분석의 6단계:
    1. 데이터 수집 (Data Collection)
       - 분석할 자료를 모으는 단계
       - 예: CSV 파일, 데이터베이스, API, 웹 스크래핑
    
    2. 데이터 정제 (Data Cleaning)
       - 분석 가능한 형태로 만드는 단계
       - 결측치 처리, 중복 제거, 데이터 타입 변환
    
    3. 데이터 탐색 (Data Exploration)
       - 데이터의 특성을 파악하는 단계
       - 기술 통계, 분포 확인, 패턴 탐색
    
    4. 데이터 분석 (Data Analysis)
       - 가설을 검증하고 패턴을 찾는 단계
       - 통계 분석, 머신러닝 모델 적용
    
    5. 시각화 (Visualization)
       - 결과를 이해하기 쉽게 표현하는 단계
       - 그래프, 차트, 대시보드
    
    6. 인사이트 도출 (Insight Generation)
       - 분석 결과를 의사결정에 활용하는 단계
       - 비즈니스 액션 아이템 도출

실무 예시 - 편의점 사장님의 고민:
    문제: 어떤 제품을 더 많이 주문해야 할까?
    데이터: 지난 3개월 판매 기록
    분석: 요일별, 시간대별 판매 패턴 파악
    인사이트: 금요일 저녁에 맥주가 가장 많이 팔린다
    행동: 금요일 전에 맥주 재고 확충
"""

# ============================================================================
# 1. Series 기본 개념
# ============================================================================
"""
Series란?
    - Pandas의 가장 기본이 되는 1차원 데이터 구조
    - Excel의 한 개 열(Column)이라고 생각하면 이해하기 쉬움
    
주요 특징:
    1. 1차원 배열: 데이터가 일렬로 나열
    2. 레이블(인덱스) 보유: 각 데이터에 이름표를 붙일 수 있음
    3. 동일 타입: 하나의 Series 안의 모든 데이터는 같은 타입
"""

# 가장 간단한 Series 생성
simple_series = pd.Series([10, 20, 30, 40, 50])
print("\n[1] 기본 Series")
print(simple_series)
print()

"""
Series의 3가지 핵심 구성요소:
    
    1. Value (값)
       - 실제 데이터가 저장되는 부분
       - Numpy 배열로 내부 저장됨
       - 빠른 수치 연산 가능
    
    2. Index (인덱스)
       - 각 값을 식별하는 레이블 (행 번호)
       - 기본값: 0, 1, 2, ... (정수)
       - 사용자 정의 가능 (문자열, 날짜 등)
       - 데이터 검색과 정렬의 기준
    
    3. Name (이름)
       - Series 전체를 설명하는 이름
       - 선택사항 (없어도 작동함)
       - DataFrame 결합 시 컬럼명으로 사용됨
"""

# 모든 구성요소를 포함한 Series
data_series = pd.Series(
    data=[10, 20, 30, 40, 50],                              # 값: 실제 저장된 데이터
    index=['Alice', 'Bob', 'Charlie', 'David', 'Eve'],      # 인덱스: 각 값의 레이블
    name='Test_Score'                                       # 이름: Series 전체의 이름
)

print("[2] 완전한 Series (값 + 인덱스 + 이름)")
print(data_series)
print()

# ============================================================================
# 2. Series 생성 방법
# ============================================================================
"""
pd.Series() 함수의 매개변수:
    
    pd.Series(data=None, index=None, dtype=None, name=None)
    
    - data: 실제 데이터 (필수)
            리스트, 딕셔너리, 스칼라값, Numpy 배열 가능
    
    - index: 인덱스 레이블 (선택)
             기본값은 0, 1, 2, ...
             리스트, 배열 등으로 사용자 지정 가능
    
    - dtype: 데이터 타입 (선택)
             자동 추론되지만 명시적으로 지정 가능
    
    - name: Series 이름 (선택)
            메타데이터로 활용
"""

# ============================================================================
# 3. 데이터 타입 (dtype)
# ============================================================================
"""
dtype이 중요한 이유:
    1. 메모리 사용량 결정
       - int8: 1바이트 (-128~127)
       - int64: 8바이트 (-9경~9경)
    
    2. 연산 가능 여부
       - 숫자 타입: 사칙연산 가능
       - 문자열 타입: 연결, 분할 가능
    
    3. 성능에 영향
       - 적절한 타입 선택으로 속도 향상
"""

# 정수형 Series
int_series = pd.Series([1, 2, 3, 4, 5])
print(f'[3-1] Integer Series dtype: {int_series.dtype}')
print(int_series)
print()

# 실수형 Series
float_series = pd.Series([1.1, 2.2, 3.3, 4.5, 5.6])
print(f'[3-2] Float Series dtype: {float_series.dtype}')
print(float_series)
print()

# 문자열 Series (object 타입으로 저장됨)
str_series = pd.Series(['Apple', 'Banana', 'Cherry'])
print(f'[3-3] String Series dtype: {str_series.dtype}')
print(str_series)
print()

# 불린형 Series
bool_series = pd.Series([True, False, True])
print(f'[3-4] Boolean Series dtype: {bool_series.dtype}')
print(bool_series)
print()

# 혼합형 Series (자동으로 float로 변환)
mixed_series = pd.Series([1, 2.5, 3])
print(f'[3-5] Mixed Series dtype: {mixed_series.dtype} (자동 변환)')
print(mixed_series)
print()

# ============================================================================
# 4. Series 생성 방법 (다양한 입력)
# ============================================================================

# 방법 1: 리스트로 생성
print("[4-1] 리스트로 Series 생성")
temp_list = [15.5, 17.2, 18.9, 19.1, 20.1]
temp = pd.Series(temp_list, name='4월_기온')
print(temp)
print()

# 방법 2: 날짜 인덱스를 가진 Series
print("[4-2] 날짜 인덱스를 가진 Series")
date = pd.date_range('2025-04-01', periods=5)  # 5일간의 날짜 생성
print("생성된 날짜 인덱스:")
print(date)
print()

temp_date = pd.Series(temp_list, index=date, name='4월_기온')
print("날짜 인덱스를 가진 기온 데이터:")
print(temp_date)
print()

# 방법 3: 딕셔너리로 생성 (키가 인덱스, 값이 데이터가 됨)
print("[4-3] 딕셔너리로 Series 생성")
product = {
    '노트북': 15,
    '마우스': 40,
    '키보드': 20
}
product_series = pd.Series(product, name='현재재고')
print(product_series)
print()

# 방법 4: 스칼라 값으로 생성 (모든 요소에 같은 값)
print("[4-4] 스칼라 값으로 Series 생성")
scalar_series = pd.Series(
    0,                          # 모든 요소를 0으로 초기화
    index=['월', '화', '수', '목'],
    name='판매량'
)
print(scalar_series)
print()

# ============================================================================
# 5. Series 속성 (Properties)
# ============================================================================
"""
Series의 주요 속성들:
    - values: 실제 데이터 (Numpy 배열)
    - index: 인덱스 정보
    - name: Series 이름
    - dtype: 데이터 타입
    - shape: 데이터 형태 (튜플)
    - size: 요소의 개수
    - ndim: 차원 (Series는 항상 1)
"""

test_scores = pd.Series(
    data=[85, 86, 59, 97, 65],
    index=['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    name='Exam'
)

print("=" * 80)
print("[5] Series 속성 전체")
print("=" * 80)

# 1. values - 실제 데이터 (Numpy 배열)
print('\n1. values (값들) - Numpy 배열 형태')
print(test_scores.values)
print(f"   타입: {type(test_scores.values)}")

# 2. index - 인덱스 정보
print('\n2. index (인덱스) - 각 데이터의 레이블')
print(test_scores.index)
print(f"   타입: {type(test_scores.index)}")

# 3. name - Series 이름
print('\n3. name (이름) - Series 전체의 이름')
print(test_scores.name)

# 4. dtype - 데이터 타입
print('\n4. dtype (타입) - 데이터의 자료형')
print(test_scores.dtype)

# 5. shape - 데이터 형태
print('\n5. shape (모양) - 데이터의 크기 (튜플)')
print(test_scores.shape)
print(f"   의미: {test_scores.shape[0]}개의 요소")

# 6. size - 요소 개수
print('\n6. size (크기) - 전체 요소의 개수')
print(test_scores.size)

# 7. ndim - 차원
print('\n7. ndim (차원) - 데이터의 차원')
print(test_scores.ndim)
print("   (Series는 항상 1차원)")
print()

# ============================================================================
# 6. 인덱싱 (Indexing) - 특정 데이터 선택
# ============================================================================
"""
인덱싱이란?
    - Series에서 특정 데이터를 선택하는 방법
    
두 가지 방식:
    1. 위치 기반 (Position-based): 0, 1, 2, ... (정수)
       - iloc[] 사용
       - 항상 0부터 시작하는 정수 인덱스
    
    2. 레이블 기반 (Label-based): 인덱스 이름으로 접근
       - loc[] 사용
       - 사용자가 지정한 인덱스 이름 사용
"""

sales = pd.Series(
    [100, 200, 150, 300],
    index=['Mon', 'Tue', 'Wed', 'Thu'],
    name="Daily_Sales"
)

print("=" * 80)
print("[6] 인덱싱 - 특정 데이터 선택")
print("=" * 80)
print("\n원본 데이터:")
print(sales)
print()

# 레이블 기반 인덱싱
print("[6-1] 레이블 기반 인덱싱")
wed_sales = sales['Wed']
print(f"sales['Wed'] = {wed_sales}")

wed_sales_loc = sales.loc['Wed']
print(f"sales.loc['Wed'] = {wed_sales_loc}")
print()

# 위치 기반 인덱싱
print("[6-2] 위치 기반 인덱싱 (0부터 시작)")
wed_sales_iloc = sales.iloc[2]  # 세 번째 요소 (0, 1, 2)
print(f"sales.iloc[2] = {wed_sales_iloc}")
print()

# 여러 개 선택
print("[6-3] 여러 개 선택 (리스트 사용)")
selected_days = sales[['Mon', 'Wed', 'Thu']]
print(selected_days)
print()

# ============================================================================
# 7. 슬라이싱 (Slicing) - 범위 선택
# ============================================================================
"""
슬라이싱이란?
    - 연속된 여러 개의 데이터를 선택하는 방법
    
주의사항:
    - loc[시작:끝]: 끝 포함 (inclusive)
    - iloc[시작:끝]: 끝 제외 (exclusive)
"""

print("=" * 80)
print("[7] 슬라이싱 - 범위 선택")
print("=" * 80)

print("\n[7-1] 레이블 기반 슬라이싱 (끝 포함)")
print("처음부터 수요일까지:")
print(sales.loc[:'Wed'])
print()

print("[7-2] 수요일부터 끝까지:")
print(sales.loc['Wed':])
print()

print("[7-3] 위치 기반 슬라이싱")
print("전체 선택:")
print(sales.iloc[:])
print()

print("[7-4] 역순으로 선택:")
print(sales.iloc[::-1])
print()

# ============================================================================
# 8. Boolean 인덱싱 - 조건으로 선택
# ============================================================================
"""
Boolean 인덱싱이란?
    - 조건을 만족하는 데이터만 선택하는 방법
    - SQL의 WHERE 절과 유사
    
작동 원리:
    1. 조건식을 작성 (예: sales >= 200)
    2. True/False로 구성된 Boolean Series 생성
    3. True인 위치의 값만 선택
"""

print("=" * 80)
print("[8] Boolean 인덱싱 - 조건으로 선택")
print("=" * 80)

sales = pd.Series(
    [100, 200, 150, 300],
    index=['Mon', 'Tue', 'Wed', 'Thu'],
    name="Daily_Sales"
)

print("\n원본 데이터:")
print(sales)
print()

# 조건 생성
print("[8-1] 조건 생성 (sales >= 200)")
condition = sales >= 200
print(condition)
print()

# 조건에 맞는 데이터 선택
print("[8-2] 조건에 맞는 데이터 선택")
result = sales[condition]
print(result)
print()

# ============================================================================
# 9. 비교 연산자
# ============================================================================
"""
비교 연산자:
    ==  : 같음
    !=  : 다름
    >   : 크다
    <   : 작다
    >=  : 크거나 같다
    <=  : 작거나 같다

논리 연산자:
    &   : AND (그리고)
    |   : OR (또는)
    ~   : NOT (부정)
    
주의: Python의 and, or가 아닌 &, | 사용
"""

print("=" * 80)
print("[9] 비교 연산자와 논리 연산자")
print("=" * 80)

print("\n[9-1] 같음 (==)")
print(sales[sales == 200])
print()

print("[9-2] AND 연산 (&) - 두 조건 모두 만족")
print("150 이상 350 이하:")
print(sales[(sales >= 150) & (sales <= 350)])
print()

print("[9-3] OR 연산 (|) - 둘 중 하나라도 만족")
print("150 미만 또는 300 이상:")
print(sales[(sales < 150) | (sales >= 300)])
print()

print("[9-4] 다름 (!=)")
print("200이 아닌 값:")
print(sales[sales != 200])
print()

# ============================================================================
# 10. 복합 조건
# ============================================================================
"""
복합 조건:
    - 여러 조건을 조합하여 사용
    - 괄호를 사용하여 우선순위 명확히 표시
"""

print("=" * 80)
print("[10] 복합 조건")
print("=" * 80)

sales = pd.Series(
    [100, 200, 150, 300, 250],
    index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    name="Daily_Sales"
)

print("\n원본 데이터:")
print(sales)
print()

# 예제 1: 평일 중 200 이상
print("[10-1] 평일 중 매출 200 이상")
weekday_high = sales[(sales >= 200) & (sales.index != 'Fri')]
print(weekday_high)
print()

# 예제 2: isin() 메서드 사용
print("[10-2] 특정 요일 또는 매출 200 미만")
weekend_or_low = sales[(sales < 200) | sales.index.isin(['Mon', 'Fri'])]
print(weekend_or_low)
print()

# ============================================================================
# 11. 벡터화 연산 (Vectorized Operations)
# ============================================================================
"""
벡터화 연산이란?
    - 반복문 없이 전체 데이터에 한 번에 연산 적용
    - Numpy 기반으로 매우 빠른 속도
    - 코드가 간결하고 읽기 쉬움

장점:
    1. 속도: 반복문보다 10~100배 빠름
    2. 간결성: 코드가 짧고 명확
    3. 가독성: 의도가 명확하게 드러남
"""

print("=" * 80)
print("[11] 벡터화 연산")
print("=" * 80)

prices = pd.Series(
    [3000, 1500, 4000, 2000],
    index=['apple', 'banana', 'orange', 'grape'],
    name='Price'
)

print("\n원본 가격:")
print(prices)
print()

print("[11-1] 덧셈: 모든 가격에 500원 추가")
print(prices + 500)
print()

print("[11-2] 뺄셈: 모든 가격에서 1000원 할인")
print(prices - 1000)
print()

print("[11-3] 곱셈: 20% 할인 (0.8 곱하기)")
print(prices * 0.8)
print()

print("[11-4] 나눗셈: 반값")
print(prices / 2)
print()

# ============================================================================
# 12. Series 간 연산
# ============================================================================
"""
Series 간 연산:
    - 같은 인덱스끼리 자동으로 매칭되어 연산
    - 인덱스가 다르면 NaN (Not a Number) 반환
    
정렬 방식:
    - 인덱스를 기준으로 자동 정렬 (Alignment)
    - SQL의 JOIN과 유사한 개념
"""

print("=" * 80)
print("[12] Series 간 연산")
print("=" * 80)

store_a = pd.Series(
    [1000, 2000, 1500, 2000],
    index=['Apple', 'Pear', 'Orange', 'Banana'],
    name='Store_A'
)

store_b = pd.Series(
    [900, 2200, 1400, 2500],
    index=['Apple', 'Pear', 'Orange', 'Grape'],  # Grape만 다름
    name='Store_B'
)

print("\nStore A 가격:")
print(store_a)
print()

print("Store B 가격:")
print(store_b)
print()

print("[12-1] 두 매장 가격 합계")
print(store_a + store_b)
print("주의: Banana와 Grape는 한쪽에만 있어서 NaN")
print()

print("[12-2] 가격 차이 (A - B)")
price_diff = store_a - store_b
print(price_diff)
print()

# ============================================================================
# 13. NaN (결측값) 처리하며 연산하기
# ============================================================================
"""
NaN (Not a Number) 처리 방법:
    
    1. fill_value 사용
       - 없는 값을 특정 값으로 채워서 연산
    
    2. reindex() 사용
       - 인덱스를 미리 맞춘 후 연산
    
    3. dropna() 사용
       - 결측값을 제거한 후 연산
"""

print("=" * 80)
print("[13] NaN (결측값) 처리")
print("=" * 80)

# 방법 1: fill_value 사용
print("\n[13-1] fill_value로 없는 값을 0으로 채워서 연산")
price_diff_filled = store_b.sub(store_a, fill_value=0)
print(price_diff_filled)
print("설명: Grape는 2500 - 0으로 계산됨")
print()

# 방법 2: reindex로 먼저 맞추기
print("[13-2] reindex로 인덱스를 먼저 맞추기")
store_a_reindexed = store_a.reindex(store_b.index, fill_value=0)
print("인덱스를 맞춘 Store A:")
print(store_a_reindexed)
print()

price_diff_reindexed = store_b - store_a_reindexed
print("재계산된 가격 차이:")
print(price_diff_reindexed)
print()

# 방법 3: dropna로 결측값 제거
print("[13-3] dropna()로 NaN 제거")
price_diff_cleaned = price_diff.dropna()
print(price_diff_cleaned)
print("설명: NaN이 있던 Banana와 Grape가 제거됨")
print()

# ============================================================================
# 14. 비교 연산과 조건부 선택
# ============================================================================
"""
where() 메서드:
    - 조건에 따라 값을 선택적으로 유지하거나 대체
    - Series.where(조건, 대체값)
    - 조건이 True인 값만 유지, False는 대체값으로
"""

print("=" * 80)
print("[14] 비교 연산과 조건부 선택")
print("=" * 80)

store_a = pd.Series(
    [1000, 2000, 1500],
    index=['Apple', 'Pear', 'Orange'],
    name='Store_A'
)

store_b = pd.Series(
    [900, 2200, 1400],
    index=['Apple', 'Pear', 'Orange'],
    name='Store_B'
)

print("\nStore A 가격:")
print(store_a)
print()

print("Store B 가격:")
print(store_b)
print()

# Store A가 더 비싼 경우 찾기
print("[14-1] B상점이 더 저렴한 제품 찾기")
is_b_cheaper = store_a > store_b
print(is_b_cheaper)
print()

# 더 저렴한 매장의 가격만 선택
print("[14-2] 각 제품별 최저가 선택")
best_prices = store_a.where(is_b_cheaper, store_b)
print(best_prices)
print("설명:")
print("  - Apple: B가 더 저렴 (900 < 1000)")
print("  - Pear: A가 더 저렴 (2000 < 2200)")
print("  - Orange: B가 더 저렴 (1400 < 1500)")
print()

print("=" * 80)
print("Pandas Series 학습 완료!")
print("=" * 80)
