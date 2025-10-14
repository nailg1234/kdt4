import pandas as pd

# 실습3. 정렬(3)
# 사용 데이터
df = pd.DataFrame({
'value': [10, 20, 30, 40]
}, index=[3, 1, 4, 2])
# 5. 인덱스 기준으로 오름차순 정렬한 결과를 출력하세요.
print('문제5.')
print('인덱스 기준 오름차순\n', df.sort_index())
print()

# 6. 인덱스 기준 내림차순 정렬, value 컬럼 기준 오름차순 정렬 두 가지 정렬 결과를 각각 출력하
# 세요.
print('문제6.')
print('인덱스 기준 내림차순\n', df.sort_index(ascending=False))
print()
print('value 컬럼 기준 오름차순\n', df.sort_values(by='value'))
