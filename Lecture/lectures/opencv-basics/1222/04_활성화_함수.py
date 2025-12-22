# 활성화 함수 (Activation Function)

# 쉽게 이해하기:
# 활성화 함수 = 뉴런이 "켜질지 말지" 결정하는 스위치
# 마치 시험에서 60점 넘으면 합격, 안 넘으면 불합격처럼!

# 정의:
# 뉴런의 출력을 결정하는 비선형 함수

# 역할:
# 1. 비선형성 도입 (복잡한 패턴 학습 가능)
# 2. 출력 범위 조절 (너무 크거나 작지 않게)
# 3. 신호 전달 여부 결정 (켤지 말지)


# 왜 필요한가?

# 쉬운 비유:
# 활성화 함수 없으면 = 레고를 일자로만 쌓는 것
# 활성화 함수 있으면 = 레고를 자유롭게 구부려서 복잡한 모양 만들기

# 수식으로 보기:
# 선형 함수만 사용하면...
# 층1: y₁ = W₁x + b₁
# 층2: y₂ = W₂y₁ + b₂
#      = W₂(W₁x + b₁) + b₂
#      = (W₂W₁)x + (W₂b₁ + b₂)
#      = W'x + b'  ← 결국 한 층짜리와 똑같음!

# 결론: 아무리 층을 쌓아도 단일 선형 변환!
# → 비선형 함수가 있어야 복잡한 패턴 학습 가능


# 주요 활성화 함수들


# 1. ReLU (Rectified Linear Unit) - 가장 많이 사용!

# 수식: ReLU(x) = max(0, x)
# - x > 0이면: x 그대로
# - x ≤ 0이면: 0

# 쉬운 비유:
# ReLU = 빚 탕감
# - 플러스 통장 (100원) → 그대로 100원
# - 마이너스 통장 (-100원) → 0원으로 탕감!

# 예시:
# ReLU(-5) = 0
# ReLU(0) = 0
# ReLU(5) = 5

# 장점:
# - 계산이 매우 빠름 (단순 비교)
# - 학습이 잘 됨
# - 기울기 소실 문제 완화

# 단점:
# - 음수 입력에 대해 뉴런이 "죽을" 수 있음 (Dying ReLU)


# 2. Sigmoid (시그모이드)

# 수식: σ(x) = 1 / (1 + e^(-x))
# 출력 범위: (0, 1)

# 쉬운 비유:
# Sigmoid = 확률 변환기
# - 큰 양수 → 1에 가까움 (거의 확실)
# - 큰 음수 → 0에 가까움 (거의 확실하지 않음)
# - 0 → 0.5 (반반)

# 예시:
# σ(-10) ≈ 0.0000
# σ(0) = 0.5
# σ(10) ≈ 0.9999

# 장점:
# - 출력을 확률로 해석 가능 (0~1 사이)
# - 부드러운 곡선

# 단점:
# - 기울기 소실 문제 (Vanishing Gradient)
# - 출력이 0 중심이 아님
# - 계산이 상대적으로 느림

# 사용처:
# - 주로 출력층 (이진 분류)
# - 은닉층에서는 잘 안 씀


# 3. Tanh (하이퍼볼릭 탄젠트)

# 수식: tanh(x) = (e^x - e^(-x)) / (e^x + e^(-x))
# 출력 범위: (-1, 1)

# Sigmoid와 비슷하지만 범위가 다름:
# - Sigmoid: 0~1
# - Tanh: -1~1 (중심이 0)

# 예시:
# tanh(-10) ≈ -1
# tanh(0) = 0
# tanh(10) ≈ 1

# 장점:
# - 출력이 0 중심 (Sigmoid보다 학습이 조금 더 좋음)
# - 부드러운 곡선

# 단점:
# - 여전히 기울기 소실 가능
# - 요즘은 ReLU를 더 많이 씀


# 4. Leaky ReLU

# 수식: LeakyReLU(x) = max(0.01x, x)
# - x > 0이면: x 그대로
# - x ≤ 0이면: 0.01x (작은 값 유지)

# ReLU의 "죽는 뉴런" 문제를 해결!

# 예시:
# LeakyReLU(-5) = -0.05 (완전히 0이 아님!)
# LeakyReLU(0) = 0
# LeakyReLU(5) = 5

# 장점:
# - ReLU의 Dying 문제 해결
# - 계산 빠름

# 단점:
# - 0.01 같은 값을 정해야 함


# 5. Softmax - 출력층 전용!

# 수식: Softmax(xᵢ) = e^xᵢ / Σe^xⱼ
# 출력: 각 클래스의 확률 (합이 1)

# 쉬운 이해:
# 여러 선택지의 확률로 변환
# 예) [2.0, 1.0, 0.1] → [0.7, 0.2, 0.1]

# 사용처:
# - 다중 클래스 분류의 출력층
# 예) 개/고양이/새 구분


# 활성화 함수 선택 가이드

# 은닉층 (중간 층):
# → ReLU 사용! (기본 선택)
# → 문제 있으면 Leaky ReLU 시도

# 출력층:
# - 이진 분류 (개 or 고양이) → Sigmoid
# - 다중 분류 (개/고양이/새) → Softmax
# - 회귀 (숫자 예측) → 활성화 함수 없음 (Linear)


# 실습 코드

import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import numpy as np

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 활성화 함수 테스트
print("=== 활성화 함수 동작 확인 ===\n")

# 테스트 입력
x = torch.tensor([-2.0, -1.0, 0.0, 1.0, 2.0])
print(f"입력: {x.tolist()}\n")

# ReLU
relu = nn.ReLU()
print(f"ReLU 출력: {relu(x).tolist()}")
print("→ 음수는 0, 양수는 그대로\n")

# Sigmoid
sigmoid = nn.Sigmoid()
print(f"Sigmoid 출력: {[f'{v:.3f}' for v in sigmoid(x).tolist()]}")
print("→ 모두 0~1 사이로 압축\n")

# Tanh
tanh = nn.Tanh()
print(f"Tanh 출력: {[f'{v:.3f}' for v in tanh(x).tolist()]}")
print("→ 모두 -1~1 사이로 압축\n")


# 신경망에서 사용 예시
print("=== 신경망에서 활성화 함수 사용 ===\n")

model = nn.Sequential(
    nn.Linear(10, 20),  # 입력층 → 은닉층
    nn.ReLU(),          # 활성화 (ReLU)
    nn.Linear(20, 10),  # 은닉층 → 은닉층
    nn.ReLU(),          # 활성화 (ReLU)
    nn.Linear(10, 1),   # 은닉층 → 출력층
    nn.Sigmoid()        # 활성화 (Sigmoid, 0~1 출력)
)

print(model)
print("\n설명:")
print("- 중간층: ReLU 사용 (표준)")
print("- 출력층: Sigmoid 사용 (이진 분류)")


# 시각화
print("\n=== 활성화 함수 그래프 ===")

x_range = np.linspace(-5, 5, 100)

# ReLU
relu_y = np.maximum(0, x_range)

# Sigmoid
sigmoid_y = 1 / (1 + np.exp(-x_range))

# Tanh
tanh_y = np.tanh(x_range)

# Leaky ReLU
leaky_relu_y = np.maximum(0.01 * x_range, x_range)

plt.figure(figsize=(14, 10))

# ReLU
plt.subplot(2, 2, 1)
plt.plot(x_range, relu_y, 'b-', linewidth=2)
plt.title('ReLU: max(0, x)', fontsize=14)
plt.xlabel('입력 (x)')
plt.ylabel('출력')
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5)

# Sigmoid
plt.subplot(2, 2, 2)
plt.plot(x_range, sigmoid_y, 'g-', linewidth=2)
plt.title('Sigmoid: 1/(1+e^(-x))', fontsize=14)
plt.xlabel('입력 (x)')
plt.ylabel('출력')
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
plt.axhline(y=0.5, color='r', linestyle='--', alpha=0.5)

# Tanh
plt.subplot(2, 2, 3)
plt.plot(x_range, tanh_y, 'r-', linewidth=2)
plt.title('Tanh: (e^x - e^(-x))/(e^x + e^(-x))', fontsize=14)
plt.xlabel('입력 (x)')
plt.ylabel('출력')
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5)

# Leaky ReLU
plt.subplot(2, 2, 4)
plt.plot(x_range, leaky_relu_y, 'm-', linewidth=2)
plt.title('Leaky ReLU: max(0.01x, x)', fontsize=14)
plt.xlabel('입력 (x)')
plt.ylabel('출력')
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5)

plt.tight_layout()
plt.show()


# 요약 정리
print("\n" + "="*60)
print("핵심 정리")
print("="*60)
print("\n1. 활성화 함수 = 비선형성을 추가해서 복잡한 패턴 학습")
print("\n2. ReLU: max(0, x)")
print("   - 가장 많이 사용")
print("   - 은닉층의 기본 선택")
print("\n3. Sigmoid: 0~1 출력")
print("   - 이진 분류 출력층")
print("\n4. Softmax: 확률 분포 출력 (합=1)")
print("   - 다중 클래스 분류 출력층")
print("\n5. 기본 전략:")
print("   - 은닉층: ReLU")
print("   - 출력층: 문제에 따라 선택")
print("="*60)
