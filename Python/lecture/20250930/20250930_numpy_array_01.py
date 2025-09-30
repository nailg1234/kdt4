# 배열 모양 변경, 조작

import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5, 6])
print('===== 1 차원 =====')
print('shape', arr_1d.shape)  # (6,) # 모양
print('ndim', arr_1d.ndim)  # 1 # 차원
print('size', arr_1d.size)  # 6 # 사이즈
print(arr_1d.reshape(3, -1))  # -1은 자동으로 채워짐 2로

print('===== 2 차원 =====')
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print('shape', arr_2d.shape)  # (2, 3) # 모양
print('ndim', arr_2d.ndim)  # 2 # 차원
print('size', arr_2d.size)  # 6 # 사이즈

# 기본 산술 연산
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 4, 3, 2, 1])

print('배열 a : ', a)
print('배열 b : ', b)

print('덧셈 (a + b) : ', a + b)
print('뺄셈 (a - b) : ', a - b)
print('곱셈 (a * b) : ', a * b)
print('거듭제곱 (a ** b): \n', a ** b)
print('나눗셈 (a / b) : ', a / b)
print('몫 (a // b): ', a // b)
print('나머지 (a % b) : ', a % b)

# 스칼라 연산
a = np.array([1, 2, 3, 4, 5])
scalar = 10
print('+ 스칼라', a + scalar)
print('- 스칼라', a - scalar)
print('* 스칼라', a * scalar)
print('/ 스칼라', a / scalar)
print('스칼라 / 배열', scalar / a)

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

B = np.array([
    [7, 8, 9],
    [10, 11, 12]
])

print('행렬 A\n', A)
print('행렬 B\n', B)

print('행렬 A + B\n', A + B)
print('행렬 A * B\n', A * B)
print('행렬 A / B\n', A / B)

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [7, 8],
    [9, 10]
])

print('행렬 곱', A @ B)

# 브로드 캐스팅 (Broadcasting)
# 서로 다른 모양의 배열 간 연산을 가능하게 하는 Numpy 기능
arr = np.array([1, 2, 3, 4, 5])
scalar = 10

# 스칼라가 자동으로 배열 크기로 "브로드캐스트" 됨
[1, 2, 3, 4, 5] + [10, 10, 10, 10, 10]

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

vector = np.array([10, 20, 30])

print(matrix + vector)

'''
[                          [
    [1, 2, 3],                  [10, 20, 30],
    [4, 5, 6],      +           [10, 20, 30],
    [7, 8, 9]                   [10, 20, 30]
]                           }

'''

# 브로드캐스팅 규칙
# 규칙 1: 차원 수가 다르면 작은 쪽의 앞에 1을 추가
# (3, 3) + (3, ) -> (1, 3)

# 규칙 2: 각 차원에서 크기가 1이거나 같아야 함
# 호환 가능 : (3, 1) & (1, 4) = (3, 4)
# 호환 불가 : (3, 2) & (4, 2) 에러!....

a = np.ones((3, 1))
b = np.ones((4, 2))

print(a + b)
