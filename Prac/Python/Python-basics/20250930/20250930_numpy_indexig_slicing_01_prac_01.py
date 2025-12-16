# 실습2. 인덱싱과 슬라이싱(1)
# 1. 다음 배열에서 2, 4, 6번째 요소를 Fancy Indexing으로 선택하세요.
# • arr = np.arange(10, 30, 2)
# 2. 3x3 배열에서 왼쪽 위 → 오른쪽 아래 대각선의 요소만 인덱싱으로 추출하세요.
# • arr = np.arange(1, 10).reshape(3, 3)
# 3. 3x4 배열에서 마지막 열만 선택해 모두 -1로 변경하세요.
# • arr = np.arange(1, 13).reshape(3, 4)
# 4. 4x4 배열에서 행을 역순, 열을 역순으로 각각 슬라이싱해 출력하세요.
# • arr = np.arange(1, 17).reshape(4, 4)


import numpy as np
arr = np.arange(10, 30, 2)
print('원본 배열 \n', arr)
print('1. 다음 배열에서 2, 4, 6 번째 요소\n', arr[[1, 3, 5]])  # [12 16 20]

arr = np.arange(1, 10).reshape(3, 3)
print('원본 배열 \n', arr)
# print('2. 3x3 배열에서 왼쪽 위 → 오른쪽 아래 대각선의 요소', arr[0, 0], arr[-1, -1])
print('2. 3x3 배열에서 왼쪽 위 → 오른쪽 아래 대각선의 요소\n', arr[[0, 1, 2], [0, 1, 2]])

arr = np.arange(1, 13).reshape(3, 4)
print('원본 배열 \n', arr)
# arr[-1] = -1
arr[:, -1] = -1
print('3. 3x4 배열에서 마지막 열만 -1로 변경 원본 배열\n', arr)

arr = np.arange(1, 17).reshape(4, 4)
print('원본 배열 \n', arr)
# print('4. 4x4 배열에서 행을 역순, 열을 역순으로 각각 슬라이싱\n', arr[::-1, ::-1])
print('4. 4x4 배열에서 행을 역순, 열을 역순으로 각각 슬라이싱\n', arr[::-1, :])
print('4. 4x4 배열에서 행을 역순, 열을 역순으로 각각 슬라이싱\n', arr[:, ::-1])
