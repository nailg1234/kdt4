import torch

# 1. 3x3 크기의 0으로 채워진 텐서
zeros = torch.zeros(3, 3)
print(f'1. {zeros}')
print()

# 2. 2x4 크기의 1로 채워진 텐서
ones = torch.ones(2, 4)
print(f'2. {ones}')
print()

# 3. 0부터 9까지의 숫자가 들어있는 1차원 텐서
numbers = torch.arange(0, 10)
print(f'3. {numbers}')
print()

# 4. 평균 0, 표준편차 1인 정규분포에서 샘플링한 5x5 텐서
random_normal = torch.randn(5, 5)
print(f'4. {random_normal}')
print()

# 5. 3x3 단위행렬 (대각선이 1인 행렬)
identity = torch.eye(3)
print(f'5. {identity}')
print()
