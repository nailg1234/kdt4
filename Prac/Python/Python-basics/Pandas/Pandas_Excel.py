import pandas as pd

sample_data = pd.DataFrame({
    'name': ['John', 'Jane', 'Park'],
    'age': [25, 30, 35],
    '도시': ['서울', '부산', '대구'],
    'salary': [50000, 60000, 55000]
})

# to_excel(): DataFrame을 Excel 파일로 저장
sample_data.to_excel('sample_data.xlsx',
                     index=False,              # 행 번호 제외
                     sheet_name='Default')     # 시트 이름 지정
print('샘플 엑셀 파일 생성 완료')

# read_excel(): Excel 파일을 읽어서 DataFrame으로 변환
df_excel = pd.read_excel('sample_data.xlsx')
# 시트 이름을 지정하지 않으면 첫 번째 시트를 자동으로 읽음

print('=== Excel 파일 읽기 ===')
print(f'{df_excel}\n')

# === Excel 파일 읽기 ===
#    name  age  도시  salary
# 0  John   25  서울   50000
# 1  Jane   30  부산   60000
# 2  Park   35  대구   55000

sample_data = pd.DataFrame({
    'name': ['John', 'Jane', 'Park'],
    'age': [25, 30, 35],
    '도시': ['서울', '부산', '대구'],
    'salary': [50000, 60000, 55000]
})

# ExcelWriter: 여러 시트를 하나의 Excel 파일에 저장할 때 사용
# with 문을 사용하면 파일이 자동으로 저장되고 닫힘
with pd.ExcelWriter('multi_sheet.xlsx') as writer:
    # 첫 번째 시트: 전체 데이터
    sample_data.to_excel(writer,
                         sheet_name='Default1',  # 시트 이름
                         index=False)

    # 두 번째 시트: 이름 열만 저장
    sample_data['name'].to_excel(writer,
                                 sheet_name='name',
                                 index=False)
    print('2개의 시트를 가진 엑셀 파일 생성 완료')
# 2개의 시트를 가진 엑셀 파일 생성 완료

# 특정 시트 읽기 예시:
df = pd.read_excel('multi_sheet.xlsx', sheet_name='Default1')
print(df)
# 모든 시트 읽기 예시:
all_sheets = pd.read_excel('multi_sheet.xlsx', sheet_name=None)  # 딕셔너리 형태로 반환
print(all_sheets)

#    name  age  도시  salary
# 0  John   25  서울   50000
# 1  Jane   30  부산   60000
# 2  Park   35  대구   55000
# {'Default1':    name  age  도시  salary
# 0  John   25  서울   50000
# 1  Jane   30  부산   60000
# 2  Park   35  대구   55000, 'name':    name
# 0  John
# 1  Jane
# 2  Park}
