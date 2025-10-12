# 실습3. NumPy 종합 연습(1)
import numpy as np
# 1. 0부터 24까지 정수를 가진 배열을 만들고, (5, 5) 배열로 변환한 뒤 가운데 행(3번째 행)과 가
# 운데 열(3번째 열)을 각각 1차원 배열로 출력하세요.
arr = np.arange(0, 25).reshape(5, 5)
print('문제 1.')
print('원본\n', arr)
print('가운데 행 : ', arr[2])
print('가운데 열 : ', arr[:, 2])
print()

# 2. 0~99 난수로 이루어진 (10, 10) 배열을 생성하고,
# 짝수 인덱스의 행만 선택하여 출력하세요.
arr = np.random.default_rng().integers(low=0, high=100, size=(10, 10))
print('문제 2.')
print('원본\n', arr)
print('짝수 인덱스 행\n', arr[::2])
print()

# 3. 0부터 49까지 정수를 가진 배열을 (5, 10) 배열로 변환한 후, 2행 3열부터 4행 7열까지의 부분 배열을 추출하세요.
arr = np.arange(0, 50).reshape(5, 10)
print('문제 3.')
print('원본\n', arr)
print(arr[1:4, 2:8])
print()

# 실습3. NumPy 종합 연습(2)
# 4. 0~9 난수로 이루어진 (4, 4) 배열을 생성하고, 각각 인덱싱으로 추출해 출력하세요.(for 이용)
# • 주대각선 요소 (왼쪽 위 → 오른쪽 아래)
# • 부대각선 요소 (오른쪽 위 → 왼쪽 아래)
arr = np.random.randint(0, 10, size=(4, 4))
print('문제 4.')
print('원본\n', arr)
arr1 = [ele[idx] for idx, ele in enumerate(arr)]
arr2 = [ele[::-1][idx] for idx, ele in enumerate(arr)]
print('주 대각선 : ', arr1)
print('부 대각선 : ', arr2)
print()

# 5. 0~9 난수로 이루어진 (3, 4, 5) 3차원 배열을 생성하고, 두 번째 층에서 첫 번째 행과 마지막
# 열의 값을 출력하세요.
arr = np.random.randint(0, 10, size=(3, 4, 5))
print('문제 5.')
print('원본\n', arr)
print('첫번째 행 마지막 열\n', arr[1, 0, -1])
print()

# 실습3. NumPy 종합 연습(3)
# 6. 35부터 74까지의 순차적인 수로 이루어진 1차원 배열을 만들고 10x4 행렬로 변환 후 출력해
# 주세요.
arr = np.arange(35, 75).reshape(10, 4)
print('문제 6.')
print('원본\n', arr)
print()

# 7. 6번에서 만든 배열을 맨 끝의 행부터 역순으로 출력해주세요.
print('문제 7.')
print('역순 배열\n', arr[::-1])
print()

# 8. 6번에서 만든 배열 중 두 번째 행부터 마지막 직전 행까지, 세번째 열부터 마지막 열까지 슬라
# 이싱해서 출력해주세요.
print('문제 8.')
print('부분 배열\n', arr[1:-1, 2:])
print()

# 실습3. NumPy 종합 연습(4)
# 9. 1부터 50까지의 난수로 된 5x6 배열을 만들고, 배열에서 짝수만 선택하여 출력하는 코드를
# 작성하세요.
arr = np.random.randint(1, 51, size=(5,6))
print('문제 9.')
print('원본\n', arr)
print('짝수만\n', arr[arr % 2 == 0])
print()

# 10. 0부터 99까지의 정수로 이루어진 (10, 10) 배열을 생성한 후,
# [1, 3, 5]번째 행과 [2, 4, 6]번째 열의 교차하는 원소들만 선택하여 출력하세요.
arr = np.arange(0, 100).reshape(10, 10)
print('문제 10.')
print('원본\n', arr)
print('1,3,5 2,4,6 원소\n', arr[[1,3,5]][:, [2,4,6]])
print()

# 11. 0~9 난수로 이루어진 1차원 배열(길이 15)을 생성하고,
# 짝수 인덱스 위치에 있는 값들 중에서 5 이상인 값만 선택해 출력하세요.
arr = np.random.randint(0, 10, size=15)
print('문제 11.')
print('원본\n', arr)
print('원본\n', arr[::2][arr[::2]>=5])
