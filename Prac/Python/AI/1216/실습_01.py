from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
import numpy as np

# 와인 데이터셋으로 분할 연습
wine = load_wine()
x, y = wine.data, wine.target

print(f"전체 데이터: {x.shape}")
print(f"클래스: {np.unique(y)}")  # [0, 1, 2]

# 1. 훈련:테스트 = 70:30으로 분할
# 2. stratify 적용
# 3. 각 세트의 클래스 분포 확인

x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.3,  # 테스트 비율
    stratify=y,  # 클래스 비율 유지!
    random_state=42  # 재현성을 위한 시도
)

print(f'전체 클래스 비율: {np.bincount(y)}')
print(f'훈련 클래스 비율: {np.bincount(y_train)}')
print(f'테스트 클래스 비율: {np.bincount(y_test)}')
