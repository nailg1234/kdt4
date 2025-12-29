# 텐서 연산

import torch

# ============================================================
# 산술 연산
# ============================================================

a = torch.tensor([1, 2, 3, 4], dtype=torch.float32)
b = torch.tensor([5, 6, 7, 8], dtype=torch.float32)

# 덧셈
print(f'a + b = {a + b}')
print(f'a + b = {torch.add(a, b)}')

# 뺄셈
print(f'\na - b = {a - b}')
print(f'a - b = {torch.sub(a, b)}')

# 곱셈 (원소별)
print(f'\na * b = {a * b}')
print(f'a * b = {torch.mul(a, b)}')

# 나눗셈
print(f'\na / b = {a / b}')
print(f'a / b = {torch.div(a, b)}')


# ============================================================
# 스칼라 연산
# ============================================================

x = torch.tensor([1, 2, 3, 4], dtype=torch.float32)

print(f'\nx = {x}')
print(f'x + 10 = {x + 10}')
print(f'x - 10 = {x - 10}')
print(f'x * 10 = {x * 10}')
print(f'x ** 2 = {x ** 2}')
print(f'x / 10 = {x / 10}')


# ============================================================
# 제자리 연산 (In-place Operations)
# ============================================================

x = torch.tensor([1, 2, 3, 4], dtype=torch.float32)
print(f'\n원본 x = {x}')

# 제자리 연산 (언더스코어 접미사)
x.add_(10)  # x = x + 10
print(f'x.add_(10) = {x}')

x.mul_(10)  # x = x * 10
print(f'x.mul_(10) = {x}')

# 주의: 자동 미분 중에는 제자리 연산 피하기
# 기울기 계산 시 문제가 발생할 수 있음


# ============================================================
# 수학 함수
# ============================================================

# 절대값
x = torch.tensor([-2, -1, 0, 1, 2], dtype=torch.float32)
print(f'\nabs: {torch.abs(x)}')

# 제곱근 (양수만)
x = torch.tensor([1, 4, 9, 16], dtype=torch.float32)
print(f'\nsqrt: {torch.sqrt(x)}')

# 지수와 로그
x = torch.tensor([1, 2, 3], dtype=torch.float32)
print(f'\nexp: {torch.exp(x)}')
print(f'log: {torch.log(x)}')

# 삼각함수
angles = torch.tensor([0, 3.14159/2, 3.14159])
print(f'\nsin: {torch.sin(angles)}')
print(f'cos: {torch.cos(angles)}')

# 반올림
w = torch.tensor([1.4, 1.5, 1.6])
print(f'\n원본: {w}')
print(f'round: {torch.round(w)}')
print(f'floor: {torch.floor(w)}')
print(f'ceil: {torch.ceil(w)}')
