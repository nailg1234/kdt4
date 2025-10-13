import pandas as pd

data = {
    "이름": ["홍길동", "이순신", "김유신", "강감찬", "장보고", "이방원"],
    "나이": [23, 35, 31, 40, 28, 34],
    "직업": ["학생", "군인", "장군", "장군", "상인", "왕자"]
}

df = pd.DataFrame(data)

# 인덱싱
print('=== 인덱싱 ===')
print(df['이름'])
print()
print(df[['이름', '나이', '직업']])
print()

print('=== 슬라이싱 ===')
print(df[1:3])
print()
print(df[-2:])
print()

# DataFrame의 슬라이싱은 행(Row) 기준으로 동작한다.
# 열 단위 슬라이싱은 명시적으로 지정해야함
print(df[-2:]['이름'])

# iloc
print('=== iloc ===')
print(df)
print(df.iloc[0])  # 0번 행 전체
print(df.iloc[:, 1])  # 모든 행의 1번(컬럼) 나이
print(df.iloc[[0, 2, 4], [0, 2]])
print()

# loc
print('=== loc ===')
print(df.loc[0])
print(df.loc[:, ['나이']])
print(df.loc[:, ['이름', '나이']])
print(df.loc[1:3, ['이름', '나이']])  # 1 ~ 3 행 까지 3포함됨!
