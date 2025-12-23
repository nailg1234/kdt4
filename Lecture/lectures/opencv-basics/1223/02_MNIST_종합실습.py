# ============================================================
# MNIST 손글씨 숫자 분류 - 딥러닝 종합 실습
# ============================================================
#
# 이 파일은 PyTorch를 사용하여 완전한 신경망을 구현하고
# MNIST 손글씨 숫자 분류 문제를 해결합니다.
#
# MNIST란?
# - 0부터 9까지 손으로 쓴 숫자 이미지 데이터셋
# - 각 이미지는 28x28 픽셀의 흑백 이미지
# - 훈련 데이터: 60,000개, 테스트 데이터: 10,000개
# ============================================================

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import matplotlib.pyplot as plt
import numpy as np

# ============================================================
# 1. 초기 설정
# ============================================================

# GPU 사용 가능 여부 확인
# - GPU가 있으면 'cuda', 없으면 'cpu' 사용
# - GPU를 사용하면 학습 속도가 훨씬 빠릅니다
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f'사용 장치: {device}')

# 재현성을 위한 시드 설정
# - 같은 코드를 여러 번 실행해도 같은 결과가 나오도록 설정
# - 랜덤 값을 고정하여 실험 결과를 재현 가능하게 만듦
torch.manual_seed(42)

if device.type == 'cuda':
    torch.cuda.manual_seed(42)


# ============================================================
# 주요 용어 설명
# ============================================================
#
# 로짓 (Logits):
#   - Softmax를 거치기 전의 원시 출력값
#   - 예: [2.1, 0.5, -0.3] -> 아직 확률이 아님
#   - Softmax를 거치면 [0.7, 0.2, 0.1] 같은 확률로 변환됨
#
# Normalize (정규화):
#   - 데이터를 평균 0, 표준편차 1로 변환
#   - (0.1307, 0.3081): MNIST 데이터셋의 평균과 표준편차
#   - 학습 안정성을 향상시킴
#   - 예: 원본 값 0.5 → 정규화 후 약 1.2
#
# Dropout:
#   - 학습 시 일부 뉴런을 무작위로 끄는 기법
#   - nn.Dropout(0.2): 20%의 뉴런을 랜덤하게 비활성화
#   - 과적합 방지 효과 (모델이 학습 데이터만 외우는 것 방지)
#   - 평가 시에는 모든 뉴런을 사용
#
# model.train() vs model.eval():
#   - train(): 학습 모드 (Dropout 작동 O)
#   - eval(): 평가 모드 (Dropout 비활성화, 모든 뉴런 사용)
#
# torch.no_grad():
#   - 기울기 계산을 비활성화
#   - 추론/평가 시 사용하여 메모리 절약 + 속도 향상
#   - 학습할 때만 기울기가 필요하므로 평가 시엔 불필요
#
# DataLoader:
#   - 데이터를 배치로 나눠서 제공하는 도구
#   - batch_size=64: 한 번에 64개씩 처리
#   - shuffle=True: 매 에폭마다 데이터 순서를 섞음 (학습 성능 향상)
#
# 에폭 (Epoch):
#   - 전체 데이터를 1회 학습하는 단위
#   - 10 epochs = 60,000개 데이터를 10번 반복 학습
#   - 많을수록 학습이 잘 되지만, 과적합 위험도 증가
#
# 배치 (Batch):
#   - 한 번에 처리하는 데이터 묶음
#   - 전체를 한 번에 처리하면 메모리 부족
#   - 작은 배치로 나눠서 처리 (예: 64개씩)
# ============================================================


# ============================================================
# 2. 데이터 준비
# ============================================================

# 데이터 변환 정의
# ToTensor(): 이미지를 텐서로 변환하고 0~1로 정규화
# Normalize(): 평균과 표준편차를 이용한 표준화
transform = transforms.Compose([
    transforms.ToTensor(),  # 이미지 → 텐서 변환 (0~255 → 0~1)
    transforms.Normalize((0.1307,), (0.3081,))  # MNIST 평균, 표준편차로 정규화
])

# MNIST 데이터셋 다운로드
# root: 데이터를 저장할 폴더
# train: True면 훈련 데이터, False면 테스트 데이터
# download: True면 데이터가 없을 때 자동 다운로드
# transform: 위에서 정의한 변환 적용
train_dataset = datasets.MNIST(
    root='./data',
    train=True,
    download=True,
    transform=transform
)

test_dataset = datasets.MNIST(
    root='./data',
    train=False,
    download=True,
    transform=transform
)

print(f'훈련 데이터: {len(train_dataset)}개')
print(f'테스트 데이터: {len(test_dataset)}개')


# ============================================================
# 3. 데이터 로더 생성
# ============================================================

# 배치 크기 설정
# 너무 작으면: 학습이 불안정, 시간 오래 걸림
# 너무 크면: 메모리 부족, 일반화 성능 저하
# 보통 32, 64, 128 등을 사용
batch_size = 64

# DataLoader 생성
# 훈련 데이터는 shuffle=True로 매번 순서를 섞음
train_loader = DataLoader(
    train_dataset,
    batch_size=batch_size,
    shuffle=True,  # 매 에폭마다 데이터 순서를 섞음
)

# 테스트 데이터는 shuffle=False (순서가 중요하지 않음)
test_loader = DataLoader(
    test_dataset,
    batch_size=batch_size,
    shuffle=False,  # 평가 시에는 순서를 섞을 필요 없음
)

print(f'훈련 배치 수: {len(train_loader)}개 (60000 ÷ 64 ≈ 938)')
print(f'테스트 배치 수: {len(test_loader)}개 (10000 ÷ 64 ≈ 157)')


# ============================================================
# 4. 데이터 시각화
# ============================================================

# 2행 5열로 10개의 샘플 이미지를 보여줌
fig, axes = plt.subplots(2, 5, figsize=(12, 5))

for i, ax in enumerate(axes.flatten()):
    # 데이터셋에서 i번째 이미지와 레이블 가져오기
    image, label = train_dataset[i]
    # 이미지 표시 (squeeze()로 차원 줄이기: [1, 28, 28] → [28, 28])
    ax.imshow(image.squeeze(), cmap='gray')
    ax.set_title(f'Label: {label}')
    ax.axis('off')  # 축 숨기기

plt.suptitle('MNIST 샘플 이미지')
plt.tight_layout()
plt.show()


# ============================================================
# 5. 신경망 모델 정의 (MLP - Multi-Layer Perceptron)
# ============================================================

class MLP(nn.Module):
    """
    다층 퍼셉트론 (Multi-Layer Perceptron)

    완전연결층(Fully Connected Layer)으로만 구성된 신경망
    각 층의 모든 뉴런이 다음 층의 모든 뉴런과 연결됨

    구조:
    입력 (784)  → FC1 (512) → ReLU → Dropout
                → FC2 (256) → ReLU → Dropout
                → FC3 (128) → ReLU → Dropout
                → FC4 (10)

    784: 28x28 이미지를 1차원으로 펼친 크기
    10: 0~9까지 10개의 클래스
    """

    def __init__(self,
                 input_size=784,
                 hidden_sizes=[512, 256, 128],
                 num_classes=10):
        """
        신경망 초기화

        Args:
            input_size (int): 입력 크기 (기본: 784 = 28x28)
            hidden_sizes (list): 은닉층의 크기들 (기본: [512, 256, 128])
            num_classes (int): 출력 클래스 수 (기본: 10 = 0~9)
        """
        # 1. 부모 클래스(nn.Module) 초기화 - 필수!
        # 이걸 해야 PyTorch가 이 클래스를 신경망으로 인식
        super(MLP, self).__init__()

        # 2. Flatten 층 정의
        # 역할: [batch, 1, 28, 28] → [batch, 784]
        # 2D 이미지를 1D 벡터로 펼침
        # 예: [[1,2],[3,4]] → [1,2,3,4]
        self.flatten = nn.Flatten()

        # 3. 신경망 층들을 리스트로 구성
        layers = []  # 층들을 순서대로 담을 리스트

        prev_size = input_size  # 이전 층의 출력 크기 (처음엔 입력 크기)

        # hidden_sizes의 각 크기에 대해 층을 생성
        # 예: [512, 256, 128]이면 3개의 은닉층 생성
        for hidden_size in hidden_sizes:
            # 완전연결층 (Fully Connected Layer) 추가
            # prev_size개의 입력을 hidden_size개의 출력으로 변환
            # 예: 784 → 512, 512 → 256, 256 → 128
            layers.append(nn.Linear(prev_size, hidden_size))

            # 활성화 함수 (ReLU) 추가
            # ReLU(x) = max(0, x)
            # 음수는 0으로, 양수는 그대로 유지
            # 비선형성을 추가하여 복잡한 패턴 학습 가능
            layers.append(nn.ReLU())

            # Dropout 추가 (과적합 방지)
            # 학습 시 20%의 뉴런을 무작위로 끔
            # 모델이 특정 뉴런에 의존하지 않도록 함
            layers.append(nn.Dropout(0.2))

            # 다음 층을 위해 현재 크기를 저장
            prev_size = hidden_size

        # 4. 출력층 추가
        # 마지막 은닉층의 크기(128) → 클래스 수(10)
        # 활성화 함수 없음 (CrossEntropyLoss가 내부에 Softmax 포함)
        layers.append(nn.Linear(prev_size, num_classes))

        # 5. Sequential로 층들을 하나의 모듈로 묶기
        # *layers: 리스트를 풀어서 개별 인자로 전달
        # 예: [layer1, layer2, layer3] → Sequential(layer1, layer2, layer3)
        self.network = nn.Sequential(*layers)

    def forward(self, x):
        """
        순전파 (Forward Pass)

        데이터가 신경망을 통과하는 과정

        Args:
            x (Tensor): 입력 이미지 [batch, 1, 28, 28]

        Returns:
            Tensor: 출력 로짓 [batch, 10]
        """
        # 1. 이미지를 1차원으로 펼침
        # [batch, 1, 28, 28] → [batch, 784]
        # 예: [64, 1, 28, 28] → [64, 784]
        x = self.flatten(x)

        # 2. 신경망 통과
        # 순차적으로 모든 층을 거침
        # [batch, 784] → [batch, 512] → [batch, 256] → [batch, 128] → [batch, 10]
        x = self.network(x)

        # 3. 로짓 반환 (Softmax 전의 값)
        # CrossEntropyLoss가 자동으로 Softmax 적용
        return x

# 모델 생성 및 GPU로 이동
model = MLP().to(device)
print(model)
print()  # 빈 줄 추가

# ============================================================
# 6. 모델 파라미터 확인
# ============================================================

# 파라미터 수 계산
# 각 층의 가중치와 편향의 개수를 모두 합산
# 예: nn.Linear(784, 512)는 784*512 + 512 = 401,920개
total_params = sum(p.numel() for p in model.parameters())
trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)

print(f'총 파라미터: {total_params:,}개')
print(f'학습 가능 파라미터: {trainable_params:,}개')
print()  # 빈 줄 추가


# ============================================================
# 7. 학습 설정
# ============================================================

# 손실 함수 (Loss Function)
# CrossEntropyLoss: 다중 분류 문제에 사용
# 내부적으로 Softmax + NLLLoss를 합친 것
# 입력: 로짓 (Softmax 전의 값)
# 타겟: 클래스 인덱스 (0~9)
criterion = nn.CrossEntropyLoss()

# 옵티마이저 (Optimizer)
# Adam: 가장 많이 사용되는 최적화 알고리즘
# lr (learning rate): 학습률
#   - 너무 크면: 학습이 불안정, 발산할 수 있음
#   - 너무 작으면: 학습이 느림, 지역 최솟값에 갇힐 수 있음
#   - 보통 0.001 (1e-3) ~ 0.0001 (1e-4) 사용
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 학습률 스케줄러 (Learning Rate Scheduler) - 선택적
# 학습이 진행될수록 학습률을 감소시킴
# StepLR: step_size 에폭마다 학습률을 gamma배 감소
# 예: 5 에폭마다 학습률을 0.5배로 감소
#     0.001 → 0.0005 → 0.00025 → ...
scheduler = optim.lr_scheduler.StepLR(
    optimizer,
    step_size=5,  # 5 에폭마다
    gamma=0.5     # 0.5배로 감소
)


# ============================================================
# 8. 학습 및 평가 함수 정의
# ============================================================

def train_epoch(model, loader, criterion, optimizer, device):
    """
    한 에폭 동안 모델을 학습

    Args:
        model: 학습할 신경망 모델
        loader: 훈련 데이터 로더
        criterion: 손실 함수
        optimizer: 최적화 알고리즘
        device: 'cuda' 또는 'cpu'

    Returns:
        avg_loss (float): 평균 손실
        accuracy (float): 정확도 (%)
    """
    # 학습 모드로 설정 (Dropout 활성화)
    model.train()

    # 통계 변수 초기화
    total_loss = 0      # 전체 손실 합계
    correct = 0         # 정답 개수
    total = 0           # 전체 샘플 개수

    # 배치 단위로 데이터 처리
    for images, labels in loader:
        # 데이터를 GPU로 이동 (GPU 사용 시)
        images, labels = images.to(device), labels.to(device)

        # 1. 순전파 (Forward Pass)
        # 모델에 이미지를 입력하여 예측값 계산
        outputs = model(images)

        # 2. 손실 계산
        # 예측값과 실제 레이블 간의 차이를 계산
        loss = criterion(outputs, labels)

        # 3. 역전파 준비: 기울기 초기화
        # 이전 배치의 기울기가 남아있으면 누적되므로 초기화 필수
        optimizer.zero_grad()

        # 4. 역전파 (Backward Pass)
        # 손실을 기준으로 각 파라미터의 기울기 계산
        loss.backward()

        # 5. 가중치 업데이트
        # 계산된 기울기를 사용하여 파라미터 업데이트
        optimizer.step()

        # 통계 업데이트
        total_loss += loss.item()  # 손실 누적
        _, predicted = outputs.max(1)  # 가장 높은 확률의 클래스 선택
        total += labels.size(0)  # 전체 샘플 수 증가
        correct += predicted.eq(labels).sum().item()  # 정답 개수 증가

    # 평균 계산
    avg_loss = total_loss / len(loader)  # 배치당 평균 손실
    accuracy = 100. * correct / total    # 정확도 (%)

    return avg_loss, accuracy


def evaluate(model, loader, criterion, device):
    """
    모델을 평가

    Args:
        model: 평가할 신경망 모델
        loader: 테스트 데이터 로더
        criterion: 손실 함수
        device: 'cuda' 또는 'cpu'

    Returns:
        avg_loss (float): 평균 손실
        accuracy (float): 정확도 (%)
    """
    # 평가 모드로 설정 (Dropout 비활성화)
    model.eval()

    # 통계 변수 초기화
    total_loss = 0
    correct = 0
    total = 0

    # 기울기 계산 비활성화
    # 평가 시에는 기울기가 필요 없으므로 메모리와 연산 절약
    with torch.no_grad():
        for images, labels in loader:
            # 데이터를 GPU로 이동
            images, labels = images.to(device), labels.to(device)

            # 순전파만 수행 (역전파 없음)
            outputs = model(images)
            loss = criterion(outputs, labels)

            # 통계 업데이트
            total_loss += loss.item()
            _, predicted = outputs.max(1)
            total += labels.size(0)
            correct += predicted.eq(labels).sum().item()

    # 평균 계산
    avg_loss = total_loss / len(loader)
    accuracy = 100. * correct / total

    return avg_loss, accuracy


# ============================================================
# 9. 학습 실행
# ============================================================

# 학습 설정
num_epochs = 10  # 전체 데이터를 10번 반복 학습

# 학습 기록을 저장할 딕셔너리
history = {
    'train_loss': [],  # 훈련 손실
    'train_acc': [],   # 훈련 정확도
    'test_loss': [],   # 테스트 손실
    'test_acc': []     # 테스트 정확도
}

print("학습 시작!")
print("=" * 60)

# 에폭별 학습
for epoch in range(num_epochs):
    # 1. 한 에폭 학습
    train_loss, train_acc = train_epoch(
        model, train_loader, criterion, optimizer, device
    )

    # 2. 테스트 데이터로 평가
    test_loss, test_acc = evaluate(
        model, test_loader, criterion, device
    )

    # 3. 학습률 스케줄러 업데이트
    scheduler.step()

    # 4. 기록 저장
    history['train_loss'].append(train_loss)
    history['train_acc'].append(train_acc)
    history['test_loss'].append(test_loss)
    history['test_acc'].append(test_acc)

    # 5. 진행 상황 출력
    print(f"Epoch [{epoch+1}/{num_epochs}] "
          f"Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.2f}% | "
          f"Test Loss: {test_loss:.4f}, Test Acc: {test_acc:.2f}%")

print("=" * 60)
print(f"최종 테스트 정확도: {history['test_acc'][-1]:.2f}%")


# ============================================================
# 10. 학습 결과 시각화
# ============================================================

# 1행 2열의 그래프 생성
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 왼쪽: 손실 그래프
axes[0].plot(history['train_loss'], label='Train Loss', marker='o')
axes[0].plot(history['test_loss'], label='Test Loss', marker='s')
axes[0].set_xlabel('Epoch')
axes[0].set_ylabel('Loss')
axes[0].set_title('학습 손실 (낮을수록 좋음)')
axes[0].legend()
axes[0].grid(True)

# 오른쪽: 정확도 그래프
axes[1].plot(history['train_acc'], label='Train Accuracy', marker='o')
axes[1].plot(history['test_acc'], label='Test Accuracy', marker='s')
axes[1].set_xlabel('Epoch')
axes[1].set_ylabel('Accuracy (%)')
axes[1].set_title('학습 정확도 (높을수록 좋음)')
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.show()

# ============================================================
# 학습 결과 해석
# ============================================================
#
# 좋은 학습의 신호:
# 1. Train Loss와 Test Loss가 함께 감소
# 2. Train Accuracy와 Test Accuracy가 함께 증가
# 3. Train과 Test 성능의 차이가 크지 않음
#
# 과적합(Overfitting)의 신호:
# - Train Accuracy는 높지만 Test Accuracy는 낮음
# - Train Loss는 계속 감소하지만 Test Loss는 증가
# 해결: Dropout 증가, 데이터 증강, 조기 종료
#
# 과소적합(Underfitting)의 신호:
# - Train Accuracy와 Test Accuracy 모두 낮음
# - Loss가 충분히 감소하지 않음
# 해결: 모델 크기 증가, 학습 시간 증가, 학습률 조정
# ============================================================
