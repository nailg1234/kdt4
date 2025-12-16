# 실습1. 배열 초기화 및 생성(1)
import numpy as np

# 1. 0으로 채워진 크기 (3, 4) 배열을 생성한 후, 모든 값을 5로 채우는 새로운 배열을 만드세요.
result = np.zeros((3, 4))
result[:, :] = 5
print('문제 1.')
print(result)
print()

# 2. 0부터 20까지 2씩 증가하는 1차원 배열을 생성하세요.
result = np.arange(0, 21, 2)
print('문제 2.')
print(result)
print()

# 3. 0~1 사이의 실수 난수를 가지는 (2, 3) 크기의 배열을 생성하세요.
result = np.random.rand(2, 3)
print('문제 3.')
print(result)
print()

# 4. 평균이 100, 표준편차가 20인 정규분포 난수 6개를 생성하세요.
result = np.random.normal(loc=100, scale=20, size=6)
print('문제 4.')
print(result)
print()

# 5. 1부터 20까지의 정수를 포함하는 1차원 배열을 만들고, 이 배열을 (4, 5) 크기의 2차원 배열로 변환하세요.
result = np.arange(1, 21).reshape(4, 5)
print('문제 5.')
print(result)
print()

# 6. 0부터 1까지 균등 간격으로 나눈 12개의 값을 가지는 배열을 생성하고, 이를 (3, 4) 크기로 변환하세요.
result = np.linspace(0, 1, 12).reshape(3, 4)
print('문제 6.')
print(result)
print()

# 7. 0~99 사이의 난수로 이루어진 (10, 10) 배열을 생성한 뒤, np.eye()로 만든 단위 행렬을 더
# 하여 대각선 요소가 1씩 증가된 배열을 만드세요.

result = np.random.randint(0, 100, size=(10, 10))
print('문제 7.')
print('원본 \n', result)
eye1 = np.eye(10)
print('eye1 \n', eye1)
print('증가된 배열 \n', result + eye1)
print()

# 8. 0~9 사이의 난수로 이루어진 (2, 3, 4) 3차원 배열을 생성하세요.
result = np.random.randint(0, 10, size=(2, 3, 4))
print('문제 8.')
print(result)