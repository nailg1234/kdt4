import pandas as pd
# import numpy as np

# 통계 함수
# 데이터의 특징을 숫자로 요약하는 것
daily_sales = pd.Series([
    300, 400, 500, 123, 405,
    603, 400, 546, 436, 875,
    756, 400, 345, 345, 893,
    456, 345, 546, 334, 123,
    457, 876, 989, 678, 345,
    678, 998, 567, 456, 765
],
    index=pd.date_range('2025-09-01', periods=30),
    name='Sales'
)

# 평균(mean) : 모든 값의 합 / 개수
mean_value = daily_sales.mean()
print(f'1. 평균 (Mean) : {mean_value:.2f}만원')

# 중앙값(Median) : 정렬했을 때 가운데 값
median_value = daily_sales.median()
print(f'2. 중앙값 (Median) : {median_value}만원')

# 최빈값(Mode) : 가장 자주 나타나는 값
mode_value = daily_sales.mode()
print(f'3. 최빈값 (Mode) : \n{mode_value}만원')

# 산포도 측정
# 데이터가 얼마나 퍼져있는지 알려주는 통계량
print('=== 산포도 측정 ===')
max_value = daily_sales.max()
min_value = daily_sales.min()

print(f'최댓값:{max_value}')
print(f'최솟값:{min_value}')

# 범위(Range) : 최댓값 - 최솟값
range_value = max_value - min_value
print(f'3. 범위(range): {range_value}')


# 분산(Variance): 평균으로 부터 떨어진 정도의 제곱의 평균
variance = daily_sales.var()
print(f'4. 분산(Variance) : {variance:.2f}')

# 표준편차(standard Deviation) : 분산의 제곱근
std_dev = daily_sales.std()
print(f'5. 표준편차 (Std Dev) : {std_dev:.2f}')

# 표준편차 해석
print('표준편차 해석 : ')
print(f'평균 표준편차 : {mean_value - std_dev:.2f}')

# 한번에 모든 통계
print(daily_sales.describe())
