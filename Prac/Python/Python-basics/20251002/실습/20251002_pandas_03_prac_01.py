# 실습2. DataFrame 연습(1)
import pandas as pd
# 1. 다음 데이터로 DataFrame을 생성하고, 컬럼명을 '이름', '나이', '도시'로 지정하세요.
# • [['홍길동', 28, '서울'], ['김철수', 33, '부산'], ['이영희', 25, '대구']]

result = pd.DataFrame(
    columns=['이름', '나이', '도시'],
    data=[
        ['홍길동', 28, '서울'],
        ['김철수', 33, '부산'],
        ['이영희', 25, '대구']
    ]
)
print('문제 1.\n', result)

# 2. 아래와 같은 딕셔너리로 DataFrame을 생성하세요.
result = pd.DataFrame(
    {'A': [1, 2, 3],
     'B': [4, 5, 6]}
)
print('문제 2.\n', result)

# 3. 아래 데이터를 사용해 DataFrame을 만드세요.
result = pd.DataFrame([
    {'과목': '수학', '점수': 90},
    {'과목': '영어', '점수': 85},
    {'과목': '과학', '점수': 95}
])
print('문제 3.\n', result)

# 4. 아래 데이터를 사용해 DataFrame을 생성하되, 인덱스를 ['학생1', '학생2', '학생3']으로 지정
# 하세요.
result = pd.DataFrame(
    data={'이름': ['민수', '영희', '철수'], '점수': [80, 92, 77]},
    index=['학생1', '학생2', '학생3']
)
print('문제 4.\n', result)

# 5. 아래 Series 객체 2개를 이용해 DataFrame을 만드세요.
kor = pd.Series([90, 85, 80], index=['a', 'b', 'c'])
eng = pd.Series([95, 88, 82], index=['a', 'b', 'c'])

result = pd.DataFrame(
    data=[kor, eng]
)
print('문제 5.\n', result)

# 6. 아래 딕셔너리로 DataFrame을 만들고, 컬럼 순서를 ['B', 'A']로 지정해 출력하세요.
result = pd.DataFrame(
    data={'A': [1, 2], 'B': [3, 4]},
    columns=['B', 'A']
)
print('문제 6.\n', result)

# 7. 데이터를 DataFrame으로 만들고, 컬럼명을 ['product', 'price', 'stock']으로 변경하세요.
result = pd.DataFrame(
    data=[['펜', 1000, 50], ['노트', 2000, 30]],
    columns=['product', 'price', 'stock']
)
print('문제 7.', result)

# 8. 아래 DataFrame을 생성한 뒤, '국가' 컬럼만 추출하세요.
# • {'국가': ['한국', '일본', '미국'], '수도': ['서울', '도쿄', '워싱턴']}
result = pd.DataFrame({'국가': ['한국', '일본', '미국'], '수도': ['서울', '도쿄', '워싱턴']})
print('문제 8.\n', result['국가'])
