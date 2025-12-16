from sklearn.model_selection import train_test_split
import numpy as np

x = np.array([[1, 2], [3, 4], [5, 6], [7, 8],
              [9, 10], [11, 12], [13, 14], [15, 16],
              [17, 18], [19, 20]])
y = np.array([0, 0, 0, 1, 1, 0, 1, 1, 0, 1])

x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.2,  # 테스트 20%
    random_state=42  # 재현성 확보
)

print(f'훈련 데이터: {len(x_train)}')  # 훈련 데이터: 8
print(f'테스트 데이터: {len(x_test)}')  # 테스트 데이터: 2


# 1단계: (훈련+검증) / 테스트
x_temp, x_test, y_temp, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# 2단계: 훈련 / 검증
x_train, x_val, y_train, y_val = train_test_split(
    x_temp, y_temp, test_size=0.25, random_state=42
)

print(f'훈련 데이터: {len(x_train)}')  # 훈련 데이터: 6
print(f'검증 데이터: {len(x_val)}')  # 검증 데이터: 2
print(f'테스트 데이터: {len(x_test)}')  # 테스트 데이터: 2
