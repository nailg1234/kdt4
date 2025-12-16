import pandas as pd

# 다음 데이터를 CSV로 저장하고 다시 읽어오세요

practice_data = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['Seoul', 'Busan', 'Daegu']
})

# TODO:
# 1. 'practice.csv'로 저장 (인덱스 제외)
practice_data.to_csv('practice.csv', index=False)
# 2. 저장한 파일 읽어오기
csv_practice_data = pd.read_csv('practice.csv')
# 3. 읽어온 데이터 출력
print('문제 1.\n', csv_practice_data)
print()

# 한글 데이터를 UTF-8로 저장하고 읽어오세요

korean_data = pd.DataFrame({
    '이름': ['김철수', '이영희', '박민수'],
    '직급': ['사원', '대리', '과장']
})

# TODO:
# 1. UTF-8 인코딩으로 저장
korean_data.to_csv('korean_data.csv', index=False, encoding='utf-8-sig')
# 2. 같은 인코딩으로 읽어오기
csv_korean_data = pd.read_csv('korean_data.csv', encoding='utf-8-sig')
# 3. 한글이 깨지지 않았는지 확인
print('문제 2.\n', csv_korean_data)
