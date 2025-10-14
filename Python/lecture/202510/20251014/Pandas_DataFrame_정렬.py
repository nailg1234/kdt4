import pandas as pd

# 실습3. 정렬(1)
# 사용 데이터
df = pd.DataFrame({
'name': ['Alice', 'Bob', 'Charlie', 'David'],
'score': [88, 95, 70, 100]
})
# 1. 주어진 DataFrame에서, score 컬럼 기준으로 오름차순 정렬한 결과를 출력하세요.
print('문제1.')
print(df.sort_values(by='score'))
print()
# 2. score 컬럼 기준 내림차순으로 정렬한 후,
# 정렬된 인덱스를 무시하고 0부터 재정렬한 결과를 출력하세요.
print('문제2.')
print(df.sort_values(by='score', ascending=False, ignore_index=True))
print()
# 2025-10-01
# 실습3. 정렬(2)
# 사용 데이터
df = pd.DataFrame({
'이름': ['가', '나', '다', '라', '마'],
'반': [2, 1, 1, 2, 1],
'점수': [90, 85, 80, 95, 85]
})
# 3. 주어진 DataFrame에서,반(class) 기준 오름차순,
# 같은 반 내에서는 점수(score) 기준 내림차순으로 
# 정렬한 결과를 출력하세요.
print('문제3.')
print(df.sort_values(by=['반', '점수'], ascending=[True, False]))
print()
# 4. 열(컬럼) 이름을 알파벳순으로 정렬해서 출력하세요.
print('문제4.')
print(df.sort_index(axis=1))
print()

# 2025-10-01
# 실습3. 정렬(3)
# 사용 데이터
df = pd.DataFrame({
'value': [10, 20, 30, 40]
}, index=[3, 1, 4, 2])
# 5. 인덱스 기준으로 오름차순 정렬한 결과를 출력하세요.
print('문제5.')
print(df.sort_index())
print()

# 6. 인덱스 기준 내림차순 정렬, 
# value 컬럼 기준 오름차순 정렬 두 가지 정렬 결과를 각각 출력하세요.
print('문제6.')
print(df.sort_index(ascending=False))
print(df.sort_values(by='value'))