import pandas as pd
import numpy as np

print("=" * 80)
print("Pandas DataFrame 완벽 가이드")
print("=" * 80)

# ============================================================================
# 1. DataFrame이란?
# ============================================================================
"""
DataFrame의 정의:
    - Pandas의 핵심 자료구조
    - 2차원 표(Table) 형태의 데이터를 다루는 객체
    - Excel 스프레드시트, SQL 테이블과 유사
    - 데이터 분석에서 가장 많이 사용되는 구조

비유로 이해하기:
    - Excel의 워크시트
    - SQL의 테이블
    - 관계형 데이터베이스의 테이블
    - CSV 파일의 내용

핵심 개념:
    1. 2차원 구조: 행(Row)과 열(Column)로 구성된 표
    2. Series의 집합: 여러 개의 Series가 열로 배치된 형태
    3. 레이블 기반: 각 행과 열에 이름(레이블)을 붙일 수 있음
    4. 혼합 타입 가능: 각 열마다 다른 데이터 타입을 가질 수 있음
       - 예: 이름(문자열), 나이(정수), 급여(실수)
"""

# ============================================================================
# 2. DataFrame의 구조
# ============================================================================
"""
DataFrame의 3가지 핵심 구성 요소:

    1. 데이터 (Values/Data)
       - 실제 저장된 값들
       - 2차원 배열(행렬) 형태
       - Numpy 배열로 내부 저장
    
    2. 행 인덱스 (Index)
       - 각 행을 식별하는 레이블
       - 기본값: 0, 1, 2, 3, ...
       - 사용자 정의 가능: 'E001', 'E002', ...
       - 행 데이터를 찾는 데 사용
    
    3. 열 이름 (Columns)
       - 각 열을 식별하는 레이블
       - 필드명, 속성명으로 사용
       - 예: 'name', 'age', 'salary'
       - 열 데이터를 찾는 데 사용

시각적 구조:
    
                   Columns (열 이름)
              ┌─────────┬─────┬────────┐
              │  name   │ age │ salary │
    ┌─────────┼─────────┼─────┼────────┤
    │  E001   │  김철수  │ 27  │  4500  │ ← Row (행)
Index├─────────┼─────────┼─────┼────────┤
(행   │  E002   │  이영희  │ 23  │  4800  │ ← Row (행)
인덱스)└─────────┴─────────┴─────┴────────┘
                    ↑       ↑      ↑
                 Column  Column Column
"""

# ============================================================================
# 3. DataFrame 생성 - 기본 예제
# ============================================================================

print("\n" + "=" * 80)
print("[1] 기본 DataFrame 생성")
print("=" * 80)

# 직원 정보를 담은 DataFrame
test_data = pd.DataFrame(
    # 1. 데이터 (Value) - 2차원 리스트
    data=[
        ['김철수', 27, "Dev", 4500],
        ['이영희', 23, "HR", 4800],
    ],
    # 2. 행 인덱스(index) - 각 행의 레이블 (사원 번호)
    index=['E001', 'E002'],
    # 3. 열 이름 (columns) - 각 열의 레이블 (필드명)
    columns=['name', 'age', 'department', 'salary']
)

print("\n생성된 DataFrame:")
print(test_data)
print()

# ============================================================================
# 4. DataFrame 구성 요소 상세 분석
# ============================================================================

print("=" * 80)
print("[2] DataFrame 구성 요소 상세 분석")
print("=" * 80)

# 4-1. 행 인덱스 (Index)
print("\n[2-1] 행 인덱스 (Index)")
print(f"      타입: {type(test_data.index)}")
print(f"      값: {test_data.index.tolist()}")
print(f"      설명: 각 행(직원)을 구분하는 고유 식별자")
print()

# 4-2. 열 이름 (Columns)
print("[2-2] 열 이름 (Columns)")
print(f"      타입: {type(test_data.columns)}")
print(f"      값: {test_data.columns.tolist()}")
print(f"      설명: 각 열(속성)의 이름")
print()

# 4-3. 데이터 형태 (Shape)
print("[2-3] 데이터 형태 (Shape)")
print(f"      값: {test_data.shape}")
print(
    f"      의미: (행 개수, 열 개수) = ({test_data.shape[0]}행, {test_data.shape[1]}열)")
print(f"      설명: 2명의 직원, 4개의 속성")
print()

# 4-4. 행 개수
print("[2-4] 행 개수")
print(f"      값: {test_data.shape[0]}")
print(f"      또는: {len(test_data)}")
print(f"      설명: 총 {test_data.shape[0]}명의 직원 데이터")
print()

# 4-5. 열 개수
print("[2-5] 열 개수")
print(f"      값: {test_data.shape[1]}")
print(f"      또는: {len(test_data.columns)}")
print(f"      설명: 각 직원마다 {test_data.shape[1]}개의 정보")
print()

# 4-6. 전체 셀 개수
print("[2-6] 전체 셀(데이터) 개수")
print(f"      값: {test_data.size}")
print(
    f"      계산: {test_data.shape[0]} × {test_data.shape[1]} = {test_data.size}")
print(f"      설명: 총 {test_data.size}개의 데이터 포인트")
print()

# ============================================================================
# 5. DataFrame 생성 방법 (다양한 방법)
# ============================================================================

print("=" * 80)
print("[3] DataFrame 생성 방법")
print("=" * 80)

# 방법 1: 딕셔너리로 생성 (가장 일반적)
print("\n[3-1] 딕셔너리로 생성 (열 기준)")
print("      → 각 키가 열 이름, 값이 열 데이터")

employees_dict = pd.DataFrame({
    'name': ['김철수', '이영희', '박민수'],
    'age': [27, 23, 35],
    'department': ['Dev', 'HR', 'Sales'],
    'salary': [4500, 4800, 5200]
})

print(employees_dict)
print()

# 방법 2: 리스트의 리스트로 생성 (행 기준)
print("[3-2] 리스트의 리스트로 생성 (행 기준)")
print("      → 각 내부 리스트가 한 행")

employees_list = pd.DataFrame(
    [
        ['김철수', 27, 'Dev', 4500],
        ['이영희', 23, 'HR', 4800],
        ['박민수', 35, 'Sales', 5200]
    ],
    columns=['name', 'age', 'department', 'salary']
)

print(employees_list)
print()

# 방법 3: 딕셔너리의 리스트로 생성
print("[3-3] 딕셔너리의 리스트로 생성 (각 행이 딕셔너리)")
print("      → JSON 데이터 형식과 유사")

employees_dict_list = pd.DataFrame([
    {'name': '김철수', 'age': 27, 'department': 'Dev', 'salary': 4500},
    {'name': '이영희', 'age': 23, 'department': 'HR', 'salary': 4800},
    {'name': '박민수', 'age': 35, 'department': 'Sales', 'salary': 5200}
])

print(employees_dict_list)
print()

# 방법 4: Numpy 배열로 생성
print("[3-4] Numpy 배열로 생성")
print("      → 대규모 수치 데이터에 적합")

data_array = np.array([
    [27, 4500],
    [23, 4800],
    [35, 5200]
])

employees_numpy = pd.DataFrame(
    data_array,
    columns=['age', 'salary'],
    index=['E001', 'E002', 'E003']
)

print(employees_numpy)
print()

# 방법 5: Series를 결합하여 생성
print("[3-5] Series를 결합하여 생성")
print("      → 각 열이 별도의 Series")

names = pd.Series(['김철수', '이영희', '박민수'], name='name')
ages = pd.Series([27, 23, 35], name='age')
departments = pd.Series(['Dev', 'HR', 'Sales'], name='department')

employees_series = pd.DataFrame({
    'name': names,
    'age': ages,
    'department': departments
})

print(employees_series)
print()

# ============================================================================
# 6. DataFrame 기본 속성
# ============================================================================

print("=" * 80)
print("[4] DataFrame 주요 속성")
print("=" * 80)

# 샘플 데이터 생성
df = pd.DataFrame({
    'name': ['김철수', '이영희', '박민수', '정수진'],
    'age': [27, 23, 35, 29],
    'department': ['Dev', 'HR', 'Sales', 'Dev'],
    'salary': [4500, 4800, 5200, 4700],
    'join_year': [2020, 2021, 2018, 2019]
})

print("\n원본 DataFrame:")
print(df)
print()

# 6-1. 데이터 값 (values)
print("[4-1] values - 데이터 값 (Numpy 배열)")
print(f"      타입: {type(df.values)}")
print("      값:")
print(df.values)
print()

# 6-2. 데이터 타입 (dtypes)
print("[4-2] dtypes - 각 열의 데이터 타입")
print(df.dtypes)
print()

# 6-3. 열 이름 (columns)
print("[4-3] columns - 열 이름 리스트")
print(df.columns.tolist())
print()

# 6-4. 행 인덱스 (index)
print("[4-4] index - 행 인덱스")
print(df.index.tolist())
print()

# 6-5. shape
print("[4-5] shape - (행 수, 열 수)")
print(f"      {df.shape}")
print(f"      → {df.shape[0]}명의 직원, {df.shape[1]}개의 정보")
print()

# 6-6. size
print("[4-6] size - 전체 데이터 개수")
print(f"      {df.size}개 (= {df.shape[0]} × {df.shape[1]})")
print()

# 6-7. ndim
print("[4-7] ndim - 차원")
print(f"      {df.ndim}차원 (DataFrame은 항상 2차원)")
print()

# ============================================================================
# 7. DataFrame 정보 확인 메서드
# ============================================================================

print("=" * 80)
print("[5] DataFrame 정보 확인 메서드")
print("=" * 80)

# 7-1. head() - 처음 n개 행
print("\n[5-1] head() - 처음 5개 행 (기본값)")
print(df.head())
print()

print("[5-2] head(2) - 처음 2개 행")
print(df.head(2))
print()

# 7-2. tail() - 마지막 n개 행
print("[5-3] tail() - 마지막 5개 행 (기본값)")
print(df.tail())
print()

print("[5-4] tail(2) - 마지막 2개 행")
print(df.tail(2))
print()

# 7-3. info() - 전체 정보 요약
print("[5-5] info() - DataFrame 전체 정보")
df.info()
print()

# 7-4. describe() - 수치형 데이터 통계
print("[5-6] describe() - 수치형 열의 통계 요약")
print(df.describe())
print()

# ============================================================================
# 8. Series vs DataFrame 비교
# ============================================================================

print("=" * 80)
print("[6] Series vs DataFrame 비교")
print("=" * 80)

print("""
┌─────────────────┬──────────────────────┬──────────────────────┐
│     특징        │       Series         │      DataFrame       │
├─────────────────┼──────────────────────┼──────────────────────┤
│ 차원            │ 1차원                │ 2차원                │
│ 구조            │ 값 + 인덱스          │ 값 + 인덱스 + 열이름 │
│ 비유            │ Excel의 한 개 열     │ Excel의 전체 시트    │
│ 데이터 타입     │ 단일 타입            │ 열마다 다른 타입     │
│ 생성            │ pd.Series()          │ pd.DataFrame()       │
│ 인덱싱          │ s[0], s['index']     │ df['col'], df.loc[]  │
└─────────────────┴──────────────────────┴──────────────────────┘

관계:
    DataFrame = 여러 개의 Series를 열로 결합한 것
    DataFrame의 한 개 열 = Series
""")

# 실제 예시
print("\n[실제 예시]")
print("\nDataFrame에서 한 개 열 추출 → Series:")
age_series = df['age']
print(age_series)
print(f"\n타입: {type(age_series)}")
print()

# ============================================================================
# 9. 실무 예제 - 직원 데이터 분석
# ============================================================================

print("=" * 80)
print("[7] 실무 예제 - 직원 데이터 분석")
print("=" * 80)

# 더 현실적인 직원 데이터
employee_data = pd.DataFrame({
    'employee_id': ['E001', 'E002', 'E003', 'E004', 'E005'],
    'name': ['김철수', '이영희', '박민수', '정수진', '최지훈'],
    'age': [27, 23, 35, 29, 31],
    'department': ['Dev', 'HR', 'Sales', 'Dev', 'Sales'],
    'position': ['Junior', 'Senior', 'Manager', 'Senior', 'Junior'],
    'salary': [4500, 4800, 5200, 4700, 4600],
    'join_year': [2020, 2021, 2018, 2019, 2020]
})

print("\n직원 데이터:")
print(employee_data)
print()

print("=" * 80)
print("데이터 요약:")
print(f"• 총 직원 수: {len(employee_data)}명")
print(f"• 데이터 항목: {employee_data.shape[1]}개")
print(f"• 평균 연봉: {employee_data['salary'].mean():.0f}만원")
print(f"• 평균 나이: {employee_data['age'].mean():.1f}세")
print(f"• 최고 연봉: {employee_data['salary'].max()}만원")
print(f"• 최저 연봉: {employee_data['salary'].min()}만원")
print("=" * 80)

print("\n" + "=" * 80)
print("DataFrame 기본 개념 학습 완료!")
print("=" * 80)
