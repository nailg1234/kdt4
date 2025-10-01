# 실습2. 통계 함수 및 집계 연산(2)

import numpy as np

# 4. 아래 배열에서 행별 평균과 열별 평균을 각각 구하세요.
arr = np.array([[10, 20],
                [30, 40],
                [50, 60]])
print('문제 4.')
print('행별 평균 : ', np.mean(arr, axis = 1))
print('열별 평균 : ', np.mean(arr, axis = 0))
print()

# 5. 1차원 배열에서 전체 표준편차를 구하고,
# 각 요소가 평균으로부터 얼마나 떨어져 있는지
# 편차 배열을 만드세요. (값 - 평균)
arr = np.array([2, 4, 4, 4, 5, 5, 7, 9])
print('문제 5.')
print('전체 표준 편차 : ', np.std(arr))
print('편차로 부터의 차이 배열 : ', arr - np.mean(arr))
print()

# 6. 아래 2차원 배열에서 행 단위 누적 합과 열 단위 누적 곱을 각각 구하세요.
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print('문제 6.')
print('행 단위 누적 합 : \n', np.cumsum(arr, axis = 1))
print('열 단위 누적 곱 : \n', np.cumprod(arr, axis = 0))