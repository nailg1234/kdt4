# 실습2. 인덱싱과 슬라이싱(1)
import numpy as np

# 1. 다음 배열에서 2, 4, 6번째 요소를 Fancy Indexing으로 선택하세요.
arr = np.arange(10, 30, 2)
print('문제 1.')
print('원본 \n', arr)
print('2, 4, 6번째 요소', arr[[1, 3, 5]])
print()

# 2. 3x3 배열에서 왼쪽 위 → 오른쪽 아래 대각선의 요소만 인덱싱으로 추출하세요.
arr = np.arange(1, 10).reshape(3, 3)
print('문제 2.')
print('원본 \n', arr)
for i,row in enumerate(arr):
    print(row[i], end=' ')
print()
print()

# 3. 3x4 배열에서 마지막 열만 선택해 모두 -1로 변경하세요.
arr = np.arange(1, 13).reshape(3, 4)
print('문제 3.')
arr[:, -1] = -1
print(arr)
print()

# 4. 4x4 배열에서 행을 역순, 열을 역순으로 각각 슬라이싱해 출력하세요.
arr = np.arange(1, 17).reshape(4, 4)
print('문제 4.')
print('행 역순 \n', arr[::-1])
print('열 역순 \n', arr[:, ::-1])
print()

# 실습2. 인덱싱과 슬라이싱(2)
# 5. 4x5 배열에서 가운데 2x3 부분을 슬라이싱한 뒤 copy()를 이용해 독립 배열을 만드세요.
arr = np.arange(1, 21).reshape(4, 5)
result = arr[1:3, 1:4]
print('문제 5.')
print('원본 \n', arr)
print('독립 배열 \n', result.copy())
print()

# 6. 3x4 배열에서 짝수이면서 10 이상인 값만 선택하세요.(&을 활용)
arr = np.array([[ 4, 9, 12, 7], [10, 15, 18, 3], [ 2, 14, 6, 20]])
print('문제 6.')
print(arr[(arr % 2 == 0) & (arr >= 10)])
print()

# 7. 5x5 배열에서 2, 4번째 행을 선택하고, 선택된 행에서 열 순서를 [4, 0, 2]로 재배치하세요.
arr = np.arange(1, 26).reshape(5, 5)
print('문제 7.')
print('원본\n', arr)
print(arr[1:4:2, [4, 0, 2]])
print()

# 실습2. 인덱싱과 슬라이싱(3)
# 8. 5x3 배열에서 각 행의 첫 번째 값이 50 이상인 행만 Boolean Indexing으로 선택하세요.
arr = np.array([[10, 20, 30], [55, 65, 75], [40, 45, 50], [70, 80, 90], [15, 25, 35]])
print('문제 8.')
print('원본\n', arr)
print('첫번째 50 이상 \n', arr[arr[:, 0] >= 50])
print()

# 9. 4x4 배열에서 (0,1), (1,3), (2,0), (3,2) 위치의 요소를 한 번에 선택하세요.
arr = np.arange(1, 17).reshape(4, 4)
print('문제 9.')
print('원본\n', arr)
print('한번에 선택\n', arr[[0,1,2,3], [1,3,0,2]])
print()

# 10. 3차원 배열 (2, 3, 4)에서 모든 블록에서 두 번째 열만 추출해 새로운 2차원 배열 (2, 3)을 만
# 드세요.
arr3d = np.arange(24).reshape(2, 3, 4)
print('문제 10.')
print('원본\n', arr3d)
print('새로운 배열\n', arr3d[:,:,1])
print('새로운 배열\n', arr3d[:,:,1].shape)