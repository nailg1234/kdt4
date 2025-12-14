import pandas as pd

sample_data = pd.DataFrame({
    'name': ['John', 'Jane', 'Park'],
    'age': [20, 30, 35],
    '도시': ['서울', '부산', '대구'],
    'salary': [50000, 60000, 70000]
})

sample_data.to_csv('sample_data.csv',
                   # index=False: 행 번호(0,1,2...)를 파일에 저장하지 않음
                   index=False,
                   # utf-8-sig: UTF-8 + BOM (Byte Order Mark)
                   encoding='utf-8-sig')

df = pd.read_csv('sample_data.csv', encoding='utf-8-sig')
# 저장할 때 사용한 인코딩과 동일한 인코딩으로 읽어야함

print('=== CSV 파일 읽기 === \n')
print(f'데이터 프레임:\n {df} \n')      # 전체 데이터프레임 출력
print(f'데이터 타입:\n {df.dtypes} \n')  # 각 열의 데이터 타입 확인 (int64, object 등)
print(f'데이터 크기:\n {df.shape} \n')  # (행 개수, 열 개수) 형태로 출력

# === CSV 파일 읽기 ===

# 데이터 프레임:
#     name  age  도시  salary
# 0  John   20  서울   50000
# 1  Jane   30  부산   60000
# 2  Park   35  대구   70000

# 데이터 타입:
#  name      object
# age        int64
# 도시        object
# salary     int64
# dtype: object

# 데이터 크기:
#  (3, 4)

sample_data = pd.DataFrame({
    'name': ['John', 'Jane', 'Park'],
    'age': [25, 30, 35],
    '도시': ['서울', '부산', '대구'],
    'salary': [50000, 60000, 55000]
})

# sep='\t': 탭(Tab) 문자로 구분된 파일 저장
# 주로 .txt 확장자와 함께 사용되며, 탭으로 구분된 값(TSV)이라고 부름
sample_data.to_csv('tab_separated.txt',
                   sep='\t',               # 구분자를 탭으로 설정
                   index=False)

# 탭으로 구분된 파일 읽기
df_tab = pd.read_csv('tab_separated.txt',
                     sep='\t')             # 읽을 때도 동일한 구분자 지정

print('=== CSV sep=탭 파일 읽기 === \n')
print(df_tab)
print()
print(df_tab.head())  # head(): 처음 5개 행만 출력 (데이터 미리보기에 유용)
# head(10)처럼 숫자를 지정하면 해당 개수만큼 출력

# === CSV sep=탭 파일 읽기 ===

#    name  age  도시  salary
# 0  John   25  서울   50000
# 1  Jane   30  부산   60000
# 2  Park   35  대구   55000

#    name  age  도시  salary
# 0  John   25  서울   50000
# 1  Jane   30  부산   60000
# 2  Park   35  대구   55000
