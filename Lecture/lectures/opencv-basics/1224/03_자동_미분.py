# ============================================================
# 12월 24일 학습 자료 - 3
# 주제: PyTorch 자동 미분 (Autograd)
# ============================================================

# 자동 미분 (Automatic Differentiation)
# = 수치적 미분 없이 정확한 기울기를 자동으로 계산하는 기법
#
# 딥러닝에서 필요한 이유:
# 1. 역전파 알고리즘의 핵심 기술
# 2. 수동 미분은 복잡하고 오류 발생 가능 (실수하기 쉬움)
# 3. 수치 미분은 느리고 부정확 (근사값이라 오차 발생)
#
# PyTorch의 Autograd:
# - 연산을 기록 (계산 그래프 자동 생성)
# - 연쇄 법칙으로 기울기 자동 계산
# - backward() 한 번 호출로 모든 파라미터의 기울기 계산

import torch



# ============================================================
# 1. 자동 미분 기본 예제
# ============================================================

# 함수: y = x² + 2x + 1
# 미분: dy/dx = 2x + 2

print("="*50)
print("1. 자동 미분 기본 예제")
print("="*50)

x = 3.0
# 수동 미분 (손으로 계산)
manual_grad = 2 * x + 2

# PyTorch 자동 미분
x_tensor = torch.tensor(x, requires_grad=True)  # 기울기 추적 활성화
y = x_tensor ** 2 + 2 * x_tensor + 1
y.backward()  # 역전파로 기울기 계산
auto_grad = x_tensor.grad

print(f'수동 미분 결과: {manual_grad}')
print(f'자동 미분 결과: {auto_grad}')
print()


# ============================================================
# 2. requires_grad - 기울기 추적 관리
# ============================================================

print("="*50)
print("2. requires_grad - 기울기 추적")
print("="*50)

# requires_grad=True: 이 텐서의 모든 연산을 추적
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
print(f'x: {x}')
print(f'requires_grad: {x.requires_grad}')

# requires_grad=False (기본값): 기울기 계산 안 함
y = torch.tensor([1.0, 2.0, 3.0])
print(f'\ny: {y}')
print(f'requires_grad: {y.requires_grad}')

# 나중에 활성화 가능 (in-place 연산)
y.requires_grad_(True)
print(f'활성화 후 requires_grad: {y.requires_grad}')

# 연산 결과의 requires_grad 자동 전파
# 규칙: 하나라도 True면 결과도 True
a = torch.tensor([1.0], requires_grad=True)
b = torch.tensor([2.0], requires_grad=True)
c = torch.tensor([3.0])  # False

d = a + b  # True + True = True
e = a + c  # True + False = True
f = b + c  # True + False = True

print(f'\na + b requires_grad: {d.requires_grad}')
print(f'a + c requires_grad: {e.requires_grad}')
print(f'b + c requires_grad: {f.requires_grad}')
print()


# ============================================================
# 3. 실전 예제: 간단한 학습 과정
# ============================================================

print("="*50)
print("3. 실전 예제: 간단한 학습")
print("="*50)

# 신경망 학습의 핵심:
# 1. 예측값 계산 (순전파)
# 2. 손실 계산 (얼마나 틀렸나?)
# 3. 가중치 조정 (어느 방향으로 얼마나?) ← 여기서 미분 필요!

# 시나리오: y = w * x 모델 학습
# 손실 함수: L = (w*x - y)²
# 목표: w의 최적값 찾기 → dL/dw를 계산해서 w 업데이트!

x = 2.0
y = 5.0  # 정답 (타겟)
w = torch.tensor(1.0, requires_grad=True)  # 가중치 (초기값)

# 순전파
pred = w * x
loss = (pred - y) ** 2

print(f"예측: {pred.item():.2f}, 정답: {y}")
print(f"손실: {loss.item():.2f}")

# 역전파 - 자동으로 dL/dw 계산!
loss.backward()
print(f"기울기 dL/dw: {w.grad.item():.2f}")

# 해석:
# 기울기가 음수(-12) → w를 증가시켜야 손실 감소
# w를 1.0에서 증가시키면 예측값이 정답에 가까워짐

print("\n[왜 자동 미분이 필수인가?]")
print("간단한 경우: L = (wx - y)²")
print("  → dL/dw = 2(wx - y) * x  ← 손으로 계산 가능!")

import torch.nn as nn

model = nn.Sequential(
    nn.Linear(784, 512),   # 401,920 파라미터
    nn.ReLU(),
    nn.Linear(512, 256),   # 131,328 파라미터
    nn.ReLU(),
    nn.Linear(256, 10),    # 2,570 파라미터
)

print("\n복잡한 신경망:")
total_params = sum(p.numel() for p in model.parameters())
print(f"  → 총 {total_params:,}개의 파라미터!")
print("  → 각각의 기울기를 손으로 계산??? 불가능!")

print("\n자동 미분의 장점:")
print("  ✓ 정확: 수치 오차 없음")
print("  ✓ 빠름: 최적화된 C++ 코드")
print("  ✓ 자동: 실수 없음")
print("  ✓ 복잡한 모델도 동일한 방식")
print()



# ============================================================
# 4. 계산 그래프 (Computational Graph)
# ============================================================

print("="*50)
print("4. 계산 그래프")
print("="*50)

# 계산 그래프 = 연산의 흐름을 기록하는 그래프
# PyTorch는 연산을 수행하면서 자동으로 그래프를 생성

# 예시: z = (x + y) * (x - y)
#
# 계산 그래프:
#     x(2)   y(3)
#      |  \  /  |
#      |   \/   |
#      |   /\   |
#      |  /  \  |
#     +         -
#     (5)      (-1)
#      \       /
#       \     /
#          *
#         (-5)
#          |
#          z
#
# 순전파: x, y → z 계산 (앞으로)
# 역전파: z의 기울기 → x, y의 기울기 계산 (거꾸로)

x = torch.tensor(2.0, requires_grad=True)
y = torch.tensor(3.0, requires_grad=True)

# 계산 그래프 생성 (순전파)
a = x + y  # a = 5
b = x - y  # b = -1
z = a * b  # z = -5

print('=== 순전파 ===')
print(f'a = x + y = {a.item()}')
print(f'b = x - y = {b.item()}')
print(f'z = a * b = {z.item()}')

# 역전파
z.backward()

print('\n=== 역전파 (기울기 계산) ===')
print(f"∂z/∂x = {x.grad}")
print(f"∂z/∂y = {y.grad}")

# 검증:
# z = (x + y)(x - y) = x² - y²
# ∂z/∂x = 2x = 2*2 = 4 ✓
# ∂z/∂y = -2y = -2*3 = -6 ✓
print()


# ============================================================
# 5. 연쇄 법칙 (Chain Rule)
# ============================================================

print("="*50)
print("5. 연쇄 법칙")
print("="*50)

# 연쇄 법칙 = 합성함수의 미분 법칙
# z = f(g(x)) 일 때
# dz/dx = (dz/dg) * (dg/dx)

# 예시 1: z = (x²)³
#
# 분해:
# g(x) = x²      → dg/dx = 2x
# h(g) = g³      → dh/dg = 3g²
#
# 연쇄 법칙 적용:
# dz/dx = (dh/dg) * (dg/dx)
#       = 3g² * 2x
#       = 3(x²)² * 2x
#       = 6x⁵

x = torch.tensor(2.0, requires_grad=True)

# z = (x²)³
g = x ** 2  # 중간 값
z = g ** 3  # 최종 값

z.backward()

print('=== 예시 1: z = (x²)³ ===')
print(f'x = {x.item()}')
print(f'g = x² = {g.item()}')
print(f'z = g³ = {z.item()}')
print(f'dz/dx = 6x⁵ = {x.grad.item()}')
print(f'검증: 6 * 2⁵ = {6 * (2**5)}')

# 예시 2: y = (2x + 1)³
#
# 분해:
# a = 2x         → da/dx = 2
# b = a + 1      → db/da = 1
# y = b³         → dy/db = 3b²
#
# 연쇄 법칙 적용:
# dy/dx = (dy/db) * (db/da) * (da/dx)
#       = 3b² * 1 * 2
#       = 6(2x + 1)²

x = torch.tensor(3.0, requires_grad=True)

a = 2 * x       # a = 2x
b = a + 1       # b = 2x + 1
y = b ** 3      # y = (2x + 1)³

# 역전파
y.backward()

print('\n=== 예시 2: y = (2x + 1)³ ===')
print(f'x = {x.item()}')
print(f'a = 2x = {a.item()}')
print(f'b = a+1 = {b.item()}')
print(f'y = b³ = {y.item()}')
print(f'dy/dx (자동) = {x.grad.item()}')

manual = 6 * ((2 * 3 + 1) ** 2)
print(f'dy/dx (수동) = 6(2*3+1)² = {manual}')
print()



# ============================================================
# 6. 동적 계산 그래프 (Dynamic Computational Graph)
# ============================================================

print("="*50)
print("6. 동적 계산 그래프")
print("="*50)

# PyTorch의 특징: 실행 시점에 그래프 생성 (Define-by-Run)
# → 조건문, 반복문 등 Python 제어 구문 사용 가능
# (TensorFlow 1.x는 정적 그래프였음)

x = torch.tensor(2.0, requires_grad=True)

# 조건에 따라 다른 연산 수행
if x > 0:
    y = x ** 2  # x가 양수면 제곱
else:
    y = x ** 3  # x가 음수면 세제곱

# 역전파
y.backward()

print(f'x = {x.item()}')
print(f'x > 0이므로 y = x² 경로 선택')
print(f'dy/dx = 2x = {x.grad}')

print("\n[동적 그래프의 장점]")
print("  ✓ Python 문법 그대로 사용 가능")
print("  ✓ 디버깅이 쉬움 (print로 중간값 확인)")
print("  ✓ 가변 길이 입력/출력 처리 용이")
print("  ✓ 조건부 연산, 반복 등 유연한 모델 구현")
