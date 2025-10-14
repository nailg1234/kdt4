import pandas as pd

# 실습4. groupby 연습문제(2)
# 2. 아래 DataFrame에서 반(class)별, 과목(subject)별로 
# 시험에 응시한 학생 수(count)와 평균 점수(avg)를 구하세요.
df = pd.DataFrame({
'class': [1, 1, 1, 2, 2, 2],
'subject': ['Math', 'Math', 'Eng', 'Math', 'Eng', 'Eng'],
'score': [80, 90, 85, 70, 95, 90]
})

print('반, 과목 별 학생수, 평균점수\n',
      df.groupby(['class', 'subject']).agg(['count', 'mean']))


result = df.groupby(['class', 'subject'])['score'].agg(['count', 'mean'])
# result.rename(columns={'mean', 'avg'}, inplace=True)
# print(result)