from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np

# 붓꽃 데이터 로드
iris = load_iris()
x = iris.data  # 특성 (꽃잎, 꽃받침 크기)
y = iris.target  # 라벨 (품종)

print(f'전체 데이터: {x.shape}')  # 전체 데이터: (150, 4)
print(f'클래스: {np.unique(y)}')  # 클래스: [0 1 2]

# 분할
x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.2,  # 테스트 비율 20%
    stratify=y,  # 클래스 비율 유지!
    random_state=42  # 재현성을 위한 시드
)

print(f'훈련 데이터: {len(x_train)}')  # 훈련 데이터: 120
print(f'테스트 데이터: {len(x_test)}')  # 테스트 데이터: 30

print(f'전체 클래스 비율: {np.bincount(y)}')  # 전체 클래스 비율: [50 50 50]
print(f'훈련 클래스 비율: {np.bincount(y_train)}')  # 훈련 클래스 비율: [40 40 40]
print(f'테스트 클래스 비율: {np.bincount(y_test)}')  # 테스트 클래스 비율: [10 10 10]
