import torch

# 두 행렬 정의
A = torch.tensor([[1, 2, 3],
                  [4, 5, 6]], dtype=torch.float32)

B = torch.tensor([[2, 0, 1],
                  [1, 3, 2]], dtype=torch.float32)

print(f"A:\n{A}\n")
print(f"B:\n{B}\n")

# 1. A와 B의 원소별 합
element_sum = A + B
print(f'1. {element_sum}')
print()

# 2. A와 B의 원소별 곱
element_mul = A * B
print(f'2. {element_mul}')
print()

# 3. A의 모든 원소를 제곱
squared = A ** 2
print(f'3. {squared}')
print()

# 4. A의 각 행의 합 (결과:[6, 15])
row_sum = torch.sum(A, axis=1)
print(f'4. {row_sum}')
print()

# 5. A의 각 열의 평균 (결과:[2.5, 3.5, 4.5])
col_mean = torch.mean(A, axis=0)
print(f'5. {col_mean}')
print()


# 6. A에서 3보다 큰 원소들만 추출
greater_than_3 = A[A > 3]
print(f'6. {greater_than_3}')
print()
