import numpy as np

# 1. 1차원 배열 [5, 12, 18, 7, 30, 25]에서 10보다 크고 20보다 작은 값만 필터링
# 불리언 인덱싱 사용
arr1 = np.array([5, 12, 18, 7, 30, 25])
print('문제 1.')
result = arr1[(arr1 > 10) & (arr1 < 20)]
print(result)
print()

# 2. 배열 [10, 15, 20 , 25, 30, 35]에서 15 이하이거나 30이상인 값만 선택
arr2 = np.array([10, 15, 20, 25, 30, 35])
print('문제 2.')
result = arr2[(arr2 <= 15) | (arr2 >= 30)]
print(result)
print()

# 3. 배열 [3, 8, 15, 6, 2, 20]에서 10 이상인 값을 모두 0으로 변경
print('문제 3.')
arr3 = np.array([3, 8, 15, 6, 2, 20])
arr3[arr3 >= 10] = 0
# idxs = np.where(arr3 >= 10)
# arr3[idxs] = 0
print(arr3)
print()

# 4. 배열 [7, 14, 21, 28, 35]에서 20 이상인 값은 "High", 나머지는 "Low"로 표시하는 새로운 배열 생성
# 삼항 연산자
print('문제 4.')
arr4 = np.array([[7, 14, 21, 28, 35]])
result = np.where(arr4 >= 20, 'High', 'Low')
print(result)
