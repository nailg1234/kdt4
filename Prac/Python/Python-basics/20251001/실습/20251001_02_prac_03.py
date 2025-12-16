# 실습3. 배열의 정렬(1)
import numpy as np

# 1. 아래의 1차원 배열을 오름차순과 내림차순으로 각각 정렬하는 코드를 작성하세요.
arr = np.array([7, 2, 9, 4, 5])
sort_arr = np.sort(arr)
sort_reverse_arr = np.sort(arr)[::-1]
print('문제 1.')
print('오름차순 : ', sort_arr)
print('내림차순 : ', sort_reverse_arr)
print()

# 2. 아래의 2차원 배열에서 각 행(row) 별로 오름차순 정렬된 배열을 구하세요.
arr = np.array([[9, 2, 5],[3, 8, 1]])
print('문제 2.')
sort_arr = np.sort(arr, axis = 1)
print('행별 오름차순 : \n', sort_arr)
print()

# 3. 아래의 1차원 배열에서 정렬 결과(오름차순)가 되는 인덱스 배열을 구하고,
# 그 인덱스를 이용해 원본 배열을 직접 재정렬하는 코드를 작성하세요.
arr = np.array([10, 3, 7, 1, 9])
sort_arg_arr = np.argsort(arr)
print('문제 3.')
print('정렬 인덱스 배열 : \n', sort_arg_arr)
print('정렬 인덱스로 원본배열 정렬 : \n', arr[sort_arg_arr])
print()

# 4. 아래 2차원 배열을 열(column) 기준(axis=0)으로 오름차순 정렬된 배열을 구하세요.
arr = np.array([[4, 7, 2],
                [9, 1, 5],
                [6, 8, 3]])
print('문제 4.')
print(np.sort(arr, axis = 0))