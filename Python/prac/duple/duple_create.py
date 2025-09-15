# 튜플 생성 예제

# 1. 소괄호 사용
my_tuple = (1, 2, 3, 4)
print(my_tuple)  # (1, 2, 3, 4)

# 2. 튜플 생성자 사용
#   list로부터 튜플 생성
from_list_tuple = tuple([1, 2, 3, 4])
print(from_list_tuple)  # (1, 2, 3, 4)

#   *range로부터 튜플 생성
range_tuple = tuple(range(1, 10))
print('type(range_tuple) : ', type(range_tuple))  # <class 'tuple'>
print('range_tuple', range_tuple)  # (1, 2, 3, 4, 5, 6, 7, 8, 9)

# 3. 소괄호 없이 튜플 생성 , 쉼표만 있어도 생성 가능하지만 명확성을 위해 소괄호 사용 권장
no_paren_tuple = 5, 6, 7
print(no_paren_tuple)  # (5, 6, 7)

# 4. 단일 요소 튜플(, 필수!!)
single = (10,)
print('type(single) : ', type(single))  # <class 'tuple'>

single_no_comma = (10)  # <class 'int'> 쉼표 없으면 정수 10 # 주의!!!!
print('type(single2) : ', type(single_no_comma))
