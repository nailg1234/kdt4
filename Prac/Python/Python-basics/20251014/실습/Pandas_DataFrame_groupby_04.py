import pandas as pd

# 실습4. groupby 연습문제(4)
# 4. 아래 DataFrame에서 팀(team)별, 포지션(position)별로 결측치(NaN)를 포함한 점수
# (score)의 평균을 구하세요.
df = pd.DataFrame({
'team': ['A', 'A', 'B', 'B', 'A', 'B'],
'position': ['FW', 'DF', 'FW', 'DF', 'DF', 'FW'],
'score': [3, 2, None, 1, 4, 2]
})

print('팀별 점수 평균\n', df.groupby(['team', 'position'])['score'].mean())
# 리더님 작성
print('팀별 점수 평균\n', df.groupby(['team', 'position'], dropna=True)['score'].mean())