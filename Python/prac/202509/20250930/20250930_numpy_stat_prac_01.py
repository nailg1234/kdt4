# 실습2. 통계 함수 및 집계 연산(1)

import numpy as np

# 1. 아래 배열의 전체 합계와 평균을 각각 구하세요.
arr = np.array([5, 10, 15, 20])
print('문제 1.')
print('합계 : ', np.sum(arr))
print('평균 : ', np.mean(arr))
print()

# 2. 다음 2차원 배열에서 전체 최소값과 최대값을 구하세요.
arr = np.array([[3, 7, 1],
                [9, 2, 8]])
print('문제 2.')
print('전체 최소 값 : ', np.min(arr))
print('전체 최대 값 : ', np.max(arr))
print()

# 3. 아래 배열에서 각 열의 합계와 각 행의 합계를 각각 구하세요.
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print('문제 3.')
print('열의 합계 : ', np.sum(arr, axis = 0))
print('행의 합계 : ', np.sum(arr, axis = 1))