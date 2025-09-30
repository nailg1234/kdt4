# 실습3. NumPy 종합 연습(3)
import numpy as np

# 6. 35부터 74까지의 순차적인 수로 이루어진 1차원 배열을 만들고 10x4 행렬로 변환 후 출력해
# 주세요.
arr = np.arange(35, 75)
arr1 = arr.reshape(10, 4)
print('문제 6. \n', arr1)
print()
# 7. 6번에서 만든 배열을 맨 끝의 행부터 역순으로 출력해주세요.
arr2 = arr1[::-1]
print('문제 7. \n', arr2)
print()
# 8. 6번에서 만든 배열 중 두 번째 행부터 마지막 직전 행까지,
# 세번째 열부터 마지막 열까지 슬라이싱해서 출력해주세요.

arr3 = arr1[1:-1, 2:]
print('문제 8. \n', arr3)