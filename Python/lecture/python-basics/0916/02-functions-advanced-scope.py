# ==========================================
# 딕셔너리 중요 메서드들과 순회 완전 가이드
# ==========================================

import copy

print("=" * 60)
print("1. setdefault() 메서드 - 안전한 키 생성")
print("=" * 60)

scores = {
    '김철수': 85,
    '이영희': 92,
    '박민수': 78
}
print(f"초기 점수: {scores}")

# setdefault(key, default_value)
# - 키가 없으면: 새 키-값 쌍을 추가하고 default_value 반환
# - 키가 있으면: 기존 값을 그대로 유지하고 기존 값 반환

# 새로운 학생 추가
new_score = scores.setdefault('정수진', 88)  # 키가 없으므로 새로 추가
print(f"정수진 점수 설정: {new_score}")
print(f"점수 추가 후: {scores}")

# 기존 학생의 점수는 변경되지 않음
existing_score = scores.setdefault('김철수', 100)  # 기존 값(85) 유지
print(f"김철수 기존 점수 유지: {existing_score}")
print(f"최종 점수: {scores}")

# setdefault() 활용 예시 - 그룹화할 때 매우 유용
students_by_grade = {}
student_data = [
    ('김철수', 1), ('이영희', 2), ('박민수', 1),
    ('정수진', 2), ('최동훈', 1)
]

print(f"\n학년별 그룹화 예시:")
for name, grade in student_data:
    # 학년 키가 없으면 빈 리스트 생성, 있으면 기존 리스트 사용
    students_by_grade.setdefault(grade, []).append(name)

print(f"학년별 학생: {students_by_grade}")

# setdefault 없이 구현하면 (더 복잡함)
students_manual = {}
for name, grade in student_data:
    if grade not in students_manual:
        students_manual[grade] = []
    students_manual[grade].append(name)
print(f"수동 구현 결과: {students_manual}")

print("\n" + "=" * 60)
print("2. copy() vs deepcopy() - 복사 방법의 차이")
print("=" * 60)

# 얕은 복사(Shallow Copy) vs 깊은 복사(Deep Copy)
scores = {
    '김철수': 85,
    '이영희': 92,
    '박민수': 78
}

# copy() - 얕은 복사: 딕셔너리 자체만 복사, 내부 객체는 참조 공유
scores_copy = scores.copy()
scores_copy['최동훈'] = 95  # 새 키 추가
scores_copy['김철수'] = 10  # 기존 키 수정

print(f"원본 scores: {scores}")           # 원본은 변경되지 않음
print(f"복사본 scores_copy: {scores_copy}")  # 복사본만 변경됨

print(f"\n단순 딕셔너리에서는 copy()로 충분합니다.")

# 중첩 딕셔너리에서의 얕은 복사 vs 깊은 복사
nested_dict = {
    "team1": {
        'leader': '김철수',
        'members': ['이영희', '박민수']  # 리스트는 가변 객체
    },
    "team2": {
        'leader': '정수진',
        'members': ['최동훈', '강미나']
    }
}
print(f"\n원본 중첩 딕셔너리: {nested_dict}")

# 얕은 복사: 내부의 리스트들은 여전히 같은 객체를 참조
shallow = nested_dict.copy()

# 깊은 복사: 모든 내부 객체까지 새로 복사
deep = copy.deepcopy(nested_dict)

# 원본의 내부 리스트 수정
nested_dict['team1']['members'].append('신입사원')
print(f"\n원본에 '신입사원' 추가 후:")
print(f"원본: {nested_dict['team1']['members']}")
print(f"얕은 복사(영향 받음): {shallow['team1']['members']}")  # 같은 리스트를 참조하므로 변경됨
print(f"깊은 복사(영향 없음): {deep['team1']['members']}")    # 별도 리스트이므로 변경 안됨

# 또 다른 테스트
shallow['team2']['leader'] = '새로운 리더'  # 딕셔너리 자체는 독립적
print(f"\n얕은 복사에서 리더 변경:")
print(f"원본 team2 리더: {nested_dict['team2']['leader']}")
print(f"얕은 복사 team2 리더: {shallow['team2']['leader']}")

# 메모리 관리 관점에서의 설명
print(f"\n메모리 참조 확인:")
print(
    f"원본과 얕은 복사의 team1 members가 같은 객체인가?: {nested_dict['team1']['members'] is shallow['team1']['members']}")
print(
    f"원본과 깊은 복사의 team1 members가 같은 객체인가?: {nested_dict['team1']['members'] is deep['team1']['members']}")

print("\n" + "=" * 60)
print("3. 딕셔너리 순회(Iteration) 방법들")
print("=" * 60)

scores = {
    '김철수': 85,
    '이영희': 92,
    '박민수': 78,
    '정수진': 88
}

# 방법 1: 키만 순회 (기본 방식)
print("1) 키만 순회 (기본 방식):")
for key in scores:  # 기본적으로 키를 순회
    print(f'{key}: {scores[key]}점')

print("\n2) 키만 순회 (명시적 방식):")
for key in scores.keys():  # 명시적으로 keys() 메서드 사용
    print(f'{key}: {scores[key]}점')

# 방법 2: 값만 순회
print("\n3) 값만 순회:")
for value in scores.values():
    print(f'점수: {value}점')

# 값들로 통계 계산
total_score = sum(scores.values())
average_score = total_score / len(scores)
max_score = max(scores.values())
min_score = min(scores.values())

print(f"\n점수 통계:")
print(f"총점: {total_score}점")
print(f"평균: {average_score:.1f}점")
print(f"최고점: {max_score}점")
print(f"최저점: {min_score}점")

# 방법 3: 키-값 쌍 순회 (가장 일반적이고 유용)
print("\n4) 키-값 쌍 순회:")
for key, value in scores.items():
    print(f'{key}: {value}점')

# 방법 4: 인덱스와 함께 순회
print("\n5) 인덱스와 함께 순회:")
for idx, (key, value) in enumerate(scores.items()):
    print(f'{idx+1}번째 - {key}: {value}점')

# 순회하면서 조건부 처리
print("\n6) 조건부 순회:")
print("90점 이상인 학생들:")
for name, score in scores.items():
    if score >= 90:
        print(f'  {name}: {score}점 (우수)')

print("\n80점 미만인 학생들:")
for name, score in scores.items():
    if score < 80:
        print(f'  {name}: {score}점 (보충 필요)')

print("\n" + "=" * 60)
print("4. 고급 순회 기법들")
print("=" * 60)

# 딕셔너리 정렬하여 순회
print("1) 점수순으로 정렬하여 순회:")
# key 함수를 사용하여 값(점수)으로 정렬
for name, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
    print(f'  {name}: {score}점')

print("\n2) 이름순으로 정렬하여 순회:")
# 키(이름)로 정렬
for name, score in sorted(scores.items()):
    print(f'  {name}: {score}점')

# 딕셔너리 컴프리헨션과 순회
print("\n3) 조건에 맞는 새 딕셔너리 생성:")
high_scores = {name: score for name, score in scores.items() if score >= 85}
print(f"85점 이상: {high_scores}")

# 값 변환하며 새 딕셔너리 생성
grade_dict = {name: 'A' if score >= 90 else 'B' if score >= 80 else 'C'
              for name, score in scores.items()}
print(f"등급 변환: {grade_dict}")

print("\n" + "=" * 60)
print("5. 실용적인 순회 활용 예시")
print("=" * 60)

# 예시 1: 학급 성적 분석
scores = {
    '김철수': 85, '이영희': 92, '박민수': 78, '정수진': 88,
    '최동훈': 95, '강미나': 83, '윤서준': 76, '한지원': 89
}

print("1) 학급 성적 분석:")
grade_distribution = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

for name, score in scores.items():
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    else:
        grade = 'D'

    grade_distribution[grade] += 1
    print(f"  {name}: {score}점 ({grade}등급)")

print(f"\n등급별 분포: {grade_distribution}")

# 예시 2: 재고 관리 시스템
inventory = {
    '노트북': {'재고': 15, '가격': 1200000},
    '마우스': {'재고': 50, '가격': 25000},
    '키보드': {'재고': 3, '가격': 80000},
    '모니터': {'재고': 8, '가격': 300000}
}

print("\n2) 재고 관리 시스템:")
total_value = 0
low_stock_items = []

for item, details in inventory.items():
    stock = details['재고']
    price = details['가격']
    item_value = stock * price
    total_value += item_value

    print(f"  {item}: 재고 {stock}개, 가격 {price:,}원, 총액 {item_value:,}원")

    if stock < 10:
        low_stock_items.append(item)

print(f"\n총 재고 가치: {total_value:,}원")
print(f"재고 부족 품목: {low_stock_items}")

# 예시 3: 단어 빈도 분석
text = "python is great python is easy python programming is fun"
words = text.split()

print("\n3) 단어 빈도 분석:")
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# 빈도순으로 정렬하여 출력
for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
    print(f"  '{word}': {count}번")

print("\n" + "=" * 60)
print("6. 순회 시 주의사항과 팁")
print("=" * 60)

print("주의사항:")
print("1. 순회 중 딕셔너리 크기 변경 금지")
print("   - 순회 중 키 추가/삭제하면 RuntimeError 발생 가능")

print("\n2. 안전한 수정 방법:")
scores_to_modify = {'A': 10, 'B': 20, 'C': 30}

# 잘못된 방법 (순회 중 수정)
# for key in scores_to_modify:
#     if scores_to_modify[key] < 15:
#         del scores_to_modify[key]  # RuntimeError 위험!

# 올바른 방법 1: 별도 리스트에 키 저장 후 삭제
keys_to_delete = []
for key, value in scores_to_modify.items():
    if value < 15:
        keys_to_delete.append(key)

for key in keys_to_delete:
    del scores_to_modify[key]
print(f"안전한 삭제 후: {scores_to_modify}")

# 올바른 방법 2: 딕셔너리 컴프리헨션 사용
original = {'A': 10, 'B': 20, 'C': 30}
filtered = {k: v for k, v in original.items() if v >= 15}
print(f"컴프리헨션으로 필터링: {filtered}")

print("\n성능 팁:")
print("1. 큰 딕셔너리에서는 .items() 사용")
print("2. 키만 필요하면 기본 순회 사용")
print("3. 값만 필요하면 .values() 사용")
print("4. 조건부 순회 시 컴프리헨션 고려")

print("\n" + "=" * 60)
print("7. 메모리 효율적인 순회 방법")
print("=" * 60)

large_dict = {f'key_{i}': i**2 for i in range(10)}

print("1) 기본 순회 (메모리 효율적):")
for key in large_dict:  # 키를 하나씩 생성
    print(f"{key}: {large_dict[key]}")
    if key == 'key_3':  # 예시를 위해 일부만 출력
        print("  ... (나머지 생략)")
        break

print("\n2) list() 변환은 메모리 사용량 증가:")
print(f"keys() 객체 크기: 작음 (뷰 객체)")
print(f"list(keys()) 크기: 큼 (실제 리스트 생성)")

# 메모리 사용량 비교 (개념적 설명)
print("\n메모리 사용 패턴:")
print("- dict.keys(): 뷰 객체 - 메모리 효율적")
print("- list(dict.keys()): 실제 리스트 - 메모리 사용량 증가")
print("- 일반적으로 list() 변환은 필요할 때만 사용")
