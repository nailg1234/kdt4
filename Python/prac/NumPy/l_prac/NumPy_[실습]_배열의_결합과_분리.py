import numpy as np
# 실습2. 배열의 결합과 분리(1)
# 1. 다음 두 배열을 행 방향으로 이어붙이세요.
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
print('문제 1.')
print('행 방향 결합\n', np.vstack([a, b]))
print()

# 2. 아래 배열을 3개로 같은 크기로 분할하세요.
a = np.arange(12)
print('문제 2.')
print(np.split(a, 3))
print()

# 3. 다음 배열들을 새로운 축에 쌓아 shape이 (3, 2)인 배열을 만드세요.
a = np.array([1, 2])
b = np.array([3, 4])
c = np.array([5, 6])
print('문제 3.')
print(np.stack((a, b, c), axis=0))
print(np.stack((a, b, c), axis=0).shape)
print()

# 4. shape가 (2, 3)인 아래 두 배열을 shape (2, 2, 3)인 3차원 배열을 만드세요.
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])
c = np.stack((a, b) , axis = 0)
print('문제 4.')
print('결합 배열\n', c)
print('결합 배열 shape: ', c.shape)
print()

# 5. 아래의 1차원 배열을 2:3:3 비율(총 3개)로 분할하세요.
arr = np.arange(8)
print('문제 5.')
print(np.split(arr, [2, 5]))
print()

# 6. 아래 두 배열을 axis=0, axis=1로 각각 stack하여 두 경우의 결과 shape을 모두 구하세요
a = np.ones((2, 3))
b = np.zeros((2, 3))
print('문제 6.')
print(np.stack((a, b), axis=0))
print(np.stack((a, b), axis=0).shape)
print()
print(np.stack((a, b), axis=1))
print(np.stack((a, b), axis=1).shape)
print()
print(np.stack((a, b), axis=2))
print(np.stack((a, b), axis=2).shape)