"""
============================================================
02. 경사 하강법 (Gradient Descent)
============================================================

학습 목표:
1. 경사 하강법이 무엇인지
2. 컴퓨터가 어떻게 최적의 직선을 찾는지
3. 학습률의 중요성
4. 실제 코드로 구현하기
5. 시각화로 이해하기
"""

import numpy as np
import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# ============================================================
# STEP 1: 경사 하강법이란?
# ============================================================
# 비유: 안개 낀 산에서 마을 찾기
#
# 상황:
# - 산 어딘가에 있음 (앞이 안 보임)
# - 마을은 가장 낮은 곳에 있음
# - 발밑의 경사만 느낄 수 있음
#
# 해결:
# - 가장 가파르게 내려가는 방향 찾기
# - 그 방향으로 한 걸음 내딛기
# - 반복!
#
# 머신러닝에서:
# - 산 정상 = 오차가 큰 상태
# - 골짜기 = 오차가 작은 상태 (목표!)
# - 경사 = 기울기 (gradient)
# - 한 걸음 = 학습률 (learning rate)

# ============================================================
# STEP 2: 경사 하강법 수식
# ============================================================
# 파라미터(새) = 파라미터(현재) - 학습률 × 기울기
#
# 풀어 쓰면:
# "현재 위치에서, 기울기 반대 방향으로, 조금씩 이동"
#
# 왜 반대(-) 방향?
# - 기울기 = 오차가 증가하는 방향
# - 우리는 오차를 줄여야 함
# - 그래서 반대로!

# ============================================================
# STEP 3: 학습률의 중요성
# ============================================================
# 학습률 = 한 걸음의 크기
#
# 너무 크면:
# - 최적점을 지나침
# - 왔다갔다 발산
# - 비유: 너무 큰 보폭으로 뛰면 반대편 산으로 넘어감
#
# 너무 작으면:
# - 목표까지 시간이 너무 오래 걸림
# - 비유: 아주 작은 걸음으로 천천히
#
# 적절한 값:
# - 보통 0.001 ~ 0.1 사이
# - 실험으로 찾기

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

print(f'\n[최종 결과]')
print(f'  w = {w:.4f} (목표: 2.0)')
print(f'  b = {b:.4f} (목표: 3.0)')
print(f'  오차: w는 {abs(w-2.0):.4f}, b는 {abs(b-3.0):.4f}')

if abs(w-2.0) < 0.1 and abs(b-3.0) < 0.1:
    print(f'  → 매우 정확하게 찾음\n')
else:
    print(f'  → 더 많은 학습 필요\n')

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
axes[1].axhline(y=2.0, color='green', linestyle='--', linewidth=2, label='목표 (2.0)')
axes[1].set_xlabel('Epoch', fontsize=10)
axes[1].set_ylabel('w', fontsize=10)
axes[1].set_title('w가 2.0으로 수렴', fontsize=12, fontweight='bold')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

# 3. b 변화
axes[2].plot(b_history, color='purple', linewidth=2, label='b')
axes[2].axhline(y=3.0, color='green', linestyle='--', linewidth=2, label='목표 (3.0)')
axes[2].set_xlabel('Epoch', fontsize=10)
axes[2].set_ylabel('b', fontsize=10)
axes[2].set_title('b가 3.0으로 수렴', fontsize=12, fontweight='bold')
axes[2].legend()
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# ============================================================
# STEP 6: 개선된 경사 하강법들
# ============================================================
# 경사 하강법의 한계와 해결책
#
# 한계 1: 지역 최솟값 (Local Minimum)
# - 전체에서 가장 낮은 곳이 아니라 근처의 웅덩이에 갇힐 수 있음
# - 비유: 작은 웅덩이에 빠져서 큰 골짜기를 못 찾음
#
# 해결 1: SGD (Stochastic Gradient Descent)
# - 전체 데이터 대신 일부만 사용
# - 빠르고, 무작위성으로 지역 최솟값 탈출
#
# 해결 2: Momentum
# - 이전 이동 방향의 관성 반영
# - 비유: 공이 굴러가듯 탄력으로 웅덩이 넘어감
#
# 해결 3: Adam (가장 많이 사용!)
# - 학습률을 파라미터별로 자동 조절
# - 대부분의 경우 잘 작동

print("=" * 60)
print("요약")
print("=" * 60)
print("\n[오늘 배운 내용]")
print("  ✓ 경사 하강법 = 산을 내려가듯 오차 줄이기")
print("  ✓ 기울기 = 오차가 증가하는 방향")
print("  ✓ 학습률 = 한 걸음 크기")
print("  ✓ 반복 = 조금씩 파라미터 조정")
print("  ✓ 개선 = SGD, Momentum, Adam")

print("\n[핵심 코드 4단계]")
print("  1. y_pred = w * x + b  # 예측")
print("  2. loss = mean((y - y_pred)²)  # 오차")
print("  3. dw, db 계산  # 기울기")
print("  4. w = w - lr * dw  # 업데이트")

print("\n[실전 팁]")
print("  - scikit-learn은 자동으로 경사 하강법 사용")
print("  - 딥러닝에서는 Adam이 가장 많이 사용")
print("  - 학습률은 0.001부터 시작")

print("\n[다음 단계]")
print("  → 03_다중선형회귀.py: 여러 변수 동시에 고려")

print("\n[연습 문제]")
print("  1. 학습률을 0.01, 0.5로 바꿔보기")
print("  2. epochs를 10, 1000으로 바꿔보기")
print("  3. 초기값 w=10, b=-5로 시작하면?")
print()
