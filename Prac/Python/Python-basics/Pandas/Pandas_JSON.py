import pandas as pd

sample_data = pd.DataFrame({
    'name': ['John', 'Jane', 'Park'],
    'age': [25, 30, 35],
    '도시': ['서울', '부산', '대구'],
    'salary': [50000, 60000, 55000]
})

# to_json(): DataFrame을 JSON 파일로 저장
sample_data.to_json('sample_data_records.json',
                    orient='records',      # orient: JSON 구조 방식 지정
                    # 'records': [{}, {}, {}] 형태 (레코드 배열)
                    # 'columns': {컬럼명: {인덱스: 값}} 형태
                    # 'index': {인덱스: {컬럼명: 값}} 형태
                    indent=2)             # indent=2: 들여쓰기 2칸 (가독성 향상)
sample_data.to_json('sample_data_records2.json',
                    orient='columns',
                    indent=2)
sample_data.to_json('sample_data_records3.json',
                    orient='index',
                    indent=2)
print('JSON 파일 저장')
print()

# read_json(): JSON 파일을 읽어서 DataFrame으로 변환
df_json = pd.read_json('sample_data.json')
print('=== JSON 파일 읽기 ===')
print(df_json)
print()

# === JSON 파일 읽기 ===
#    name  age  도시  salary
# 0  John   25  서울   50000
# 1  Jane   30  부산   60000
# 2  Park   35  대구   55000
