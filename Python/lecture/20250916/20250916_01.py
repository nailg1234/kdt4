# Dictionary(딕셔너리)
# Key-Value 쌍으로 데이터를 저장하는 자료구조
# 해시 테이블 기반으로 매우 빠른 검색 속도
# Python에서 가장 강력하고 유용한 자료 구조


# 딕셔너리를 사용하지 않는 경우 - 두개의 리스트로 관리
student_ids = ["20230001", "20230002", "20230003"]
student_names = ["김철수", "이영희", "박민수"]

# 특정 학번의 이름을 찾으려면?
target_id = "20230002"
if target_id in student_ids:
    index = student_ids.index(target_id)
    name = student_names[index]
    print(name)


# 딕셔너리를 사용 하는 경우 - 직관적이고 빠름

students = {
    "20230001": "김철수",
    "20230002": "이영희",
    "20230003": "박민수"
}

print(students["20230002"])  # O(1) - 즉시 접근

# 특징
# Key-Value 쌍 : 각 값에 고유한 키로 접근
# 빠른 검색 : O(1) 시간 복잡도
# 변경 가능 (Mutable) : 요소 추가, 수정, 삭제 가능
# Key는 유일 : 중복 키 불가(값은 중복 가능)
# 순서 보장 : Python3.7+ 부터 삽입 순서 유지


# Dictionary 생성
# 1. 빈 딕셔너리 생성
emtpy_dict = {}  # 비어있는 dict
emtpy_dict2 = dict()  # 비어있는 dict
empty_set = set()  # 비어있는 set

# 2. 값이 있는 딕셔너리 생성
person = {
    'name': '김철수',
    'age': 25,
    'city': 'seoul'
}

print('person : ', person)
# 3. dict() 생성자 사용
person2 = dict(name='이영희', age=25, city='부산')
print('person2 : ', person2)

# 4. 리스트/튜플로부터 생성
pairs = [('a', 1), ('b', 2)]

dict_from_pairs = dict(pairs)
print('dict_from_pairs : ', dict_from_pairs)

# 5. zip()을 이용한 생성
keys = ['name', 'age', 'city']
values = ['박민수', '21', '대전']

person3 = dict(zip(keys, values))
print('person :', person3)

# 6. dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print('squares', squares)

# 7 fromkeys()
keys = ['a', 'b', 'c']
default_dict = dict.fromkeys(keys, 'A')

print(default_dict)

# Key로 사용 가능한 타입
# Hashable 타입만 key로 사용 가능
valid_dict = {
    1: "정수",
    3.14: "실수",
    '문자열': 'string',
    (1, 2): "튜플",
    True: '불리언',
    frozenset([1, 2]): 'frozenset'
}

# Unhashable 타입은 key로 사용 불가
# invalid_dict = {
#     [1, 2]: '리스트',
#     {1, 2}: 'set',
#     {'a': 1}: '딕셔너리'
# } TypeError 발생

# 접근과 수정
student = {
    'name': '김철수',
    'age': 20,
    'major': '컴퓨터공학',
    'gpa': 3.7
}

# 1. 대괄호 표기법 (KeyError 위험)
name = student['name']
print(name)

# grade = student['grade']  # KeyError 발생
# print('grade', grade)

# get() 메서드(안전한 접근)
major = student.get('major')
print('major', 'major')

grade1 = student.get('grade')
print('grade1', grade1)

# 기본값 지정
grade2 = student.get('grade', 'N/A')
print('grade2', grade2)

# keys(), values(), items()

print('student.key() : ', list(student.keys()))
print('student.values(): ', list(student.values()))
print('student.items() : ', student.items())


# 값 수정, 추가
student = {
    'name': '김철수',
    'age': 20,
    'major': '컴퓨터공학',
    'gpa': 3.7
}

student['age'] = 23
print('student', student)

student['grade'] = 3
print('student', student)

# update() 메서드로 여러 값 한번에 수정 추가
student.update({
    'gpa': 4.0,
    'city': 'seoul',
    'email': 'a@b.com'
})

print(student)

info_dict = {
    'age': 22,
    'grade': 1,
    'phone': '010-1234-1234'
}

student.update(info_dict)
print('student', student)

# 값 삭제
#   del 키워드
del student['grade']
print('student', student)

# pop(키) 메서드 - 값을 반환하면서 삭제
popped = student.pop('phone')
print(popped)
print('student', student)

# popitem() - 마지막 항목 제거
last_item = student.popitem()
print('last_item', last_item)

# dict 내부 요소 전부 삭제
student.clear()
print('student', student)
