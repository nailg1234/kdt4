# ============================================================
# 12월 24일 학습 자료 - 1
# 주제: PyTorch 텐서 연산 (행렬 연산, 브로드캐스팅, 집계)
# ============================================================

import torch
torch.set_printoptions(precision=3)  # 소수점 3자리까지만 표시


# ============================================================
# 1. 행렬 연산
# ============================================================

# 1-1. 행렬 곱셈 (Matrix Multiplication)
A = torch.tensor([
    [1, 2],
    [3, 4],
], dtype=torch.float32)

B = torch.tensor([
    [5, 6],
    [7, 8],
], dtype=torch.float32)

print('=== 행렬 곱셈 ===')
print(f'A @ B:\n{A @ B}')
print(f'torch.mm(A, B):\n{torch.mm(A, B)}')
print(f'torch.matmul(A, B):\n{torch.matmul(A, B)}\n')

# 1-2. 행렬-벡터 곱
matrix = torch.tensor([
    [1, 2, 3],
    [4, 5, 6]
], dtype=torch.float32)

vector = torch.tensor([1, 2, 3], dtype=torch.float32)

print('=== 행렬-벡터 곱 ===')
print(f'행렬 크기: {matrix.shape}')
print(f'벡터 크기: {vector.shape}')

result = torch.mv(matrix, vector)
print(f'결과: {result}')
print(f'결과 크기: {result.shape}\n')

# 1-3. 배치 행렬 곱셈
# 3D 텐서 (배치 행렬): (batch, m, n) @ (batch, n, p) => (batch, m, p)
batch_A = torch.randn(10, 3, 4)  # 10개의 3x4 행렬
batch_B = torch.randn(10, 4, 5)  # 10개의 4x5 행렬

print('=== 배치 행렬 곱셈 ===')
result = torch.bmm(batch_A, batch_B)
print(f'bmm 결과 크기: {result.shape}')

# matmul은 자동으로 배치 처리
result = torch.matmul(batch_A, batch_B)
print(f'matmul 결과 크기: {result.shape}')

# 브로드캐스팅 지원
B = torch.randn(4, 5)
result = torch.matmul(batch_A, B)
print(f'브로드캐스팅 결과 크기: {result.shape}\n')

# 1-4. 전치와 역행렬
A = torch.tensor([
    [1, 2],
    [3, 4]
], dtype=torch.float32)

print('=== 전치와 역행렬 ===')
print(f'원본:\n{A}')
print(f'전치 (A.T):\n{A.T}')
print(f'전치 (transpose):\n{A.transpose(0, 1)}')

# 역행렬
A_inv = torch.inverse(A)
print(f'역행렬:\n{A_inv}')
print(f'A @ A_inv (단위행렬):\n{A @ A_inv}\n')

# ============================================================
# 2. 브로드캐스팅 (Broadcasting)
# ============================================================
# 크기가 다른 텐서 간의 연산 규칙
#
# 규칙:
# 1. 차원이 다르면 작은 쪽에 1을 앞에 추가
# 2. 크기 1인 차원은 다른 텐서에 맞춰 확장
# 3. 크기가 다르고 둘 다 1이 아니라면 에러
#
# 예시:
# (3, 4) + (4,)   => (3, 4) + (1, 4) => (3, 4) ✓
# (3, 1) + (1, 4) => (3, 4) ✓
# (3, 4) + (3,)   => (3, 4) + (1, 3) => 에러 ✗

# 2-1. 1D와 2D 브로드캐스팅
matrix = torch.tensor([
    [1, 2, 3],
    [4, 5, 6],
])

vector = torch.tensor([10, 20, 30])

print('=== 1D와 2D 브로드캐스팅 ===')
print(f'행렬 크기: {matrix.shape}')  # (2, 3)
print(f'벡터 크기: {vector.shape}')  # (3,) => (1, 3)

result = matrix + vector
print(f'결과:\n{result}\n')

# 2-2. 열 벡터와 행 벡터 브로드캐스팅
col_vec = torch.tensor([[1], [2], [3]])  # (3, 1)
row_vec = torch.tensor([10, 20, 30, 40])  # (4,) => (1, 4)

print('=== 열/행 벡터 브로드캐스팅 ===')
print(f'열 벡터 크기: {col_vec.shape}')  # (3, 1) => (3, 4)
print(f'행 벡터 크기: {row_vec.shape}')  # (4,) => (1, 4) => (3, 4)

result = col_vec + row_vec
print(f'결과:\n{result}\n')

# 2-3. 배치 정규화 예제 (브로드캐스팅 활용)
batch = torch.randn(32, 10)  # 32개 샘플, 10개 특성

# 각 특성의 평균과 표준편차 계산
mean = batch.mean(dim=0)  # (10,)
std = batch.std(dim=0)    # (10,)

# 정규화 (브로드캐스팅 활용)
normalized = (batch - mean) / std

print('=== 배치 정규화 (브로드캐스팅 활용) ===')
print(f'배치 크기: {batch.shape}')
print(f'평균 크기: {mean.shape}')
print(f'정규화 후 크기: {normalized.shape}')
print(f'정규화 평균 (≈0): {normalized.mean(dim=0)}')
print(f'정규화 표준편차 (≈1): {normalized.std(dim=0)}\n') 


# ============================================================
# 3. 집계 함수 (Aggregation Functions)
# ============================================================

# 3-1. 전체 집계
x = torch.tensor([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
], dtype=torch.float32)

print('=== 전체 집계 ===')
print(f'합계: {x.sum()}')
print(f'평균: {x.mean()}')
print(f'최솟값: {x.min()}')
print(f'최댓값: {x.max()}')
print(f'표준편차: {x.std()}')
print(f'분산: {x.var()}\n')

# 3-2. 차원별 집계
x = torch.tensor([
    [1, 2, 3],
    [4, 5, 6],
], dtype=torch.float32)

print('=== 차원별 집계 ===')
# dim=0: 행 방향 (세로로 집계)
print(f'dim=0 합계: {x.sum(dim=0)}')
print(f'dim=0 평균: {x.mean(dim=0)}')

# dim=1: 열 방향 (가로로 집계)
print(f'dim=1 합계: {x.sum(dim=1)}')
print(f'dim=1 평균: {x.mean(dim=1)}\n')

# keepdim=True: 차원 유지
print('=== keepdim=True (차원 유지) ===')
print(f'dim=0 합계: {x.sum(dim=0, keepdim=True)}')
print(f'dim=1 합계: {x.sum(dim=1, keepdim=True)}\n')
# 3-3. argmax와 argmin (최대/최소 위치 찾기)
x = torch.tensor([
    [3, 2, 3],
    [9, 7, 0],
], dtype=torch.float32)

print('=== argmax와 argmin ===')
print(f'전체 argmax: {x.argmax()}')
print(f'전체 argmin: {x.argmin()}')
print(f'dim=0 argmax: {x.argmax(dim=0)}')
print(f'dim=1 argmax: {x.argmax(dim=1)}\n')


# ============================================================
# 4. 텐서 결합 (Concatenation & Stacking)
# ============================================================

# 4-1. cat (같은 차원에서 결합)
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[5, 6], [7, 8]])

print('=== cat (결합) ===')
# dim=0: 행 방향 결합 (아래로)
cat0 = torch.cat([a, b], dim=0)
print(f'cat dim=0:\n{cat0}')

# dim=1: 열 방향 결합 (옆으로)
cat1 = torch.cat([a, b], dim=1)
print(f'cat dim=1:\n{cat1}\n')

# 4-2. stack (새 차원 추가하며 결합)
a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])
c = torch.tensor([7, 8, 9])

print('=== stack (새 차원 추가) ===')
stacked0 = torch.stack([a, b, c], dim=0)
print(f'stacked dim=0:\n{stacked0}')

stacked1 = torch.stack([a, b, c], dim=1)
print(f'stacked dim=1:\n{stacked1}\n')

# 4-3. split과 chunk (분할)
x = torch.arange(12).reshape(3, 4)

print('=== split (지정 크기로 분할) ===')
splits = torch.split(x, 2, dim=1)  # 열 방향 2개씩
for i, s in enumerate(splits):
    print(f'{i}: shape={s.shape}, data=\n{s}')

print('\n=== chunk (지정 개수로 분할) ===')
chunks = torch.chunk(x, 3, dim=0)  # 행 방향 3등분
for i, c in enumerate(chunks):
    print(f'{i}: shape={c.shape}, data=\n{c}')


# ============================================================
# 5. 비교 연산 (Comparison Operations)
# ============================================================

a = torch.tensor([1, 2, 3, 4])
b = torch.tensor([2, 2, 2, 2])

print('\n=== 비교 연산 ===')
print(f'a > b: {a > b}')
print(f'a >= b: {a >= b}')
print(f'a == b: {a == b}')
print(f'a != b: {a != b}')

print('\n=== torch 함수 ===')
print(f'torch.gt(a, b): {torch.gt(a, b)}')
print(f'torch.eq(a, b): {torch.eq(a, b)}')

print('\n=== 조건 검사 ===')
print(f'전부 같음: {torch.all(a == b)}')
print(f'하나라도 같음: {torch.any(a == b)}')