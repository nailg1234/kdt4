# 실습2. 통계 함수 및 집계 연산(1)
import numpy as np

# 1. 아래 배열의 전체 합계와 평균을 각각 구하세요.
arr = np.array([5, 10, 15, 20])
print('문제 1.')
print('전체 합계 : ', np.sum(arr))
print('전체 평균 : ', np.mean(arr))
print()

# 2. 다음 2차원 배열에서 전체 최소값과 최대값을 구하세요.
arr = np.array([[3, 7, 1],
                [9, 2, 8]])
print('문제 2.')
print('전체 최소값 : ', np.min(arr))
print('전체 최대값 : ', np.max(arr))
print()

# 3. 아래 배열에서 각 열의 합계와 각 행의 합계를 각각 구하세요.
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print('문제 3.')
print('열 합계 : ', np.sum(arr, axis=0))
print('행 합계 : ', np.sum(arr, axis=1))
print()

# 실습2. 통계 함수 및 집계 연산(2)
# 4. 아래 배열에서 행별 평균과 열별 평균을 각각 구하세요.
arr = np.array([[10, 20],
                [30, 40],
                [50, 60]])
print('문제 4.')
print('행별 평균 : ', np.mean(arr, axis=1))
print('행별 평균 : ', np.mean(arr, axis=0))
print()

# 5. 1차원 배열에서 전체 표준편차를 구하고, 각 요소가 평균으로부터 얼마나 떨어져 있는지 편차
# 배열을 만드세요. (값 - 평균)
arr = np.array([2, 4, 4, 4, 5, 5, 7, 9])
arr_std = np.std(arr)
print('문제 5.')
print('표준 편차 : ', arr_std)
print('편차 배열 : \n', arr - arr.mean())
print()

# 6. 아래 2차원 배열에서 행 단위 누적 합과 열 단위 누적 곱을 각각 구하세요.
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print('문제 6.')
print('행 단위 누적 합\n', np.cumsum(arr, axis=1))
print('열 단위 누적 곱\n', np.cumprod(arr, axis=0))