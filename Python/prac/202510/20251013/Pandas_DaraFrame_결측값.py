import pandas as pd
import numpy as np

# 데이터 정제

'''
    문제점)
    중복 데이터
    결측값 : None, NaN
    형식 불일치 : age, join_date
    이상값 : age 250
'''
# 결측값
'''
    결측값 (Missing Value)
    비어있는, 알 수 없는, 기록되지 않은 데이터를 의미합니다.
    종류
    None : Python의 빈 객체
    np.nan : Numpy의 Not a Number
    pd.NA : Pandas의 결측값(최신)
    빈 문자열 : '', " "(공백)
    특수 값 : -99999, 99999
'''

missing_types = pd.DataFrame({
    'none_type': [1, 2, None, 4],           # Python None
    'nan_type': [1, 2, np.nan, 4],         # NumPy NaN
    'empty_string': ['A', 'B', '', 'D'],   # 빈 문자열
    'whitespace': ['A', 'B', ' ', 'D'],    # 공백
    'special_value': [1, 2, -999, 4]       # -999를 결측값으로 사용하는 경우
})

print(missing_types)

# 결측값 탐지
# isnull() / isna()
# 결측값이면 True

# notnull() / notna()
# 값이 있으면 True

print('=== isna() ===')
print(missing_types.isna())
print('=== isnull() ===')
print(missing_types.isnull())

print('=== notna() ===')
print(missing_types.notna())
print('=== notnull() ===')
print(missing_types.notnull())

# 결측값 통계 확인
print('=== 열별 결측값 개수 ===')
print(missing_types.isna().sum())

# 전체 결측값 개수
print(missing_types.isna().sum().sum())

# 결측값 처리 전략

'''
    삭제 - 결측값이 있는 행/열 제거
    대체 - 다른 값으로 채우기
    예측 - 앞뒤 값이나 패턴으로 추정
'''

# 결측값이 있는 샘플 데이터
sales_data = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=7),
    'sales': [100, 120, np.nan, 150, np.nan, 180, 200],
    'customers': [20, 25, 22, np.nan, 30, 35, 40],
    'region': ['Seoul', 'Busan', np.nan, 'Daegu', 'Seoul', np.nan, 'Busan']
})

print('=== 원본 ===')
print(sales_data)
print()
# 삭제
# 1-1 결측값이 있는 행 전체 삭제
drop_rows = sales_data.dropna()
print('결측값이 있는 행 삭제:')
print(drop_rows)
print()

# 1-2 결측값이 있는 열 전체 삭제
drop_cols = sales_data.dropna(axis=1)
print('결측값이 있는 열 삭제:')
print(drop_cols)
print()

# 1-3 특정 열 기준 삭제 (여기선 'sales')
drop_sales = sales_data.dropna(subset=['sales'])
print('sales 열 기준으로만 삭제')
print(drop_sales)

# 대체
# 2-1 평균값으로 대체
fill_mean = sales_data.copy()
fill_mean['sales'] = fill_mean['sales'].fillna(
    fill_mean['sales'].mean())
print(fill_mean)
print()

# 2-2 중앙값으로 대체 (이상값이 있을때 유용)
fill_median = sales_data.copy()
fill_median['sales'] = fill_median['sales'].fillna(
    fill_median['sales'].median())
print(fill_median)
print()

# 시계열 대체
# 시간 순서가 있는 데이터에서 앞뒤 값으로 결측값을 채운다.
# 3-1 Forward fill (앞의 값으로 채우기)
fill_forward = sales_data.copy()
fill_forward['customers'] = fill_forward['customers'].fillna(method='ffill')
print(fill_forward)

# 3-2 Backward fill (뒤의 값으로 채우기)
fill_backward = sales_data.copy()
fill_backward['customers'] = fill_backward['customers'].fillna(method='bfill')
print(fill_backward)
