# 손실 함수 (Loss Function)
# 예측과 실제의 차이를 측정

# 목적
# - 모델 성능을 수치화
# - 최적화 목표 제공
# - 손실이 작을수록 좋은 모델

# 다른 이름:
# - 비용 함수 (Cost Function)
# - 목적 함수 (Objective Function)

# 손실 vs 비용
# 손실 (Loss)
# - 단일 샘플에 대한 오차
# - L(ŷ, y)

# 비용 (Cost)
# - 전체 샘플의 평균 손실
# - J = (1/n) × Σ L(ŷᵢ, yᵢ)



# 회귀 손실 함수
# MSE(Mean Squared Error)

# 수식: MSE = (1/n) × Σ(yᵢ - ŷᵢ)²

# 특징
# - 오차의 제곱 평균
# - 큰 오차에 큰 패널티
# - 미분이 간단

# 사용: 일반적인 회귀 문제

import torch
import torch.nn as nn

# 예측과 실제
y_pred = torch.tensor([2.5, 0.0, 2.1, 7.8])
y_test = torch.tensor([3.0, -0.5, 2.0, 7.5])

# MSE 계산 (수동)
mse_manual = ((y_test-y_pred) ** 2).mean()
print(f'MSE (수동): {mse_manual:.4f}')

# PyTorch MSE
mse_loss = nn.MSELoss()
mse = mse_loss(y_pred, y_test)
print(f'MSE (PyTorch) {mse:.4f}')

# MAE(Mean Absolute Error)
# 수식: MAE = (1/n) × Σ|yᵢ - ŷᵢ|

# 특징
# - 오차의 절대값 평균
# - 이상치에 덜 민감
# - 0에서 미분 불가

# 사용: 이상치가 있는 회귀

mae_loss = nn.L1Loss()
mae = mae_loss(y_pred, y_test)
print(f'MAE (PyTorch) {mae:.4f}')


# Huber Loss

# 수식:
# δ 이하: 0.5 × (y - ŷ)²
# δ 초과: δ × (|y - ŷ| - 0.5δ)

# 특징
# MSE와 MAE의 조합
# - 작은 오차: MSE처럼 동작
# - 큰 오차 : MAE처럼 동작

# 사용: 이상치가 일부 있는 경우
huber_loss= nn.HuberLoss(delta=1.0)
huber = huber_loss(y_pred, y_test)
print(f'Huber (PyTorch) {huber:.4f}')

# 분류 손실 함수
# Binary Cross-Entropy (BCE)
# 수식: BCE = -(1/n) × Σ[y·log(ŷ) + (1-y)·log(1-ŷ)]

# 특징:
# - 이진 분류용
# - 확률 예측 필요 (0~1)
# - Sigmoid 출력과 함께 사용

# 해석
# - y = 1일때 : -log(ŷ) -> ŷ가 1에 가까울수록 손실 작음
# - y = 0일때 : -log(1-ŷ) -> ŷ가 0에 가까울수록 손실 작음

# 이진 분류
y_pred = torch.tensor([0.9, 0.2, 0.8, 0.3])
y_test = torch.tensor([1.0, 0.0 ,1.0, 0.0])

# BCE
bce_loss = nn.BCELoss()
bce = bce_loss(y_pred, y_test)
print(f'BCE: {bce:.4f}')

# BCEWithLogits (Sigmoid + BCE, 더 안정적)
y_logits = torch.tensor([2.0, -1.5, 1.5, -1.0])
bce_logits = nn.BCEWithLogitsLoss()
bce2 = bce_logits(y_logits, y_test)
print(f'BCEWithLogits: {bce2:.4f}')

# Cross-Entropy (다중 분류)

# 수식: CE = -Σ yᵢ·log(ŷᵢ)

# 특징
# - 다중 분류용
# - One-hot 인코딩된 라벨
# - Softmax 출력과 함께 사용

# PyTorch:
# CrossEntropyLoss = Softmax + NLLLoss
# 입력: 로짓 (Softmax 전)
# 타겟: 클래스 인덱스 (정수)

# 다중 분류 (3개 클래스)
y_logits = torch.tensor([
    [2.0, 1.0, 0.1],
    [0.5, 2.5, 0.3],
    [0.1, 0.2, 3.0],
])

y_test = torch.tensor([0, 1, 2]) # 클래스 인덱스

ce_loss = nn.CrossEntropyLoss()
ce = ce_loss(y_logits, y_test)
print(f'Cross-Entropy: {ce:.4f}')

# 확률로 변환
probs = torch.softmax(y_logits, dim=1)
print(f'예측 확률:\n {probs}')

# 손실 함수 선택 가이드
# 회귀:
# - 기본 : MSE
# - 이상치 있음 : MAE 또는 Huber
# - 특수 분포 : 적절한 손실 설계

# 분류:
# - 이진 분류 : BCELoss 또는 BCEWithLogitsLoss
# - 다중 분류 : CrossEntropyLoss
