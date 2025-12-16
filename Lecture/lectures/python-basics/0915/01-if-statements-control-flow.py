# ==========================================
# Python 튜플(Tuple) 완전 가이드
# ==========================================

# 튜플이란?
# - 순서가 있는 불변 시퀀스 자료 구조
# - 한 번 생성되면 수정할 수 없는 리스트와 유사한 구조
# - 여러 개의 값을 하나의 단위로 묶을 때 사용

print("=" * 50)
print("1. 튜플이 필요한 이유")
print("=" * 50)

# 왜 튜플이 필요한가?
# 1) 변경되면 안되는 데이터 보호
# 2) 실수로 인한 데이터 변경 방지

# 리스트 사용 시 - 실수로 변경 가능
coordinates_list = [37.345, 126.432]  # GPS 좌표를 리스트로 저장
print(f"원본 좌표: {coordinates_list}")

coordinates_list[0] = 0  # 실수로 좌표가 변경됨!
print(f"변경된 좌표: {coordinates_list} (문제 발생!)")

# 튜플 사용시 - 변경 불가능
coordinates_tuple = (37.345, 126.432)  # GPS 좌표를 튜플로 저장
print(f"튜플 좌표: {coordinates_tuple}")

# coordinates_tuple[0] = 0  # TypeError 발생! 변경 불가능
# 위 코드의 주석을 해제하면 에러가 발생합니다.

print("\n" + "=" * 50)
print("2. 튜플의 특징")
print("=" * 50)

# 튜플의 주요 특징들:
# 1. 불변성(Immutability): 생성 후 수정 불가능
# 2. 순서 보장(Ordered): 인덱스로 접근 가능
# 3. 중복 허용(Allow Duplicates): 같은 값 여러 번 저장 가능
# 4. 해시 가능(Hashable): 딕셔너리 키로 사용 가능
# 5. 메모리 효율적: 리스트보다 적은 메모리 사용

# 예시로 특징 확인
sample_tuple = (1, 2, 2, 3, 2)  # 중복 허용
print(f"중복 허용 예시: {sample_tuple}")
print(f"인덱스 접근: {sample_tuple[1]}")  # 순서 보장

print("\n" + "=" * 50)
print("3. 튜플 생성 방법들")
print("=" * 50)

# 방법 1: 소괄호 사용 (가장 일반적)
empty_tuple = ()  # 빈 튜플
numbers = (1, 2, 3, 4, 5)  # 숫자 튜플
mixed = ("hello", 1, True, 3.14)  # 다양한 타입 혼합 (마지막 콤마는 선택사항)
print(f'혼합 튜플: {mixed}')

# 방법 2: 소괄호 없이 생성 (콤마로 구분)
numbers2 = 1, 2, 3, 4, 5  # 소괄호 생략 가능
print(f'numbers2의 타입: {type(numbers2)}')  # <class 'tuple'>

# 방법 3: tuple() 생성자 사용
from_list = tuple([1, 2, 3, 4])  # 리스트를 튜플로 변환
print(f'리스트에서 변환된 튜플 타입: {type(from_list)}')

from_str = tuple("hello")  # 문자열을 문자 튜플로 변환
print(f'문자열에서 변환된 튜플: {from_str}')
print(f'문자열 튜플 타입: {type(from_str)}')

# 방법 4: 단일 요소 튜플 (콤마 필수!)
single = (10,)  # 콤마가 있어야 튜플
print(f'단일 요소 튜플 타입: {type(single)}')

not_tuple = (10)  # 콤마가 없으면 그냥 정수
print(f'콤마 없는 경우 타입: {type(not_tuple)}')  # <class 'int'>

# 방법 5: range로 튜플 생성
range_tuple = tuple(range(1, 10))  # 1부터 9까지의 숫자 튜플
print(f'range 튜플 타입: {type(range_tuple)}')
print(f'range 튜플 내용: {range_tuple}')

print("\n" + "=" * 50)
print("4. 튜플 접근과 슬라이싱")
print("=" * 50)

fruits = ('사과', '바나나', '수박', '오렌지', '포도')

# 인덱스를 통한 개별 접근
print(f"두 번째 과일: {fruits[1]}")  # 바나나 (인덱스는 0부터 시작)
print(f"마지막 과일: {fruits[-1]}")  # 포도 (음수 인덱스는 뒤에서부터)

# 슬라이싱을 통한 부분 추출
print(f"2-3번째 과일: {fruits[1:3]}")  # ('바나나', '수박') - 끝 인덱스 미포함
print(f"처음 2개 과일: {fruits[:2]}")  # ('사과', '바나나')
print(f"역순 정렬: {fruits[::-1]}")  # 튜플을 뒤집어서 출력

# 슬라이싱으로 새 튜플 생성
first_two = fruits[:2]  # 처음 2개
last_two = fruits[-2:]  # 마지막 2개
print(f'마지막 2개: {last_two}')

# 튜플 연결 (새로운 튜플 생성)
combined = first_two + last_two
print(f'연결된 튜플: {combined}')

print("\n" + "=" * 50)
print("5. 불변성 확인")
print("=" * 50)

numbers = (1, 2, 3, 4, 5, 6)

# 아래 모든 수정 시도들은 에러를 발생시킵니다:
# numbers[0] = 10        # TypeError: 'tuple' object does not support item assignment
# numbers.append(6)      # AttributeError: 'tuple' object has no attribute 'append'
# del numbers[1]         # TypeError: 'tuple' object doesn't support item deletion

print("튜플은 수정할 수 없지만, 새로운 튜플 생성은 가능합니다:")

# 하지만 새 튜플 생성은 가능
new_numbers = numbers + (7, 8)  # 기존 튜플과 새 튜플을 연결
print(f"새로 생성된 튜플: {new_numbers}")

# 주의: 튜플 내부의 가변 객체는 수정 가능
tuple_with_list = ([1, 2], [3, 4])  # 리스트를 포함한 튜플
print(f"수정 전: {tuple_with_list}")

tuple_with_list[0].append(3)  # 튜플 내부의 리스트는 수정 가능
print(f'수정 후: {tuple_with_list}')

# 하지만 리스트 자체를 바꾸는 것은 불가능
# tuple_with_list[0] = [2, 3]  # TypeError 발생!

print("\n" + "=" * 50)
print("6. 언패킹(Unpacking)")
print("=" * 50)

# 기본 언패킹
coordinates = (3, 5)
x, y = coordinates  # 튜플의 값들을 개별 변수에 할당
print(f'좌표 x: {x}, y: {y}')

# 직접 언패킹
x, y = (10, 20)  # 튜플을 바로 언패킹
print(f'새 좌표 x: {x}, y: {y}')

x = 30  # x 값만 변경 (y는 그대로)
print(f'x 변경 후 - x: {x}, y: {y}')

# 값의 개수가 맞지 않으면 에러 발생
# x, y = (10, 20, 30)  # ValueError: too many values to unpack

# 확장 언패킹 (Python 3+)
numbers = (1, 2, 3, 4, 5, 6, 7, 8)
first, *middle, last = numbers  # *를 사용해 중간 값들을 리스트로 수집
print(f'첫 번째: {first}')
print(f'중간 값들: {middle}')  # 리스트로 저장됨
print(f'마지막: {last}')

# 하나의 요소만 있는 경우
first, *rest = (1,)
print(f'첫 번째: {first}')  # 1
print(f'나머지: {rest}')    # [] (빈 리스트)

print("\n" + "=" * 50)
print("7. 튜플 메서드")
print("=" * 50)

numbers = (1, 1, 3, 3, 2, 2, 5, 4, 3)

# count() - 특정 값의 개수 세기
count_2 = numbers.count(2)
print(f'숫자 2의 개수: {count_2}')

count_3 = numbers.count(3)
print(f'숫자 3의 개수: {count_3}')

# index() - 특정 값의 첫 번째 인덱스 찾기
index_4 = numbers.index(4)
print(f'숫자 4의 인덱스: {index_4}')

# 없는 값 검색 시 에러가 발생하므로 안전한 검색 방법
value_to_find = 10
if value_to_find in numbers:
    print(f'{value_to_find}의 인덱스: {numbers.index(value_to_find)}')
else:
    print(f'{value_to_find}는 튜플에 없습니다.')

print("\n" + "=" * 50)
print("8. 튜플 연산")
print("=" * 50)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# 연결 연산 (+)
print(f'튜플 연결: {tuple1 + tuple2}')

# 반복 연산 (*)
print(f'튜플 반복: {tuple1 * 3}')

# 비교 연산 (사전식 순서로 비교)
tuple1 = (1, 3, 3)
tuple2 = (2, 2, 4)

print(f'{tuple1} < {tuple2}: {tuple1 < tuple2}')  # 첫 번째 요소부터 비교
print(f'{tuple1} == {tuple2}: {tuple1 == tuple2}')

# 멤버십 연산
print(f'1이 tuple1에 있는가?: {1 in tuple1}')
print(f'10이 tuple1에 없는가?: {10 not in tuple1}')

print("\n" + "=" * 50)
print("9. 튜플 내장 함수들")
print("=" * 50)

numbers = (1, 2, 3, 4, 5)

# 기본 통계 함수들
print(f'튜플 길이 (요소 개수): {len(numbers)}')
print(f'최댓값: {max(numbers)}')
print(f'최솟값: {min(numbers)}')
print(f'모든 요소의 합: {sum(numbers)}')

# 정렬 (새로운 리스트 반환)
mixed_numbers = (3, 1, 4, 1, 5, 9, 2, 6)
print(f'원본 튜플: {mixed_numbers}')
print(f'정렬된 리스트: {sorted(mixed_numbers)}')
print(f'역순 정렬: {sorted(mixed_numbers, reverse=True)}')

print("\n" + "=" * 50)
print("10. 실용적인 튜플 활용 예시")
print("=" * 50)

# 1) 함수에서 여러 값 반환


def get_name_age():
    """이름과 나이를 튜플로 반환"""
    return "김철수", 25


name, age = get_name_age()  # 언패킹으로 받기
print(f"이름: {name}, 나이: {age}")

# 2) 딕셔너리의 키로 사용 (해시 가능하므로)
locations = {
    (37.5665, 126.9780): "서울",
    (35.1796, 129.0756): "부산",
    (37.4563, 126.7052): "인천"
}
seoul_coords = (37.5665, 126.9780)
print(f"좌표 {seoul_coords}의 도시: {locations[seoul_coords]}")

# 3) 설정값이나 상수 저장
RGB_RED = (255, 0, 0)
RGB_GREEN = (0, 255, 0)
RGB_BLUE = (0, 0, 255)

print(f"빨간색 RGB: {RGB_RED}")

# 4) 데이터베이스 레코드 표현
student_record = ("김학생", 20, "컴퓨터공학과", 3.8)
name, age, major, gpa = student_record
print(f"학생 정보 - 이름: {name}, 나이: {age}, 전공: {major}, 학점: {gpa}")

print("\n" + "=" * 50)
print("튜플 vs 리스트 비교")
print("=" * 50)

print("튜플 사용이 좋은 경우:")
print("- 데이터가 변경되지 않아야 할 때")
print("- 딕셔너리의 키로 사용할 때")
print("- 함수의 반환값이 여러 개일 때")
print("- 설정값이나 상수를 저장할 때")
print("- 메모리 효율이 중요할 때")

print("\n리스트 사용이 좋은 경우:")
print("- 데이터를 자주 수정해야 할 때")
print("- 요소를 추가/삭제해야 할 때")
print("- 정렬이나 뒤섞기 등의 연산이 필요할 때")
