import numpy as np

A = np.array([[1, 2], [3, 4], [5, 6]])
B = np.array([[1, 2, 3], [4, 5, 6]])

# 1. A의 shape 확인
print(A.shape)
# 2. A의 전치 행렬 구하기
print(A.transpose())
# 3. A @ B 계산하기 (가능한지 먼저 확인!)
print(np.matmul(A, B))
# 4. B @ A 계산하기
print(np.dot(B, A))
# 5. np.arange(12)를 3x4 행렬로 reshape
print(np.arange(12).reshape(3, 4))
