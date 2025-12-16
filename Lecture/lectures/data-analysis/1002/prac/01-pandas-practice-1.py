import numpy as np


# 실습1. 배열 형태 변형, 차원 확장·축소(1)
# 1. 아래의 배열을 사용해서
# · arr = np.array([[10, 20], [30, 40], [50, 60]])
# ravel과 flatten을 각각 사용해 1차원 배열로 변환하고,
# arr의 첫 번째 원소(arr[0, 0])를 999로 바꾼 뒤 ravel 결과와 flatten 결과에 어떤 변화가 있는지 확인하 →
arr = np.array([[10, 20], [30, 40], [50, 60]])

# 1차원 변환
r1 = arr.ravel()
f1 = arr.flatten()
print('ravel : ', r1)
print('flatten :', f1)
print()

arr[0, 0] = 999
print('ravel : ', r1)  # ravel은 원본과 연결 -> 같이 변환
print('flatten :', f1)  # flatten은 복사본 -> 그대로 유지
print()
# 2. 크기가 32×32인 이미지 데이터를 가정하고,
#  이 배열에 대해 expand_dims를 사용하여
# shape(1, 32, 32)로 바꾸는 코드를 작성하세요.
# · img = np.random.rand(32, 32)
img = np.random.rand(32, 32)
img_expanded = np.expand_dims(img, axis=0)
print('img_expanded', img_expanded.shape)
print()

# 3.아래 배열에서 불필요한 1차원을 모두 제거하여 shape이 (28, 28)이 되도록 만드세요.
# · img = np.random.randint(0, 255, (1, 28, 28, 1))
img = np.random.randint(0, 255, (1, 28, 28, 1))

img_squeezed = np.squeeze(img, axis=None)
print('img_squeezed', img_squeezed.shape)
print()

# 4.아래 2차원 배열을 1)
# 1차원 배열로 만든 후
# 2) 중복값을 제거한 뒤 shape (1, n)으로 재구상 하세요.
# · arr = np.array([[3, 1, 2, 2],
# [1, 2, 3, 1],
# [2, 2, 1, 4]])
arr = np.array([[3, 1, 2, 2],
                [1, 2, 3, 1],
                [2, 2, 1, 4]])
# 평탄화 => 1차원 변환
flat = arr.flatten()

# 중복 제거
unique = np.unique(flat)

# (1,n) 형태로 변환
reshaped = unique.reshape(1, -1)

print('원본', arr)
print('1차원', flat)
print('중복 제거', unique)
print('(1,n) 형태', reshaped.shape)
print('최종 형태', reshaped)
print()


# 실습2. 배열의 결합과 분리(1)

# 1. 다음 두 배열을 행 방향으로 이어붙이세요.
# · a = np.array([[1, 2], [3, 4]])
# · b = np.array([[5, 6]])

a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6]])

result = np.vstack((a, b))
print('result', result)
print()

# 2. 아래 배열을 3개로 같은 크기로 분할하세요.
# · a = np.arange(12)
a = np.arange(12)
result = np.split(a, 3)
print('result', result)
print()

# 3. 다음 배열들을 새로운 축에 쌓아 shape이 (3, 2)인 배열을 만드세요.
# · a = np.array([1, 2])
# . b = np.array([3, 4])
# · c = np.array([5, 6])
a = np.array([1, 2])
b = np.array([3, 4])
c = np.array([5, 6])

result = np.stack((a, b, c), axis=0)
print('result\n', result)
print()

# 4. shape가 (2, 3)인 아래 두 배열을 shape (2, 2, 3)인 3차원 배열을 만드세요.
# · a = np.array([[1, 2, 3], [4, 5, 6]])
# · b = np.array([[7, 8, 9], [10, 11, 12]])
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])

result = np.stack((a, b), axis=0)
print('result\n', result)
print()


# 5. 아래의 1차원 배열을 2:3:3 비율(총 3개)로 분할하세요.
# · arr = np.arange(8)
arr = np.arange(8)
result = np.split(arr, [2, 5])
print('result\n', result)
print()

# 6. 아래 두 배열을 axis=0, axis=1로 각각 stack하여
#  두 경우의 결과 shape을 모두 구하세요
# · a = np.ones((2, 3))
# · b = np.zeros((2, 3))
a = np.ones((2, 3))
b = np.zeros((2, 3))

# 위아래로 쌓음ㅅ
result0 = np.stack((a, b), axis=0)

print('result0\n', result0)  # (2,2,3)
print()

# 옆으로 쌓음
result1 = np.stack((a, b), axis=1)
print('result1\n', result1)  # (2,2,3)
print()

# 1. 다음 배열을 생성하고, 모든 요소에 3을 더하세요.
# . arr = np.array([1, 2, 3, 4])
arr = np.array([1, 2, 3, 4])
result = arr + 3
print('result\n', result)
print()

# 2. 아래 2차원 배열에서 각 요소를 - 1로 곱한 새로운 배열을 만드세요.
# · arr = np.array([[5, 10],
#                   [15, 20]])
arr = np.array([[5, 10],
                [15, 20]])
result = arr * -1
print('arr\n', arr)
print('result\n', result)
print()


# 3. 아래 두 배열의 요소별 곱셈과 나눗셈 결과를 각각 출력하세요.
# · arr1 = np.array([2, 4, 6])
# · arr2 = np.array([1, 2, 3])
arr1 = np.array([2, 4, 6])
arr2 = np.array([1, 2, 3])

mul1 = arr1 * arr2
div1 = arr1 / arr2
print('mul1\n', mul1)
print('div1\n', div1)
print()


# 4. 아래 배열에서 모든 요소를 최대값 100으로 만들기 위해
# 필요한 값을 더한 결과 배열을 브로드 캐스팅으로 만드세요.
# · arr = np.array([[95, 97],
#                   [80, 85]])
arr = np.array([[95, 97],
                [80, 85]])

add_val = 100 - arr
print('add_val\n', add_val)
result = arr + add_val
print('result\n', result)
print()

# 5. 아래 2차원 배열에서 각 행에 다른 값을 곱하여 새로운 배열을 만드세요.(브로드캐스팅 이용)
# · arr = np.array([[1, 2, 3], [4, 5, 6]])
# • 첫 번째 행은 10을 곱하고
# • 두 번째 행은 100을 곱해야 합니다.
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

mul_val = np.array([[10], [100]])
result = arr * mul_val
print('result\n', result)
print()

# 6. 아래 배열에서 각 행마다 다른 스칼라 값을 더하기 위해
# • 1차원 배열을 만들어 브로드캐스팅 연산을 수행하세요.
# • 첫 번째 행에 100, 두 번째 행에 200, 세 번째 행에 300을 더하세요.
# · arr = np.array([[10, 20],
# [30, 40],
# [50, 60]])
arr = np.array([[10, 20],
                [30, 40],
                [50, 60]])

add_val = np.array([100, 200, 300])
reshaped = add_val.reshape(-1, 1)
result = arr + reshaped
print('result\n', result)
print()

print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
