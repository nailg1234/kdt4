from sklearn.model_selection import train_test_split
import numpy as np

# 계층 분할(Stratified)

# 클래스 비율을 유지하면서 분할

# 불균형 데이터 예시
x = np.array([[1, 2], [3, 4], [5, 6], [7, 8],
              [9, 10], [11, 12], [13, 14], [15, 16],
              [17, 18], [19, 20]])
y = np.array([0, 0, 0, 0, 0, 0, 0, 1, 1, 1])  # 7 : 3

# stratify 옵션 사용
x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.2,  # 테스트 비율 20%
    stratify=y,  # 클래스 비율 유지!
    random_state=42  # 재현성을 위한 시드
)

print(f'전체 클래스 비율: {np.bincount(y)}')  # 전체 클래스 비율: [7 3]
print(f'훈련 클래스 비율: {np.bincount(y_train)}')  # 훈련 클래스 비율: [6 2]
print(f'테스트 클래스 비율: {np.bincount(y_test)}')  # 테스트 클래스 비율: [1 1]
