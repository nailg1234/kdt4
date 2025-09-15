# Tuple
# 순서가 있는 불변 시퀀스 자료 구조
# 한번 생성되면 수정할 수 없는 리스트와 유사한 구조
# 여러 개의 값을 하나의 단위로 묶을 때 사용

# 왜 Tuple이 필요한가???
# 변경되면 안되는 데이터 보호
# 리스트 사용 시 -> 실수로 변경 가능...

coordinates_list = [37.345, 126.432]  # 특정 좌표
coordinates_list[0] = 0  # 실수로 변경 가능

# 튜플 사용 시 -> 변경 불가능
coordinates_tuple = (37.345, 126.432)  # 특정 좌표
# coordinates_tuple[0] = 0  # TypeError!!! 발생 -> 변경 불가능

# 특징
# 불변성 : 생성 후 수정 불가능
# 순서 보장 : 인덱스로 접근 가능
# 중복 허용 : 같은 값 여러 번 저장 가능
# 해시 기능 : 딕셔너리 키로 사용 가능
# 메모리 효율적 : 리스트보다 적은 메모리

# 1. 소괄호 사용
empty_tuple = ()
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14, True)
print('mixed : ', mixed)

# 2. 소괄호 없이 생성
numbers2 = 1, 2, 3, 4, 5
print('type : ', type(numbers2))

# 3. tuple() 생성자 사용
from_list = tuple([1, 2, 3, 4])
print('type(from_list) : ', type(from_list))

from_str = tuple("hello")
print('type(from_str) : ', type(from_str))

# 4. 단일 요소 튜플(, 필수!!)
single = (10,)
print('type(single) : ', type(single))

not_tuple = (10)
print('type(not_tuple) : ', type(not_tuple))

# range로 튜플 생성
range_tuple = tuple(range(1, 10))
print('type(range_tuple) : ', type(range_tuple))
print('range_tuple', range_tuple)
print('type(range_tuple)', type(range_tuple))

# tuple 접근과 슬라이싱
fruits = ('사과', '바나나', '수박', '오렌지', '포도')
fruits[1]  # 바나나
fruits[-1]  # 포도
print(fruits[1:3])  # (바나나, 수박)
print(fruits[:2])  # (사과, 바나나)
print(fruits[::-1])  # ('포도', '오렌지', '수박', '바나나', '사과')

# 슬라이싱으로 새 튜플 생성
first_three = fruits[:3]
print(first_three)  # ('사과', '바나나', '수박')
last_two = fruits[-2:]
print(last_two)  # ('오렌지', '포도')
combined = first_three + last_two
print(combined)

# 불변성 확인
numbers = (1, 2, 3, 4, 5, 6)
# numbers[0] = 10  # TypeError 발생
# numbers.append(6) # Error
# del numbers[1] # Error

# 하지만 새 튜플 생성은 가능
new_numbers = numbers + (1, 2)

tuple_with_list = ([1, 2], [3, 4])
tuple_with_list[0].append(3)
print('tuple_with_list : ', tuple_with_list)

# 언패킹(Unpacking)
coordinates = (3, 5)
x, y = coordinates
print(f'x : {x}, y : {y}')

# 직접 언패킹
x, y = (10, 20)
print(f'x : {x}, y : {y}')

# x, y = (10, 20, 30)
# print(f'x : {x}, y : {y}') # ValueError 발생
numbers = (1, 2, 3, 4, 5,)
first, *middle, last = numbers

print(first)
print(middle)
print(last)

print(type(middle))

# 빈 리스트 생성
first, *rest = (1, 2)  # * 붙이면 리스트화
print('first', first)  # 1
print('rest', rest)  # []

# tuple 메서드
numbers = (1, 1, 3, 3, 2, 2, 5, 4, 3)

# 특정 값의 개수
count_2 = numbers.count(2)
print(count_2)

# 특정 값의 인덱스
# 없는 값 검색 시 에러...
index_4 = numbers.index(4)
print(index_4)

# 안전한 검색
value = 10
if value in numbers:
    print(f'{value}의 인덱스 : {numbers.index(value)}')
else:
    print(f'{value}는 튜플에 없습니다.')

# 연산
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

print('tuple1 + tuple2 : ', tuple1 + tuple2)


# 곱셈(반복)
print('tuple1 * 3 : ', tuple1 * 3)

# 비교 연산(앞에서 부터 비교)
tuple1 = (1, 3, 3)
tuple2 = (1, 1, 6)

print(tuple1 < tuple2)
print(tuple1 == tuple2)

# 길이, 최대, 최소, 합
numbers = (1, 2, 3, 4)
print(len(numbers))  # 튜플의 길이
print(max(numbers))  # 요소들중 최대 값
print(min(numbers))  # 요소들중 최소 값
print(sum(numbers))  # 요소들의 합
