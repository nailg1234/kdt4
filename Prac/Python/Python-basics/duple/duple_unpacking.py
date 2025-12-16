# 튜플 언패킹
coordinates = (3, 5)
x, y = coordinates
print(f'x : {x}, y : {y}')  # x : 3, y : 5

# 직접 언패킹
x, y = (10, 20)
print(f'x : {x}, y : {y}')  # x : 10, y : 20

# x, y = (10, 20, 30)  # ValueError: too many values to unpack (expected 2)

numbers = (1, 2, 3, 4, 5,)
first, *middle, last = numbers
# first : 1, middle : [2, 3, 4], last : 5
print(f'first : {first}, middle : {middle}, last : {last}')

numbers = (1, 2, 3, 4, 5,)
first, *middle, last = numbers

print(first)  # 1
print(middle)  # [2, 3, 4] * 붙은거 -> 리스트
print(last)  # 5

print(type(middle))

# 빈 리스트 생성
first, second, *rest = (1, 2)  # * 붙이면 리스트화
print('first', first)  # 1
print('second', second)  # 2
print('rest', rest)  # []
