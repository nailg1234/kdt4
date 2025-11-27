
# ═══════════════════════════════════════════════════════════════
# 추가 실전 예제 및 고급 팁
# ═══════════════════════════════════════════════════════════════

print("=" * 60)
print("추가 실전 예제")
print("=" * 60)

# ─────────────────────────────────────────────────────────────
# 예제 1: 조건 필터링 종합
# ─────────────────────────────────────────────────────────────

students = pd.DataFrame({
    '이름': ['철수', '영희', '민수', '지영', '동현'],
    '학년': [1, 2, 1, 2, 3],
    '성별': ['남', '여', '남', '여', '남'],
    '수학': [85, 92, 78, 95, 88],
    '영어': [90, 88, 85, 92, 94]
})

print("\n[원본 데이터]")
print(students)
print()

# 복합 조건 1: 1학년 남학생
print("[복합 조건 1] 1학년 남학생:")
result = students[(students['학년'] == 1) & (students['성별'] == '남')]
print(result)
print()

# 복합 조건 2: 수학 90점 이상 OR 영어 90점 이상
print("[복합 조건 2] 수학 90점 이상 OR 영어 90점 이상:")
result = students[(students['수학'] >= 90) | (students['영어'] >= 90)]
print(result)
print()

# 복합 조건 3: 부정 조건 (NOT)
# ~ 연산자: 조건의 반대
print("[복합 조건 3] 1학년이 아닌 학생:")
result = students[~(students['학년'] == 1)]
# 또는: students[students['학년'] != 1]
print(result)
print()

# 복합 조건 4: 범위 조건
# between(최소값, 최대값): 특정 범위 내의 값
print("[복합 조건 4] 수학 점수 80~90점:")
result = students[students['수학'].between(80, 90)]
# 또는: students[(students['수학'] >= 80) & (students['수학'] <= 90)]
print(result)
print()

# 복합 조건 5: 문자열 포함 검색
# str.contains('문자열'): 문자열 포함 여부
students_copy = students.copy()
students_copy['이름'] = ['김철수', '이영희', '박민수', '최지영', '정동현']
print("[복합 조건 5] 이름에 '영'이 포함된 학생:")
result = students_copy[students_copy['이름'].str.contains('영')]
print(result)
print()

# ─────────────────────────────────────────────────────────────
# 예제 2: 행/열 추가 삭제 종합
# ─────────────────────────────────────────────────────────────

scores = pd.DataFrame({
    '이름': ['A', 'B', 'C'],
    '점수1': [80, 90, 85]
})

print("\n[행/열 추가 삭제 종합]")
print("원본:")
print(scores)
print()

# 1. 여러 열 동시 추가
print("1. 여러 열 동시 추가:")
scores['점수2'] = [85, 88, 90]
scores['점수3'] = [82, 91, 87]
print(scores)
print()

# 2. 계산된 값으로 열 추가
print("2. 평균 열 추가 (계산):")
scores['평균'] = (scores['점수1'] + scores['점수2'] + scores['점수3']) / 3
# 또는: scores['평균'] = scores[['점수1', '점수2', '점수3']].mean(axis=1)
print(scores)
print()

# 3. 조건부 열 추가
print("3. 합격 여부 열 추가 (조건부):")
# np.where(조건, 참일때값, 거짓일때값)
scores['합격'] = np.where(scores['평균'] >= 85, '합격', '불합격')
print(scores)
print()

# 4. 여러 열 동시 삭제
print("4. 점수1, 점수2 열 삭제:")
scores = scores.drop(['점수1', '점수2'], axis=1)
# 또는: scores = scores.drop(columns=['점수1', '점수2'])
print(scores)
print()

# 5. 여러 행 동시 삭제
print("5. 불합격 학생 모두 삭제:")
scores = scores[scores['합격'] == '합격']
# 또는: scores = scores.drop(scores[scores['합격'] == '불합격'].index)
print(scores)
print()

# ─────────────────────────────────────────────────────────────
# 예제 3: 정렬 고급 활용
# ─────────────────────────────────────────────────────────────

employees = pd.DataFrame({
    '부서': ['영업', '개발', '영업', '개발', '인사'],
    '이름': ['김', '이', '박', '최', '정'],
    '급여': [4500, 5500, 4800, 6000, 4200],
    '경력': [3, 5, 4, 7, 2]
})

print("\n[정렬 고급 활용]")
print("원본:")
print(employees)
print()

# 1. 부서별 정렬 후 급여 내림차순
print("1. 부서 오름차순 → 급여 내림차순:")
result = employees.sort_values(
    by=['부서', '급여'],
    ascending=[True, False]  # 부서는 오름차순, 급여는 내림차순
)
print(result)
print()

# 2. 정렬 후 순위 컬럼 추가
print("2. 급여순 순위 추가:")
employees_ranked = employees.copy()
# rank(): 순위 계산 (기본: 평균 순위, method='min'으로 최소 순위)
employees_ranked['급여순위'] = employees_ranked['급여'].rank(
    ascending=False,  # 높은 급여가 1위
    method='min'      # 동점은 최소 순위
)
print(employees_ranked.sort_values('급여순위'))
print()

# 3. 상위 N개 추출 (정렬 + 슬라이싱)
print("3. 급여 상위 3명:")
top3 = employees.nlargest(3, '급여')  # nlargest(개수, 기준컬럼)
# 또는: employees.sort_values('급여', ascending=False).head(3)
print(top3)
print()

# 4. 하위 N개 추출
print("4. 경력 하위 2명:")
bottom2 = employees.nsmallest(2, '경력')  # nsmallest(개수, 기준컬럼)
print(bottom2)
print()

# ─────────────────────────────────────────────────────────────
# 예제 4: GroupBy 고급 활용
# ─────────────────────────────────────────────────────────────

sales_data = pd.DataFrame({
    '지역': ['서울', '서울', '부산', '부산', '서울', '부산'],
    '분기': ['Q1', 'Q2', 'Q1', 'Q2', 'Q3', 'Q3'],
    '매출': [100, 120, 80, 90, 130, 95],
    '비용': [60, 70, 50, 55, 75, 60]
})

print("\n[GroupBy 고급 활용]")
print("원본:")
print(sales_data)
print()

# 1. 그룹별 통계 + 새 컬럼 계산
print("1. 지역별 매출 통계:")
result = sales_data.groupby('지역').agg({
    '매출': ['sum', 'mean', 'count'],
    '비용': 'sum'
})
print(result)
print()

# 2. transform으로 그룹 평균 추가
# transform(): 원본과 같은 크기로 결과 반환
print("2. 지역별 평균 매출 컬럼 추가:")
sales_with_avg = sales_data.copy()
sales_with_avg['지역평균매출'] = sales_data.groupby('지역')['매출'].transform('mean')
print(sales_with_avg)
# transform의 특징: 각 행에 해당 그룹의 집계 값이 채워짐
print()

# 3. 그룹별 누적합
print("3. 지역별 매출 누적합:")
sales_with_cumsum = sales_data.copy()
sales_with_cumsum['누적매출'] = sales_data.groupby('지역')['매출'].cumsum()
print(sales_with_cumsum)
print()

# 4. 그룹별 필터링
# filter(함수): 조건을 만족하는 그룹만 반환
print("4. 총 매출 300 이상인 지역만:")
result = sales_data.groupby('지역').filter(
    lambda x: x['매출'].sum() >= 300
)
print(result)
# 서울의 총 매출: 100+120+130 = 350 (포함)
# 부산의 총 매출: 80+90+95 = 265 (제외)
print()

# 5. 사용자 정의 집계 함수
print("5. 지역별 매출 범위 (최대-최소):")
result = sales_data.groupby('지역')['매출'].agg(
    범위=lambda x: x.max() - x.min()
)
print(result)
print()

# 6. 피벗 테이블처럼 활용
print("6. 지역/분기별 매출 (unstack):")
result = sales_data.groupby(['지역', '분기'])['매출'].sum().unstack(fill_value=0)
# unstack(): MultiIndex를 피벗 테이블 형태로 변환
print(result)
print()

# ─────────────────────────────────────────────────────────────
# 예제 5: 종합 실전 문제
# ─────────────────────────────────────────────────────────────

print("\n[종합 실전 문제]")

# 고객 구매 데이터
purchases = pd.DataFrame({
    '고객ID': ['A001', 'A001', 'A002', 'A003', 'A002', 'A001', 'A003'],
    '상품': ['노트북', '마우스', '키보드', '모니터', '노트북', '키보드', '마우스'],
    '금액': [1200000, 30000, 80000, 300000, 1300000, 85000, 35000],
    '수량': [1, 2, 1, 1, 1, 1, 3],
    '날짜': ['2024-01-15', '2024-01-20', '2024-02-10',
           '2024-02-15', '2024-03-05', '2024-03-10', '2024-03-20']
})

print("원본 구매 데이터:")
print(purchases)
print()

# 문제 1: 고객별 총 구매금액과 구매횟수
print("문제 1: 고객별 총 구매금액과 구매횟수")
result = purchases.groupby('고객ID').agg(
    총구매금액=('금액', 'sum'),
    구매횟수=('금액', 'count'),
    평균구매금액=('금액', 'mean')
).round(0)  # 소수점 반올림
print(result)
print()

# 문제 2: 100만원 이상 구매한 고객만 추출
print("문제 2: 100만원 이상 구매 내역:")
high_value = purchases[purchases['금액'] >= 1000000]
print(high_value)
print()

# 문제 3: 고객별 총 구매금액이 150만원 이상인 고객
print("문제 3: 총 구매금액 150만원 이상 고객:")
customer_total = purchases.groupby('고객ID')['금액'].sum()
vip_customers = customer_total[customer_total >= 1500000]
print(vip_customers)
print()

# 문제 4: 상품별 판매현황
print("문제 4: 상품별 판매현황:")
product_sales = purchases.groupby('상품').agg(
    판매횟수=('수량', 'count'),
    총판매수량=('수량', 'sum'),
    총판매금액=('금액', 'sum')
).sort_values('총판매금액', ascending=False)
print(product_sales)
print()

# 문제 5: 날짜를 datetime으로 변환하고 월별 집계
print("문제 5: 월별 매출:")
purchases['날짜'] = pd.to_datetime(purchases['날짜'])
purchases['월'] = purchases['날짜'].dt.month
monthly_sales = purchases.groupby('월')['금액'].sum()
print(monthly_sales)
print()

'''
═══════════════════════════════════════════════════════════════
핵심 메서드 체크리스트
═══════════════════════════════════════════════════════════════

□ 조건 필터링:
  - df[조건]
  - df[(조건1) & (조건2)]  # AND
  - df[(조건1) | (조건2)]  # OR
  - df[~조건]              # NOT
  - df['열'].isin([값들])
  - df['열'].between(최소, 최대)
  - df['열'].str.contains('문자')

□ 행/열 추가:
  - df['새열'] = 값
  - df.loc[인덱스] = [값들]
  - pd.concat([df, new_df], ignore_index=True)

□ 행/열 삭제:
  - df.drop('열', axis=1)
  - df.drop(인덱스)
  - df.drop(['열1', '열2'], axis=1)
  - df[조건]  # 필터링으로 간접 삭제

□ 정렬:
  - df.sort_values(by='열')
  - df.sort_values(by=['열1', '열2'], ascending=[True, False])
  - df.sort_index()
  - df.nlargest(n, '열')
  - df.nsmallest(n, '열')

□ 그룹화:
  - df.groupby('열')['집계열'].함수()
  - df.groupby('열').agg({'열1': '함수1', '열2': '함수2'})
  - df.groupby('열').agg(이름=('열', '함수'))
  - df.groupby('열')['열'].transform('함수')
  - df.groupby('열').filter(lambda x: 조건)

□ 인덱스 관리:
  - df.reset_index(drop=True)
  - df.set_index('열')
  - df.index

□ 데이터 타입:
  - pd.to_datetime('날짜')
  - df['열'].astype('타입')
'''

# ═══════════════════════════════════════════════════════════════
# 실무 팁과 주의사항
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("실무 팁과 주의사항")
print("=" * 60)

print("""
1. 조건 필터링 시:
   ✅ 조건마다 괄호() 필수
   ✅ and/or 대신 &/| 사용
   ✅ 여러 값 비교는 isin() 사용
   ❌ df[df.score >= 80 and df.name == 'A']  # 오류!
   ✅ df[(df.score >= 80) & (df.name == 'A')]  # 정상

2. 원본 보존:
   ✅ 원본 변경: df.drop(..., inplace=True)
   ✅ 새 변수: new_df = df.drop(...)
   ❌ 주의: 대부분의 메서드는 원본을 변경하지 않음!

3. 인덱스 관리:
   ✅ 필터링/삭제 후 reset_index(drop=True)
   ✅ concat 시 ignore_index=True
   ❌ 인덱스 불연속 방치 → 접근 오류 발생

4. 정렬 후:
   ✅ inplace=True 또는 재할당
   ✅ reset_index(drop=True)로 인덱스 정리
   ❌ 정렬만 하고 저장 안 함 → 원본 그대로

5. GroupBy 활용:
   ✅ as_index=False → 병합 작업 전
   ✅ 명명된 집계로 가독성 향상
   ✅ transform으로 원본 크기 유지
   ❌ 너무 많은 그룹 → 성능 저하

6. 성능 최적화:
   ✅ 큰 데이터는 필터링 먼저
   ✅ 불필요한 정렬 피하기 (sort=False)
   ✅ 필요한 열만 선택
   ❌ 전체 데이터에서 무거운 연산

7. 데이터 검증:
   ✅ df.info() → 데이터 타입 확인
   ✅ df.isnull().sum() → 결측값 확인
   ✅ df.describe() → 통계 요약
   ✅ df.duplicated().sum() → 중복 확인
""")

# ═══════════════════════════════════════════════════════════════
# 자주 하는 실수와 해결법
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("자주 하는 실수와 해결법")
print("=" * 60)

print("""
실수 1: SettingWithCopyWarning
문제: df_filtered = df[df.score > 80]
     df_filtered['grade'] = 'A'  # 경고 발생!
해결: df_filtered = df[df.score > 80].copy()

실수 2: 조건문 괄호 누락
문제: df[df.age > 20 & df.city == 'Seoul']  # 오류!
해결: df[(df.age > 20) & (df.city == 'Seoul')]

실수 3: 인덱스 불일치
문제: df1과 df2를 병합했는데 인덱스가 꼬임
해결: reset_index(drop=True) 사용

실수 4: inplace 오해
문제: result = df.sort_values('col', inplace=True)
     print(result)  # None 출력됨!
해결: inplace=True면 반환값이 None
     df.sort_values('col', inplace=True)
     또는
     result = df.sort_values('col')

실수 5: 문자열 컬럼에 수치 연산
문제: df['age'].mean()  # 오류 (age가 문자열)
해결: df['age'] = df['age'].astype(int)
     df['age'].mean()

실수 6: 날짜 형식 미변환
문제: df['date'] > '2024-01-01'  # 문자열 비교
해결: df['date'] = pd.to_datetime(df['date'])
     df['date'] > '2024-01-01'  # 날짜 비교
""")

print("\n" + "=" * 60)
print("코드 작성 완료!")
print("=" * 60)
