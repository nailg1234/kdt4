import numpy as np

# 다음 벡터 연산을 수행하세요

a = np.array([2, 4, 6])
b = np.array([1, 3, 5])

# 1. a + b 계산
print(a + b)
# 2. a - b 계산
print(a - b)
# 3. a * 3 계산
print(a * 3)
# 4. a의 크기(노름) 계산
a_norm = np.linalg.norm(a)
print(a_norm)
# 5. a의 단위 벡터 구하기
print(a / a_norm)
