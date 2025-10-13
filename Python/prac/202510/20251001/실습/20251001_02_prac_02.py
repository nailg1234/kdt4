# 실습2. 배열의 결합과 분리(1)
import numpy as np

# 1. 다음 두 배열을 행 방향으로 이어붙이세요.
a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6]])
concat_arr = np.concatenate((a, b), axis = 0)
print('문제 1.')
print('이어 붙인 배열 : \n', concat_arr)
print()

# 2. 아래 배열을 3개로 같은 크기로 분할하세요.
a = np.arange(12)
split_a = np.split(a, 3)
print('문제 2.')
print('분할한 배열')
for arr in split_a:
    print(arr)

# 3. 다음 배열들을 새로운 축에 쌓아 shape이 (3, 2)인 배열을 만드세요.
a = np.array([1, 2])
b = np.array([3, 4])
c = np.array([5, 6])
stack = np.stack((a, b, c), axis = 0)
print('문제 3.')
print(stack)
print(stack.shape)
print()

# 4. shape가 (2, 3)인 아래 두 배열을 shape (2, 2, 3)인 3차원 배열을 만드세요.
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([[7, 8, 9],
              [10, 11, 12]])
stack = np.stack((a, b), axis = 0)
print('문제 4.')
print(stack)
print(stack.shape)

# 5. 아래의 1차원 배열을 2:3:3 비율(총 3개)로 분할하세요.
arr = np.arange(8)
split_arr = np.split(arr, [2, 5], axis = 0)
print('문제 5.')
for _arr in split_arr:
    print(_arr)
print()

# 6. 아래 두 배열을 axis=0, axis=1로 각각 stack하여 두 경우의 결과 shape을 모두 구하세요
a = np.ones((2, 3))
b = np.zeros((2, 3))

stack0 = np.stack((a, b), axis = 0)
stack1 = np.stack((a, b), axis = 1)
print('문제 6.')
print(stack0)
print(stack0.shape)
print()
print(stack1)
print(stack1.shape)