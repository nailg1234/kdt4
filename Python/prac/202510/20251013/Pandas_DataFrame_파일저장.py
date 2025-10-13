import pandas as pd

# DataFrame vs Series

# Series
# 1차원

# DataFrame
# 2차원(Series들의 묶음)
# 데이터(values) - 2차원 배열
# 행 인덱스(index) - 각 행의 레이블
# 열 이름(columns) - 각 열의 레이블

# df_default = pd.DataFrame({
#     'name': ['Kim', 'Lee', 'Park'],
#     'age': [25, 26, 27]
# }, index=['Kim', 'Lee', 'Park'])

# print(df_default.index)
# print(f'인덱스 : {df_default.index}')
# print(f'열 이름 : {df_default.columns}')

# CSV파일
# CSV(comma-separated Values) 가장 널리 사용되는 데이터 파일 형식

'''
    특징
    쉼표(,)로 값을 구분
    텍스트 파일이라 어디서나 열람 가능
    가볍도 빠름
    Excel, Google Sheets 등과 호환
'''
sample_data = pd.DataFrame({
    'name': ['John', 'Jane', 'Park'],
    'age': [25, 30, 35],
    '도시': ['서울', '부산', '대구'],
    'salary': [50000, 60000, 55000]
})

# UTF-8로 저장 (기본값, 권장)
sample_data.to_csv('sample_data.csv', index=False, encoding='utf-8-sig')

# utf-8-sig : UTF8 + BOM (Excel 호환)

# CP949로 저장 (Window 한글)
# sample_data.to_csv('sample_data.csv', index=False, encoding='cp949')

df = pd.read_csv('sample_data.csv', encoding='utf-8-sig')
print('=== CSV 파일 읽기 ===')
print(df)
print(f'데이터 타입:\n {df.dtypes}')
print(f'데이터 크기:\n {df.shape}')

# seq - 구분자 설정
sample_data.to_csv('tab_separated.txt',
                   sep='\t',
                   index=False)
df_tab = pd.read_csv('tab_separated.txt', sep='\t')
print('=== CSV sep=tab 파일 읽기 ===')
print(df_tab)
print(df_tab.head())  # - 처음 5개 행(기본값)

# Excel
# 엑셀은 마이크로소프트의 스프레드시트 프로그램입니다.
'''
    특징
    여러 시트(Sheet) 지원
    서식, 수식 포함 가능
    비즈니스에서 가장 많이 사용
    확장자 (.xlsx)최신 / (.xls)구버전
    pip install openpyxl
'''

sample_data = pd.DataFrame({
    'name': ['John', 'Jane', 'Park'],
    'age': [25, 30, 35],
    '도시': ['서울', '부산', '대구'],
    'salary': [50000, 60000, 55000]
})

sample_data.to_excel('sample_data.xlsx',
                     index=False,
                     sheet_name='Default')
print('샘플 엑셀 파일 생성 완료')

df_excel = pd.read_excel('sample_data.xlsx')
print('=== Excel 파일 읽기 ===')
print(df_excel)

# 여러 시트 다루기
with pd.ExcelWriter('multi_sheet.xlsx') as writer:
    sample_data.to_excel(writer,
                         sheet_name='Default1',
                         index=False)
    sample_data['name'].to_excel(writer,
                                 sheet_name='name',
                                 index=False)
print('2개의 시트를 가진 엑셀파일 생성 완료')

# JSON
# JSON(JavaScript Object Notation)
# 웹에서 많이 사용되는 데이터 형식

sample_data.to_json('sample_data.json',
                    orient='records',
                    indent=2)
print('JSON 파일 저장')
print()

df_json = pd.read_json('sample_data.json')
print('=== JSON 파일 읽기 ===')
print(df_json)
