import pandas as pd

# 실습3. 정렬(2)
# 사용 데이터
df = pd.DataFrame({
'이름': ['가', '나', '다', '라', '마'],
'반': [2, 1, 1, 2, 1],
'점수': [90, 85, 80, 95, 85]
})
# 3. 주어진 DataFrame에서,반(class) 기준 오름차순,
# 같은 반 내에서는 점수(score) 기준 내림차순으로 정렬한 결과를 출력하세요.
print('문제3.')
df.sort_values(by=['반', '점수'], ascending=[True, False])
print('반, 점수 정렬\n', df.sort_values(by=['반', '점수'], ascending=[True, False]))
print()

# 4. 열(컬럼) 이름을 알파벳순으로 정렬해서 출력하세요.
print('문제4.')
print('컬럼 정렬\n', df.sort_index(axis=1))