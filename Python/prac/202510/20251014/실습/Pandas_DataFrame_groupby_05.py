import pandas as pd

# 실습4. groupby 연습문제(5)
# 5. 아래 DataFrame에서 부서(dept)별로 성별(gender)별 인원 수와, 총 연봉(salary) 합계를
# 구하세요.
df = pd.DataFrame({
'dept': ['HR', 'HR', 'IT', 'IT', 'Sales', 'Sales'],
'gender': ['M', 'F', 'F', 'M', 'F', 'F'],
'salary': [3500, 3200, 4000, 4200, 3000, 3100]
})

print('부서별 성별 인원수\n',df.groupby('dept')['gender'].count())
print('부서별 총 연봉 합계\n',df.groupby('dept')['salary'].sum())

# 리더님 작성
print(df.groupby(['dept', 'gender']).agg(['sum', 'count']))
result = df.groupby(['dept', 'gender']).agg(
    count=('salary', 'count'),
    total_salary=('salary', 'sum')
)
print(result)