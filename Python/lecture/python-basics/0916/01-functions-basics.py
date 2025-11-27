# ==========================================
# Python 딕셔너리(Dictionary) 완전 가이드
# ==========================================

# 딕셔너리란?
# - Key-Value 쌍으로 데이터를 저장하는 자료구조
# - 해시 테이블 기반으로 매우 빠른 검색 속도 (O(1))
# - Python의 가장 강력하고 유용한 자료구조 중 하나

import copy
print("=" * 60)
print("1. 딕셔너리가 필요한 이유")
print("=" * 60)

# 딕셔너리를 사용하지 않는 경우 - 두 개의 리스트로 관리 (비효율적)
student_ids = ["20230001", "20230002", "20230003"]
student_names = ["김철수", "이영희", "박민수"]

print("리스트로 관리하는 경우:")
print(f"학번 리스트: {student_ids}")
print(f"이름 리스트: {student_names}")

# 특정 학번의 이름을 찾으려면? (비효율적 - O(n) 시간복잡도)
target_id = "20230002"
if target_id in student_ids:  # 전체 리스트를 순차 검색
    index = student_ids.index(target_id)  # 또 다시 순차 검색 O(n)
    name = student_names[index]
    print(f"학번 {target_id}의 이름: {name}")

# 딕셔너리를 사용하는 경우 - 직관적이고 빠름 (O(1) 시간복잡도)
students = {
    "20230001": "김철수",
    "20230002": "이영희",
    "20230003": "박민수"
}

print(f"\n딕셔너리로 관리: {students}")
print(f"학번 20230002의 이름: {students['20230002']}")  # O(1) - 즉시 접근!

print("\n" + "=" * 60)
print("2. 딕셔너리의 주요 특징")
print("=" * 60)

# 딕셔너리의 5가지 주요 특징:
print("1. Key-Value 쌍: 각 값에 고유한 키로 접근")
print("2. 빠른 검색: O(1) 시간 복잡도로 데이터 접근")
print("3. 변경 가능(Mutable): 요소 추가, 수정, 삭제 가능")
print("4. Key는 유일: 중복 키 불가 (값은 중복 가능)")
print("5. 순서 보장: Python 3.7+ 부터 삽입 순서 유지")

# 특징 확인 예시
sample_dict = {"a": 1, "b": 2, "a": 3}  # 중복 키 - 마지막 값으로 덮어씀
print(f"\n중복 키 처리: {sample_dict}")  # {'a': 3, 'b': 2}

# 순서 보장 확인 (Python 3.7+)
ordered_dict = {"첫번째": 1, "두번째": 2, "세번째": 3}
print(f"순서 보장 확인: {list(ordered_dict.keys())}")

print("\n" + "=" * 60)
print("3. 딕셔너리 생성 방법들")
print("=" * 60)

# 방법 1: 빈 딕셔너리 생성
empty_dict1 = {}  # 중괄호 사용
empty_dict2 = dict()  # dict() 생성자 사용
print(f"빈 딕셔너리 타입 확인: {type(empty_dict1)}, {type(empty_dict2)}")

# 방법 2: 값이 있는 딕셔너리 생성 (리터럴 방식)
person = {
    'name': '김철수',
    'age': 25,
    'city': 'seoul'
}
print(f"person: {person}")

# 방법 3: dict() 생성자 사용 (키워드 인자)
person2 = dict(name='이영희', age=25, city='부산')
print(f"person2: {person2}")

# 방법 4: 리스트/튜플 쌍으로부터 생성
pairs = [('a', 1), ('b', 2), ('c', 3)]  # 리스트의 튜플들
dict_from_pairs = dict(pairs)
print(f"쌍에서 생성된 딕셔너리: {dict_from_pairs}")

# 튜플의 튜플로도 가능
tuple_pairs = (('x', 10), ('y', 20), ('z', 30))
dict_from_tuples = dict(tuple_pairs)
print(f"튜플 쌍에서 생성: {dict_from_tuples}")

# 방법 5: zip()을 이용한 생성 (매우 유용!)
keys = ['name', 'age', 'city']
values = ['박민수', 21, '대전']
person3 = dict(zip(keys, values))  # 두 리스트를 쌍으로 묶어서 딕셔너리 생성
print(f"zip으로 생성: {person3}")

# 방법 6: Dictionary Comprehension (고급 기법)
squares = {x: x**2 for x in range(1, 6)}  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(f"comprehension으로 생성: {squares}")

# 조건부 comprehension
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"조건부 comprehension: {even_squares}")

# 방법 7: fromkeys() 메서드 - 같은 기본값으로 초기화
keys = ['a', 'b', 'c']
default_dict = dict.fromkeys(keys, 0)  # 모든 키에 0으로 초기화
print(f"fromkeys로 생성: {default_dict}")

# 주의: 가변 객체를 기본값으로 사용할 때
# wrong_way = dict.fromkeys(['a', 'b'], [])  # 모든 키가 같은 리스트를 참조!
# 올바른 방법은 comprehension 사용
right_way = {key: [] for key in ['a', 'b']}  # 각각 다른 리스트 생성
print(f"올바른 초기화: {right_way}")

print("\n" + "=" * 60)
print("4. Key로 사용 가능한 데이터 타입")
print("=" * 60)

# Hashable(해시 가능한) 타입만 key로 사용 가능 - 불변 타입들
valid_dict = {
    1: "정수",
    3.14: "실수",
    '문자열': 'string',
    (1, 2): "튜플",
    True: '불리언',  # True는 1과 같으므로 정수 키와 충돌 주의
    frozenset([1, 2]): "frozenset"
}
print(f"유효한 키 타입들: {valid_dict}")

# 키 충돌 예시 (True와 1은 같은 키로 취급)
collision_example = {1: "정수", True: "불리언"}
print(f"키 충돌 예시: {collision_example}")  # True가 1을 덮어씀

# Unhashable(해시 불가능한) 타입은 key로 사용 불가 - 가변 타입들
print("사용 불가능한 키 타입들:")
print("- 리스트: [1, 2]")
print("- 딕셔너리: {'a': 1}")
print("- 집합: {1, 2}")

# 다음 코드들은 TypeError를 발생시킵니다:
# invalid_dict = {[1, 2]: "리스트"}  # TypeError
# invalid_dict = {{1, 2}: "집합"}   # TypeError
# invalid_dict = {{'a': 1}: "딕셔너리"}  # TypeError

print("\n" + "=" * 60)
print("5. 딕셔너리 접근과 조회")
print("=" * 60)

student = {
    'name': '김철수',
    'age': 20,
    'major': '컴퓨터공학',
    'gpa': 3.7
}
print(f"student 딕셔너리: {student}")

# 방법 1: 대괄호 표기법 (빠르지만 KeyError 위험)
name = student['name']
print(f"이름 (대괄호): {name}")

# 존재하지 않는 키 접근 시 에러 발생
# grade = student['grade']  # KeyError 발생!
print("존재하지 않는 키 접근 시 KeyError 발생")

# 방법 2: get() 메서드 (안전한 접근)
major = student.get('major')
print(f"전공 (get): {major}")

# 존재하지 않는 키 - None 반환
grade1 = student.get('grade')
print(f"존재하지 않는 키 (get): {grade1}")  # None

# 기본값 지정 가능
grade2 = student.get('grade', 'N/A')
print(f"기본값과 함께 get: {grade2}")  # N/A

# 방법 3: setdefault() - 키가 없으면 기본값 설정하고 반환
email = student.setdefault('email', 'no-email@example.com')
print(f"setdefault 결과: {email}")
print(f"setdefault 후 딕셔너리: {student}")

# 방법 4: 딕셔너리의 구조 파악
print(f"모든 키들: {list(student.keys())}")
print(f"모든 값들: {list(student.values())}")
print(f"모든 키-값 쌍: {list(student.items())}")

# 키 존재 여부 확인
print(f"'name' 키 존재?: {'name' in student}")
print(f"'grade' 키 존재?: {'grade' in student}")

print("\n" + "=" * 60)
print("6. 딕셔너리 수정과 추가")
print("=" * 60)

student = {
    'name': '김철수',
    'age': 20,
    'major': '컴퓨터공학',
    'gpa': 3.7
}
print(f"원본 student: {student}")

# 기존 값 수정
student['age'] = 23
print(f"나이 수정 후: {student}")

# 새로운 키-값 추가
student['grade'] = 3
print(f"학년 추가 후: {student}")

# update() 메서드로 여러 값 한 번에 수정/추가
student.update({
    'gpa': 4.0,
    'city': 'seoul',
    'email': 'ethan@gmail.com'
})
print(f"update() 후: {student}")

# 다른 딕셔너리로 업데이트
info_dict = {
    'age': 22,
    'grade': 1,
    'phone': '010-1234-1234'
}
student.update(info_dict)
print(f"다른 딕셔너리로 update 후: {student}")

# 키워드 인자로도 업데이트 가능
student.update(scholarship=True, club='프로그래밍동아리')
print(f"키워드 인자로 update 후: {student}")

print("\n" + "=" * 60)
print("7. 딕셔너리 값 삭제")
print("=" * 60)

student_backup = student.copy()  # 백업 생성

# 방법 1: del 키워드 - 키 삭제 (값 반환 안함)
del student['grade']
print(f"del로 grade 삭제 후: {student}")

# 방법 2: pop() 메서드 - 값을 반환하면서 삭제
popped_phone = student.pop('phone')
print(f"pop으로 제거된 phone: {popped_phone}")
print(f"pop 후 딕셔너리: {student}")

# 존재하지 않는 키 pop 시 기본값 반환
popped_unknown = student.pop('unknown_key', 'KEY_NOT_FOUND')
print(f"존재하지 않는 키 pop: {popped_unknown}")

# 방법 3: popitem() - 마지막 항목 제거 (LIFO: Last In, First Out)
last_item = student.popitem()
print(f"popitem으로 제거된 마지막 항목: {last_item}")
print(f"popitem 후 딕셔너리: {student}")

# 방법 4: clear() - 모든 요소 제거
student.clear()
print(f"clear() 후: {student}")

print("\n" + "=" * 60)
print("8. 딕셔너리 순회(반복)")
print("=" * 60)

student = student_backup.copy()  # 백업에서 복원
print(f"순회할 딕셔너리: {student}")

# ====================================================

# 방법 1: 키만 순회
print("\n키만 순회:")
for key in student:  # 기본적으로 키를 순회
    print(f"키: {key}")

for key in student.keys():  # 명시적으로 키 순회
    print(f"키 (명시적): {key}")

# 방법 2: 값만 순회
print("\n값만 순회:")
for value in student.values():
    print(f"값: {value}")

# 방법 3: 키-값 쌍 순회 (가장 일반적)
print("\n키-값 쌍 순회:")
for key, value in student.items():
    print(f"{key}: {value}")

# 방법 4: 인덱스와 함께 순회
print("\n인덱스와 함께 순회:")
for index, (key, value) in enumerate(student.items()):
    print(f"{index}: {key} = {value}")

print("\n" + "=" * 60)
print("9. 딕셔너리 메서드들")
print("=" * 60)

original_dict = {'a': 1, 'b': 2, 'c': 3}
print(f"원본 딕셔너리: {original_dict}")

# copy() - 얕은 복사
copied_dict = original_dict.copy()
copied_dict['d'] = 4
print(f"복사된 딕셔너리: {copied_dict}")
print(f"원본은 변경 안됨: {original_dict}")

# 중첩 딕셔너리의 경우 깊은 복사 필요
nested_dict = {'user': {'name': 'Alice', 'age': 25}}
shallow_copy = nested_dict.copy()
deep_copy = copy.deepcopy(nested_dict)

shallow_copy['user']['age'] = 30  # 원본도 변경됨
print(f"얕은 복사 후 원본: {nested_dict}")  # age가 30으로 변경됨

# len() - 딕셔너리 크기
print(f"딕셔너리 크기: {len(original_dict)}")

print("\n" + "=" * 60)
print("10. 고급 딕셔너리 활용")
print("=" * 60)

# 중첩 딕셔너리
students_db = {
    "20230001": {
        "name": "김철수",
        "age": 20,
        "grades": {"수학": 90, "영어": 85, "과학": 92}
    },
    "20230002": {
        "name": "이영희",
        "age": 19,
        "grades": {"수학": 95, "영어": 88, "과학": 90}
    }
}

# 중첩 딕셔너리 접근
student_id = "20230001"
student_name = students_db[student_id]["name"]
math_grade = students_db[student_id]["grades"]["수학"]
print(f"학생 {student_id}의 이름: {student_name}")
print(f"수학 점수: {math_grade}")

# 안전한 중첩 접근
english_grade = students_db.get(student_id, {}).get(
    "grades", {}).get("영어", "점수 없음")
print(f"영어 점수: {english_grade}")

# 딕셔너리 병합 (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
# merged = dict1 | dict2  # Python 3.9+
merged = {**dict1, **dict2}  # 이전 버전에서도 동작
print(f"딕셔너리 병합: {merged}")

# 조건부 딕셔너리 생성
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = {num: num**2 for num in numbers if num % 2 == 0}
print(f"짝수의 제곱: {even_squares}")

# 딕셔너리 뒤집기 (키-값 교환)
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {value: key for key, value in original.items()}
print(f"뒤집힌 딕셔너리: {reversed_dict}")

print("\n" + "=" * 60)
print("11. 실용적인 딕셔너리 활용 예시")
print("=" * 60)

# 1) 카운터 구현
text = "hello world"
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(f"문자 카운터: {char_count}")

# 더 간단한 방법 (setdefault 사용)
char_count2 = {}
for char in text:
    char_count2.setdefault(char, 0)
    char_count2[char] += 1
print(f"setdefault 사용: {char_count2}")

# 2) 그룹화
students_list = [
    {"name": "김철수", "grade": 1},
    {"name": "이영희", "grade": 2},
    {"name": "박민수", "grade": 1},
    {"name": "최지영", "grade": 2}
]

grouped_by_grade = {}
for student in students_list:
    grade = student["grade"]
    if grade not in grouped_by_grade:
        grouped_by_grade[grade] = []
    grouped_by_grade[grade].append(student["name"])

print(f"학년별 그룹화: {grouped_by_grade}")

# 3) 캐시 구현
cache = {}


def expensive_function(n):
    if n in cache:
        print(f"캐시에서 반환: {n}")
        return cache[n]

    print(f"계산 중: {n}")
    result = n ** 2  # 복잡한 계산이라고 가정
    cache[n] = result
    return result


print(f"첫 번째 호출: {expensive_function(5)}")
print(f"두 번째 호출: {expensive_function(5)}")  # 캐시에서 반환

# 4) 설정 관리
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp"
    },
    "api": {
        "timeout": 30,
        "retry_count": 3
    }
}

db_host = config["database"]["host"]
api_timeout = config.get("api", {}).get("timeout", 60)  # 기본값 60
print(f"DB 호스트: {db_host}")
print(f"API 타임아웃: {api_timeout}")

print("\n" + "=" * 60)
print("딕셔너리 vs 다른 자료구조 비교")
print("=" * 60)

print("딕셔너리 사용이 좋은 경우:")
print("- 키-값 관계의 데이터를 저장할 때")
print("- 빠른 검색이 필요할 때")
print("- 데이터의 구조화가 필요할 때")
print("- 고유 식별자로 데이터에 접근할 때")

print("\n리스트 사용이 좋은 경우:")
print("- 순서가 중요한 데이터")
print("- 인덱스 기반 접근이 필요할 때")
print("- 중복 데이터를 허용해야 할 때")

print("\n성능 비교:")
print("- 검색: 딕셔너리 O(1) vs 리스트 O(n)")
print("- 삽입: 딕셔너리 O(1) vs 리스트 O(1) (끝에 추가)")
print("- 삭제: 딕셔너리 O(1) vs 리스트 O(n) (중간 삭제)")

print("\n" + "=" * 60)
print("딕셔너리 사용 시 주의사항")
print("=" * 60)

print("1. 키는 불변 타입만 사용 가능")
print("2. 키의 순서는 Python 3.7+ 에서만 보장")
print("3. 중첩 딕셔너리 복사 시 깊은 복사 고려")
print("4. 키 존재 여부 확인 후 접근하는 습관")
print("5. 메모리 사용량이 리스트보다 많음")
