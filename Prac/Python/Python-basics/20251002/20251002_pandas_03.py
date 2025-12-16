import pandas as pd
# Data Frame
# Data Frame은 pandas 의 핵심 자료구조로,
# 2차원 표 형태의 데이터를 다루는 객체
'''
    핵심 개념
    2차원 구조: 행, 열로 구성된 표
    Series의 집합: 여러 개의 Series가 열로 배치된 형태
    레이블 기반: 각 행과 열에 이름(레이블)을 붙일 수 있음
    각 열마다 다른 데이터 타입 가능
'''

# Data Frame의 구성 요소
test_data = pd.DataFrame(
    # 1. 데이터(Value) - 2차원 배열
    data=[
        ['김철수', 27, "Dev", 4500],
        ['이영희', 23, "Hr", 4800]
    ],
    # 2. 행 인덱스(index) - 각 행의 레이블
    index=['E001', 'E002'],
    # 3. 열 이름(columns) - 각 열의 레이블
    columns=['name', 'age', 'department', 'salary']
)

print('=== Data Frame')
print(test_data)

print('=== 구성 요소 분석 ===')
print('1. 행 인덱스', test_data.index.tolist())
print('2. 열 이름', test_data.columns.tolist())
print('3. 데이터 형태', test_data.shape)  # (2, 4)
print('4. 행 개수', test_data.shape[0])  # 2
print('5. 열 개수', test_data.shape[1])  # 4
print('6. 전체 셀 개수', test_data.size)  # 8
