import pandas as pd

# 실습3. 정렬(1)
# 사용 데이터
df = pd.DataFrame({
'name': ['Alice', 'Bob', 'Charlie', 'David'],
'score': [88, 95, 70, 100]
})
# 1. 주어진 DataFrame에서,
# score 컬럼 기준으로 오름차순 정렬한 결과를 출력하세요.
print('문제1.')
print('score 오름차순 정렬\n', df.sort_values(by='score'))
print()

# 2. score 컬럼 기준 내림차순으로 정렬한 후,
# 정렬된 인덱스를 무시하고 0부터 재정렬한 결과를
# 출력하세요.
print('문제2.')
df = df.sort_values(by='score', ascending=False, ignore_index=True)
print(df)