import pandas as pd
import numpy as np
# 그룹화 집계

# GroupBy
'''
    그룹화는 데이터를 특정 기준에 따라 묶어 분석하는 것
    
''' 

employee_data = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry'],
    'department': ['Dev', 'Dev', 'Sales', 'Sales', 'Dev', 'HR', 'HR', 'Sales'],
    'years': [3, 5, 2, 7, 10, 4, 6, 3],
    'salary': [4500, 5500, 4000, 6500, 8000, 4800, 5800, 4200]
})

print('전체 직원 데이터')
print(employee_data)

# 전체 분석 vs 그룹별 분석
print('전체 분석')
overall_avg = employee_data['salary'].mean()
print(f'전체 평균 연봉: {overall_avg}')
print()

print('그룹별 분석')
dept_avg = employee_data.groupby('department')['salary'].mean()
print(dept_avg)
print()

#GroupBy 핵심
'''
    Split - Apply - Combine
    3단계 프로세스

    1. Split(분할) - 데이터 그룹으로 나누기
    2. Apply(적용) - 각 그룹에 함수 적용
    3. Combine(결합) - 결과를 하나로 합치기
'''

print('=== Split - Apply - Combine ===')
simple_data = pd.DataFrame({
    'category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'value': [10, 20, 15, 25, 12, 22]
})
print('원본 데이터')
print(simple_data)
print()

# 1단계 Split(분할)
for category, group in simple_data.groupby('category'):
    print(f'{category} 그룹')
    print(group)
print()

# 2단계 Apply(적용)
for category, group in simple_data.groupby('category'):
    avg = group['value'].mean()
    print(f'{category} 그룹 평균 {avg}')
print()

# 3단계 Combine(결합)
result = simple_data.groupby('category')['value'].mean()
print(result)

# groupby(by=None, axis=0, Level=None, as_index=True, sort=True)
'''
    by : 그룹화 기준 (컬럼명 또는 컬럼명 리스트)
    as_index : 그룹 키를 인덱스로 사용여부 (기본=True)
    sort : 그룹 키를 정렬할지 여부 (기본=True)
'''

employee_data = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry'],
    'department': ['Dev', 'Dev', 'Sales', 'Sales', 'Dev', 'HR', 'HR', 'Sales'],
    'years': [3, 5, 2, 7, 10, 4, 6, 3],
    'salary': [4500, 5500, 4000, 6500, 8000, 4800, 5800, 4200]
})

# 방법 1 - 컬럼명 문자열
result1 = employee_data.groupby('department')['salary'].mean()
print(result1)
print()

# 방법 2 - 컬럼 접근 후 집계
result2 = employee_data.groupby('department').salary.mean()
print(result2)
print()

# 여러 컬럼 선택
result3 = employee_data.groupby('department')[['salary','years']].mean()
print(result3)
print()

# as_index 매개변수
result_indexed = employee_data.groupby('department',
                                       as_index=True)['salary'].mean()
print(result_indexed)
print(type(result_indexed)) # <class 'pandas.core.series.Series'>

result_no_indexed = employee_data.groupby('department',
                                       as_index=False)['salary'].mean()
print(result_no_indexed)
print(type(result_no_indexed)) # <class 'pandas.core.frame.DataFrame'>

# sort 매개변수
result_sorted = employee_data.groupby('department',
                                      sort=True)['salary'].mean()
print(result_sorted)

result_no_sorted = employee_data.groupby('department',
                                      sort=False)['salary'].mean()
print(result_no_sorted)

'''
    count() - 개수
    
    var() - 분산
    
    std() - 표준편차
    
    mean() - 평균

    median() - 중앙값
'''

# describe() 메서드
#   여러 통계를 한번에 계산하는 메서드
result = employee_data.groupby('department')['salary'].describe()
print(result)
print()

employee_detail = pd.DataFrame({
    'department': ['Dev', 'Dev', 'Dev', 'Sales', 'Sales', 'Sales', 'HR', 'HR'],
    'position': ['Junior', 'Mid', 'Senior', 'Junior', 'Mid', 'Senior', 'Mid', 'Senior'],
    'gender': ['M', 'F', 'M', 'F', 'M', 'M', 'F', 'F'],
    'salary': [4000, 4500, 5500, 3800, 4300, 5200, 4500, 5300]
})

multy_group = employee_detail.groupby(['department', 'position'])['salary'].mean()
print(multy_group)
print()
multy_group = employee_detail.groupby(['position', 'department'])['salary'].mean()
print(multy_group)
print()

# agg() 다양한 사용법
# 1. 함수 이름 리스트
result1 = multy_group = employee_detail.groupby(['department'])['salary'].agg(['mean', 'sum', 'std'])
print(result1)

# 2. 함수 객체 사용
# result2 = multy_group = employee_detail.groupby(['department'])['salary'].agg([np.mean, np.sum, np.std])

# 3. 튜플 사용
result3 = multy_group = employee_detail.groupby(['department']).agg(total=('salary', 'sum'),
                                                                             avg=('salary', 'mean'))
print(result3)


monthly_sales = pd.DataFrame({
    'month': [1, 1, 2, 2, 3, 3, 1, 2, 3],
    'store': ['A', 'B', 'A', 'B', 'A', 'B', 'C', 'C', 'C'],
    'sales': [100, 80, 120, 90, 150, 100, 110, 95, 130],
    'customers': [50, 40, 60, 45, 75, 50, 55, 48, 65]
})

# 4. 딕셔너리 사용
result4 = multy_group = monthly_sales.groupby('store').agg({'sales':['mean', 'sum'],
                                                            'customers':['mean', 'max']})
print(result4)