import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# ============================================================
# STEP 4: 코드로 구현
# ============================================================
# 목표: y = 2x + 3 관계를 데이터에서 찾아내기

print("=" * 60)
print("경사 하강법 구현")
print("=" * 60)

# 데이터 생성
np.random.seed(42)
x = np.random.randn(100)
y = 2 * x + 3 + np.random.randn(100) * 0.5  # y = 2x + 3 + 노이즈

print(f"\n[데이터] {len(x)}개")
print(f"실제 관계: y = 2x + 3")
print(f"목표: 컴퓨터가 스스로 찾기!\n")

# 파라미터 초기화
w = 0.0  # 기울기
b = 0.0  # 절편
lr = 0.1  # 학습률 (learning rate)
epochs = 100  # 반복 횟수

# 학습 과정 기록
loss_history = []
w_history = []
b_history = []

print("[학습 시작]")
print(f"초기값: w={w}, b={b}")
print(f"학습률: {lr}, 반복: {epochs}번\n")
# [학습 시작]
# 초기값: w=0.0, b=0.0
# 학습률: 0.1, 반복: 100번

# 경사 하강법 실행
for epoch in range(epochs):
    # 1. 예측
    y_pred = w * x + b

    # 2. 오차 계산 (MSE)
    loss = np.mean((y - y_pred) ** 2)
    loss_history.append(loss)

    # 3. 기울기 계산 (미분)
    # dw = "w를 조금 바꾸면 오차가 어떻게 변하나?"
    # db = "b를 조금 바꾸면 오차가 어떻게 변하나?"
    dw = np.mean(2 * (y_pred - y) * x)  # w에 대한 기울기
    db = np.mean(2 * (y_pred - y))  # b에 대한 기울기

    # 4. 파라미터 업데이트
    # 기울기 반대 방향으로 조금씩 이동
    w = w - lr * dw
    b = b - lr * db

    # 기록
    w_history.append(w)
    b_history.append(b)

    # 20번마다 출력
    if epoch % 20 == 0:
        print(f'Epoch {epoch:3d}: Loss={loss:.4f}, w={w:.4f}, b={b:.4f}')
        # Epoch   0: Loss=11.1166, w=0.2567, b=0.5607
        # Epoch  20: Loss=0.2294, w=1.8559, b=2.9548
        # Epoch  40: Loss=0.2209, w=1.9258, b=3.0024
        # Epoch  60: Loss=0.2209, w=1.9283, b=3.0037
        # Epoch  80: Loss=0.2209, w=1.9284, b=3.0037

print(f'\n[최종 결과]')
print(f'  w = {w:.4f} (목표: 2.0)')
print(f'  b = {b:.4f} (목표: 3.0)')
print(f'  오차: w는 {abs(w-2.0):.4f}, b는 {abs(b-3.0):.4f}')

if abs(w-2.0) < 0.1 and abs(b-3.0) < 0.1:
    print(f'  → 매우 정확하게 찾음\n')
else:
    print(f'  → 더 많은 학습 필요\n')
# [최종 결과]
#   w = 1.9284 (목표: 2.0)
#   b = 3.0037 (목표: 3.0)
#   오차: w는 0.0716, b는 0.0037
#   → 매우 정확하게 찾음


# ============================================================
# STEP 5: 시각화
# ============================================================
# 학습 과정을 그래프로 확인
# - 오차가 줄어드는 과정
# - w와 b가 목표값으로 수렴하는 과정

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# 1. 오차 감소
axes[0].plot(loss_history, color='red', linewidth=2)
axes[0].set_xlabel('Epoch', fontsize=10)
axes[0].set_ylabel('Loss (오차)', fontsize=10)
axes[0].set_title('오차가 점점 줄어듦', fontsize=12, fontweight='bold')
axes[0].grid(True, alpha=0.3)

# 2. w 변화
axes[1].plot(w_history, color='blue', linewidth=2, label='w')
axes[1].axhline(y=2.0, color='green', linestyle='--',
                linewidth=2, label='목표 (2.0)')
axes[1].set_xlabel('Epoch', fontsize=10)
axes[1].set_ylabel('w', fontsize=10)
axes[1].set_title('w가 2.0으로 수렴', fontsize=12, fontweight='bold')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

# 3. b 변화
axes[2].plot(b_history, color='purple', linewidth=2, label='b')
axes[2].axhline(y=3.0, color='green', linestyle='--',
                linewidth=2, label='목표 (3.0)')
axes[2].set_xlabel('Epoch', fontsize=10)
axes[2].set_ylabel('b', fontsize=10)
axes[2].set_title('b가 3.0으로 수렴', fontsize=12, fontweight='bold')
axes[2].legend()
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
