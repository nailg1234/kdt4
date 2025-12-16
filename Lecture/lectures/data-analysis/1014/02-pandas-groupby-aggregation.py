import pandas as pd
import numpy as np

# ═══════════════════════════════════════════════════════════════
# 그룹화와 집계 (Grouping and Aggregation)
# ═══════════════════════════════════════════════════════════════
# 데이터를 특정 기준으로 묶어서 분석하는 핵심 기법입니다.
# SQL의 GROUP BY와 유사하며, 데이터 분석의 필수 도구입니다.

# ─────────────────────────────────────────────────────────────
# 1. GroupBy의 필요성
# ─────────────────────────────────────────────────────────────

'''
    그룹화가 필요한 이유:
    
    ❌ 전체 평균만으로는 부족한 경우가 많음
       예: 전체 평균 연봉 5,000만원
       → 하지만 부서별로는 큰 차이가 있을 수 있음
    
    ✅ 그룹화를 통해 얻는 인사이트:
       - 카테고리별 패턴 발견 (부서별, 지역별, 시간별)
       - 세그먼트별 비교 분석
       - 숨겨진 트렌드 파악
       
    실무 예시:
    - 부서별 평균 연봉 비교
    - 월별 매출 추이 분석
    - 지역별 고객 수 집계
    - 제품 카테고리별 판매량
'''

# 직원 데이터 예시
employee_data = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry'],
    'department': ['Dev', 'Dev', 'Sales', 'Sales', 'Dev', 'HR', 'HR', 'Sales'],
    'years': [3, 5, 2, 7, 10, 4, 6, 3],  # 근속연수
    'salary': [4500, 5500, 4000, 6500, 8000, 4800, 5800, 4200]  # 연봉(만원)
})

print('전체 직원 데이터')
print(employee_data)
print()

# ─────────────────────────────────────────────────────────────
# 2. 전체 분석 vs 그룹별 분석 비교
# ─────────────────────────────────────────────────────────────

# 전체 평균 - 모든 직원의 평균 연봉
print('전체 분석')
overall_avg = employee_data['salary'].mean()
print(f'전체 평균 연봉: {overall_avg:.2f}만원')
# 결과: 5,412.5만원 → 부서별 차이가 보이지 않음!
print()

# 그룹별 평균 - 부서별로 나누어 분석
print('그룹별 분석')
dept_avg = employee_data.groupby('department')['salary'].mean()
print(dept_avg)
# 결과:
# Dev      6000.0  (개발팀이 가장 높음)
# HR       5300.0
# Sales    4900.0  (영업팀이 가장 낮음)
# → 부서별 연봉 격차가 명확하게 드러남!
print()

# ═══════════════════════════════════════════════════════════════
# GroupBy의 핵심 개념: Split-Apply-Combine
# ═══════════════════════════════════════════════════════════════

'''
    GroupBy의 3단계 프로세스:
    
    1. Split (분할)
       - 데이터를 그룹으로 나누기
       - 예: 부서별로 직원 데이터 분리
    
    2. Apply (적용)
       - 각 그룹에 독립적으로 함수 적용
       - 예: 각 부서의 평균 연봉 계산
    
    3. Combine (결합)
       - 결과를 하나의 DataFrame/Series로 합치기
       - 예: 부서별 평균을 하나의 테이블로 정리
    
    시각적 표현:
    ┌─────────────────┐
    │  전체 데이터     │
    └────────┬────────┘
             │ Split
    ┌────────┴────────┐
    │ Dev │ HR │Sales │ ← 그룹별로 분할
    └────┬───┬───┬────┘
         │   │   │ Apply (각 그룹에 함수 적용)
    ┌────┴───┴───┴────┐
    │   결과 테이블     │ ← Combine
    └─────────────────┘
'''

print('=== Split - Apply - Combine 단계별 확인 ===')
simple_data = pd.DataFrame({
    'category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'value': [10, 20, 15, 25, 12, 22]
})
print('원본 데이터')
print(simple_data)
print()

# ─────────────────────────────────────────────────────────────
# 1단계: Split (분할) - 데이터를 그룹으로 나누기
# ─────────────────────────────────────────────────────────────
print('【1단계: Split】')
for category, group in simple_data.groupby('category'):
    print(f'\n{category} 그룹:')
    print(group)
# A 그룹: 0, 2, 4번 행 (value: 10, 15, 12)
# B 그룹: 1, 3, 5번 행 (value: 20, 25, 22)
print()

# ─────────────────────────────────────────────────────────────
# 2단계: Apply (적용) - 각 그룹에 함수 적용
# ─────────────────────────────────────────────────────────────
print('【2단계: Apply】')
for category, group in simple_data.groupby('category'):
    avg = group['value'].mean()
    print(f'{category} 그룹 평균: {avg}')
# A 그룹 평균: (10+15+12) / 3 = 12.33
# B 그룹 평균: (20+25+22) / 3 = 22.33
print()

# ─────────────────────────────────────────────────────────────
# 3단계: Combine (결합) - 결과를 하나로 합치기
# ─────────────────────────────────────────────────────────────
print('【3단계: Combine】')
result = simple_data.groupby('category')['value'].mean()
print(result)
# category
# A    12.333333
# B    22.333333
# Name: value, dtype: float64
print()

# ═══════════════════════════════════════════════════════════════
# groupby() 메서드의 주요 매개변수
# ═══════════════════════════════════════════════════════════════

'''
    groupby() 함수 시그니처:
    groupby(by=None, axis=0, level=None, as_index=True, sort=True, ...)
    
    주요 매개변수:
    - by: 그룹화 기준 (컬럼명 또는 컬럼명 리스트)
    - as_index: 그룹 키를 인덱스로 설정할지 여부 (기본=True)
    - sort: 그룹 키를 정렬할지 여부 (기본=True)
    - axis: 0=행, 1=열 기준 그룹화 (거의 항상 0 사용)
'''

# ─────────────────────────────────────────────────────────────
# 3. groupby() 사용법 - 컬럼 선택 방법
# ─────────────────────────────────────────────────────────────

employee_data = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry'],
    'department': ['Dev', 'Dev', 'Sales', 'Sales', 'Dev', 'HR', 'HR', 'Sales'],
    'years': [3, 5, 2, 7, 10, 4, 6, 3],
    'salary': [4500, 5500, 4000, 6500, 8000, 4800, 5800, 4200]
})

print('=== 컬럼 선택 방법 ===')

# 방법 1 - 대괄호 접근 (권장)
result1 = employee_data.groupby('department')['salary'].mean()
print('방법 1: groupby("부서")["연봉"]')
print(result1)
print()

# 방법 2 - 점(.) 접근 (간결하지만 컬럼명에 공백 있으면 사용 불가)
result2 = employee_data.groupby('department').salary.mean()
print('방법 2: groupby("부서").salary')
print(result2)
print()

# 방법 3 - 여러 컬럼 선택 (이중 대괄호 사용)
result3 = employee_data.groupby('department')[['salary', 'years']].mean()
print('방법 3: 여러 컬럼 선택')
print(result3)
# 결과: salary와 years 모두 평균 계산
print()

# ─────────────────────────────────────────────────────────────
# 4. as_index 매개변수 - 인덱스 설정 제어
# ─────────────────────────────────────────────────────────────

print('=== as_index 매개변수 ===')

# as_index=True (기본값) - 그룹 키가 인덱스로 설정됨
result_indexed = employee_data.groupby(
    'department', as_index=True)['salary'].mean()
print('as_index=True (기본값):')
print(result_indexed)
print(f'타입: {type(result_indexed)}')  # Series
print(f'인덱스: {result_indexed.index.tolist()}')  # ['Dev', 'HR', 'Sales']
# 장점: 인덱싱으로 빠른 접근 가능 (result_indexed['Dev'])
# 단점: DataFrame으로 변환 필요한 경우 불편
print()

# as_index=False - 그룹 키가 일반 컬럼으로 유지됨
result_no_indexed = employee_data.groupby(
    'department', as_index=False)['salary'].mean()
print('as_index=False:')
print(result_no_indexed)
print(f'타입: {type(result_no_indexed)}')  # DataFrame
# 장점: 바로 DataFrame 형태, 추가 처리 용이
# 단점: 인덱스 접근 불가
print()

'''
    as_index 선택 가이드:
    - True: 빠른 조회, 시각화에 적합
    - False: 추가 분석, 병합(merge) 작업에 적합
'''

# ─────────────────────────────────────────────────────────────
# 5. sort 매개변수 - 정렬 제어
# ─────────────────────────────────────────────────────────────

print('=== sort 매개변수 ===')

# sort=True (기본값) - 그룹 키를 알파벳/숫자 순으로 정렬
result_sorted = employee_data.groupby(
    'department', sort=True)['salary'].mean()
print('sort=True (기본값):')
print(result_sorted)
# 결과: Dev, HR, Sales 순서 (알파벳순)
print()

# sort=False - 데이터 등장 순서대로 유지
result_no_sorted = employee_data.groupby(
    'department', sort=False)['salary'].mean()
print('sort=False:')
print(result_no_sorted)
# 결과: Dev, Sales, HR 순서 (데이터에 나타난 순서)
# 장점: 대용량 데이터에서 정렬 비용 절약 (속도 향상)
print()

# ═══════════════════════════════════════════════════════════════
# 6. 집계 함수 (Aggregation Functions)
# ═══════════════════════════════════════════════════════════════

'''
    주요 집계 함수:
    
    기본 통계:
    - count()   : 개수 (결측값 제외)
    - sum()     : 합계
    - mean()    : 평균
    - median()  : 중앙값 (중간값)
    - min()     : 최솟값
    - max()     : 최댓값
    
    분산 관련:
    - var()     : 분산 (데이터의 퍼진 정도²)
    - std()     : 표준편차 (데이터의 퍼진 정도)
    
    기타:
    - first()   : 첫 번째 값
    - last()    : 마지막 값
    - size()    : 그룹 크기 (결측값 포함)
'''

print('=== 집계 함수 예시 ===')
print(f"count: {employee_data.groupby('department')['salary'].count()}")
print(f"sum: {employee_data.groupby('department')['salary'].sum()}")
print(f"min: {employee_data.groupby('department')['salary'].min()}")
print(f"max: {employee_data.groupby('department')['salary'].max()}")
print()

# ─────────────────────────────────────────────────────────────
# 7. describe() - 종합 통계 한 번에 확인
# ─────────────────────────────────────────────────────────────

# describe(): 여러 통계를 한 번에 계산하는 편리한 메서드
result = employee_data.groupby('department')['salary'].describe()
print('=== describe() 종합 통계 ===')
print(result)
# 결과: count, mean, std, min, 25%, 50%, 75%, max 모두 출력
# 데이터 분포를 한눈에 파악 가능!
print()

# ═══════════════════════════════════════════════════════════════
# 8. 다중 그룹화 (Multiple Grouping)
# ═══════════════════════════════════════════════════════════════
# 여러 컬럼을 기준으로 계층적 그룹화

employee_detail = pd.DataFrame({
    'department': ['Dev', 'Dev', 'Dev', 'Sales', 'Sales', 'Sales', 'HR', 'HR'],
    'position': ['Junior', 'Mid', 'Senior', 'Junior', 'Mid', 'Senior', 'Mid', 'Senior'],
    'gender': ['M', 'F', 'M', 'F', 'M', 'M', 'F', 'F'],
    'salary': [4000, 4500, 5500, 3800, 4300, 5200, 4500, 5300]
})

print('=== 다중 그룹화 ===')

# 부서 → 직급 순서로 그룹화
multi_group1 = employee_detail.groupby(
    ['department', 'position'])['salary'].mean()
print('부서 → 직급 순 그룹화:')
print(multi_group1)
# 결과: 계층적 인덱스 (MultiIndex)
# Dev
#   Junior    4000
#   Mid       4500
#   Senior    5500
# HR
#   Mid       4500
#   Senior    5300
# ...
print()

# 직급 → 부서 순서로 그룹화 (순서가 다르면 결과 구조가 달라짐!)
multi_group2 = employee_detail.groupby(
    ['position', 'department'])['salary'].mean()
print('직급 → 부서 순 그룹화:')
print(multi_group2)
# 결과:
# Junior
#   Dev      4000
#   Sales    3800
# Mid
#   Dev      4500
#   HR       4500
#   Sales    4300
# ...
print()

'''
    다중 그룹화 팁:
    - 첫 번째 기준이 상위 레벨, 두 번째가 하위 레벨
    - unstack()으로 피벗 테이블처럼 변환 가능
    - reset_index()로 일반 DataFrame으로 변환
'''

# ═══════════════════════════════════════════════════════════════
# 9. agg() - 다양한 집계 동시 수행
# ═══════════════════════════════════════════════════════════════
# agg() = aggregate (집계하다)
# 여러 집계 함수를 한 번에 적용할 수 있는 강력한 메서드

monthly_sales = pd.DataFrame({
    'month': [1, 1, 2, 2, 3, 3, 1, 2, 3],
    'store': ['A', 'B', 'A', 'B', 'A', 'B', 'C', 'C', 'C'],
    'sales': [100, 80, 120, 90, 150, 100, 110, 95, 130],  # 매출
    'customers': [50, 40, 60, 45, 75, 50, 55, 48, 65]     # 고객수
})

print('=== agg() 다양한 사용법 ===')

# ─────────────────────────────────────────────────────────────
# 방법 1: 함수 이름 리스트 (가장 간단)
# ─────────────────────────────────────────────────────────────
result1 = monthly_sales.groupby('store')['sales'].agg(['mean', 'sum', 'std'])
print('방법 1: 함수 이름 리스트')
print(result1)
# 결과: 각 매장의 평균, 합계, 표준편차가 열로 표시됨
print()

# ─────────────────────────────────────────────────────────────
# 방법 2: 함수 객체 사용 (NumPy 함수 등)
# ─────────────────────────────────────────────────────────────
result2 = monthly_sales.groupby(
    'store')['sales'].agg([np.mean, np.sum, np.std])
print('방법 2: 함수 객체 사용')
print(result2)
# 결과: 컬럼명이 <ufunc 'mean'> 같은 형태로 나옴 (권장하지 않음)
print()

# ─────────────────────────────────────────────────────────────
# 방법 3: 딕셔너리로 컬럼별 다른 함수 적용 (가장 유연)
# ─────────────────────────────────────────────────────────────
result3 = monthly_sales.groupby('store').agg({
    'sales': ['mean', 'sum'],        # 매출: 평균, 합계
    'customers': ['mean', 'max']      # 고객수: 평균, 최댓값
})
print('방법 3: 딕셔너리로 컬럼별 다른 함수')
print(result3)
# 결과: 계층적 컬럼명 (MultiIndex)
#        sales              customers
#         mean   sum         mean  max
# store
# A      123.33  370         61.67  75
# B       90.00  270         45.00  50
# C      111.67  335         56.00  65
print()

# ─────────────────────────────────────────────────────────────
# 방법 4: 사용자 정의 함수 (람다 또는 def)
# ─────────────────────────────────────────────────────────────
result4 = monthly_sales.groupby('store')['sales'].agg([
    ('평균', 'mean'),
    ('합계', 'sum'),
    ('범위', lambda x: x.max() - x.min())  # 최댓값 - 최솟값
])
print('방법 4: 사용자 정의 함수와 이름 지정')
print(result4)
# 결과: 컬럼명을 한글로 지정 가능, 복잡한 계산 가능
print()

'''
═══════════════════════════════════════════════════════════════
GroupBy 실무 활용 패턴
═══════════════════════════════════════════════════════════════

1. 기본 집계
   df.groupby('부서')['연봉'].mean()

2. 다중 집계
   df.groupby('부서').agg({'연봉': 'mean', '근속연수': 'max'})

3. 다중 그룹화
   df.groupby(['부서', '직급'])['연봉'].mean()

4. 필터링과 결합
   df.groupby('부서').filter(lambda x: x['연봉'].mean() > 5000)

5. 변환(Transform)
   df['부서_평균'] = df.groupby('부서')['연봉'].transform('mean')

자주 사용되는 조합:
- as_index=False → 병합(merge) 작업 전
- sort=False → 대용량 데이터 성능 최적화
- agg(['mean', 'std']) → 평균과 분산 동시 확인
'''

# ═══════════════════════════════════════════════════════════════
# 실전 예제: 월별 매장 성과 분석
# ═══════════════════════════════════════════════════════════════

print('=== 종합 실전 예제 ===')

# 월별, 매장별 통합 분석
comprehensive = monthly_sales.groupby(['month', 'store']).agg({
    'sales': ['sum', 'mean'],
    'customers': ['sum', 'mean']
})

print('월별/매장별 종합 분석:')
print(comprehensive)
print()

# 매장별 총합 (월 구분 없이)
store_total = monthly_sales.groupby('store', as_index=False).agg({
    'sales': ['sum', 'mean'],
    'customers': 'sum'
})
print('매장별 총합:')
print(store_total)

print()
print()
