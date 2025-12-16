# 배열 인덱싱, 슬라이싱

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
print('원본 배열 arr : \n', arr)

# 팬시 인덱싱 (Fancy indexing)
# indices = [1, 4, 7]
indices = [1, 3, 1, 7, 4, 7]
print('인덱스 [1, 4, 7] 선택 : \n', arr[indices])  # [20 50 80]
print('인덱스 [1, 3, 1, 7, 4, 7] 선택 : \n', arr[indices])  # [20 40 20 80 50 80]

# 양수 인덱스 (0부터 시작)
print('첫번째 요소 (인덱스 0)', arr[0])  # 10
print('2번째 요소 (인덱스 2)', arr[2])  # 30
print('8번째 요소 (인덱스 8)', arr[8])  # 90

arr[0] = 100
print('수정 후 배열', arr)  # [100  20  30  40  50  60  70  80  90]

# 음수 인덱스 (뒤에서 부터)
print('마지막 요소 (인덱스 -1)', arr[-1])  # 90
print('-2번째 요소 (인덱스 -2)', arr[-2])  # 80
print('-8번째 요소 (인덱스 -8)', arr[-8])  # 20

arr[-3] = 400
print('수정 후 배열', arr)  # [100  20  30  40  50  60 400  80  90]

# 배열 슬라이싱

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
print('원본 배열 arr : \n', arr)

print('인덱스 2부터 5까지 (5 제외) : ', arr[2:5])
print('인덱스 처음부터 4까지 (4 제외) : ', arr[:4])
print('인덱스 3부터 마지막 까지 : ', arr[3:])
print('짝수 인덱스만 : \n', arr[::2])
print('홀수 인덱스만 : \n', arr[1::2])

# 슬라이싱으로 값 수정
arr[2:5] = 100
print('수정 후 배열 arr :\n', arr)  # [ 10  20 100 100 100  60  70  80  90]

arr[2:5] = [10, 20, 30]
print('수정 후 배열 arr :\n', arr)  # [ 10  20 100 100 100  60  70  80  90]

# arr[2:5] = [10, 20,] // 오류 발생!
# print('수정 후 배열 arr :\n', arr)

original = np.array([1, 2, 3, 4, 5,])
view = original[1:4]
print('original \n', original)
print('view \n', view)

view[0] = 10
print('original \n', original)  # [1, 10, 3, 4, 5]
print('view \n', view)  # [10, 3, 4]

view[1:] = 20
print('original \n', original)  # [1, 10, 20, 20, 5]
print('view \n', view)  # [10, 20, 20]

# 독립적인 복사본이 필요한 경우
original = np.array([1, 2, 3, 4, 5,])
copy = original[1:4].copy()

copy[0] = 100
print('original \n', original)  # [1 2 3 4 5 ]
print('copy \n', copy)  # [100 3 4]

# 2차원 배열 3 x 3
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print('2차원 배열 : \n', matrix)

print('0,0 요소 : ', matrix[0, 0])  # 1
print('0,0 요소 : ', matrix[2, 2])  # 9
print('0,0 요소 : ', matrix[1, 2])  # 6
# print('0,0 요소 : ', matrix[3, 0])  # Error

print('-1,-2 요소 : ', matrix[-1, -2])  # 8
print('-1,-2 요소 : ', matrix[-1][-2])  # 8(일반 파이썬과 같이도 사용 가능!)

print('첫번째 행 : ', matrix[0])  # [1 2 3]
print('두번째 행 : ', matrix[1])  # [4 5 6]

print('여러 행: \n', matrix[:2])  # [[1 2 3] [4 5 6]]


# 부분 행렬 추출
matrix = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
])

print('matrix[:2, 1:]: \n', matrix[:2, 1:])  # [[2 3 4 5] [7 8 9 10]]
print('matrix[1:3, 1:4]: \n', matrix[1:3, 1:4])  # [[7 8 9] [12 13 14]]
print('matrix[::2, ::2]: \n', matrix[::2, ::2])  # [[1 3 5] [11 13 15]]

row_indices = [0, 2, 3]

print('[0, 2, 3] 행 선택 : \n', matrix[row_indices])


# 특정 요소들 선택(행, 열 인덱스)

row_indices = [0, 2, 2]
col_indices = [3, 2, 3]
print('[0, 2, 3] 행 선택 : \n', matrix[row_indices, col_indices])

arr = np.array([1, 5, 4, 7, 2, 3])
print('4 이상 : ', arr[arr >= 4])  # [5 4 7]

print('2미만, 4 이상', arr[(arr >= 4) | (arr < 2)])  # [1 5 4 7]
print('2이상, 4 이하', arr[(2 <= arr) & (arr <= 4)])  # [4 2 3]


# 2차원 행렬
matrix = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
])

print('9보다 큰 요소들',  matrix[matrix > 9])
print('첫번째 열이 4 이상인 행들\n',  matrix[matrix[:, 0] >= 4])

matrix[matrix > 9] = 10
print(matrix)
