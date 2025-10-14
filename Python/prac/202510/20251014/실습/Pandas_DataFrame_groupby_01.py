import pandas as pd
# 실습4. groupby 연습문제(1)
# 1. 각 학년(grade)별 평균 국어 점수(kor)를 구하세요.
df = pd.DataFrame({
'grade': [1, 2, 1, 2, 1, 3],
'name': ['Kim', 'Lee', 'Park', 'Choi', 'Jung', 'Han'],
'kor': [85, 78, 90, 92, 80, 75]
})

print('학년별 평균 국어 점수\n', df.groupby('grade')['kor'].mean())