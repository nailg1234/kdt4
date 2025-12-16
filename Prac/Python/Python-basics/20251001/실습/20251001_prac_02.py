import numpy as np

# 5. 0~9 범위의 배열에서 짝수는 그대로 두고, 홀수는 홀수 값 × 10으로 변환한 배열을 만드세요
arr5 = np.arange(0, 10)  # [0 1 2 3 4 5 6 7 8 9]
# idxs = np.where(arr5 % 2)
result = np.where(arr5 % 2 == 0, arr5, arr5 * 10)
# arr5[idxs] *= 10
print('문제 5.')
print(result)
print()

# 6. 아래 2차원 배열 에서 20 이상 40 이하인 값만 선택하세요.
# [[10, 25, 30],
# [40, 5, 15],
# [20, 35, 50]]
arr6 = np.array([[10, 25, 30],
                [40, 5, 15],
                [20, 35, 50]])
result = arr6[(arr6 >= 20) & (arr6 <= 40)]
print('문제 6.')
print(result)
print()

# 7. 배열 [1, 2, 3, 4, 5, 6]에서 3의 배수가 아닌 값만 선택하세요.
arr7 = np.array([1, 2, 3, 4, 5, 6])
result = arr7[arr7 % 3 != 0]
print('문제 7.')
# idxs = np.where(arr7 % 3)
print(result)
