# 실습1. 배열 연산(1)
import numpy as np

# 1. 다음 배열을 생성하고, 모든 요소에 3을 더하세요.
arr = np.array([1, 2, 3, 4])
print('문제 1.')
print('원본\n', arr)
print('더하기 3\n', arr + 3)
print()

# 2. 아래 2차원 배열에서 각 요소를 -1로 곱한 새로운 배열을 만드세요.
arr = np.array([[5, 10],
                [15, 20]])
print('문제 2.')
print('원본\n', arr)
print('곱하기 -1\n', arr * -1)
print()

# 3. 아래 두 배열의 요소별 곱셈과 나눗셈 결과를 각각 출력하세요.
arr1 = np.array([2, 4, 6])
arr2 = np.array([1, 2, 3])
print('문제 3.')
print('곱셈\n', arr1 * arr2)
print('나눗셈\n', arr1 / arr2)
print()

# 실습1. 배열 연산(1)
# 4. 아래 배열에서 모든 요소를 최대값 100으로 만들기 위해 필요한 값을 더한 결과 배열을 브로드
# 캐스팅으로 만드세요.
arr = np.array([[95, 97],
                [80, 85]])
print('문제 4.')
arr1 = 100 - arr
print(arr1)
print(arr + arr1)
print()

# 5. 아래 2차원 배열에서 각 행에 다른 값을 곱하여 새로운 배열을 만드세요.(브로드캐스팅 이용)
# • 첫 번째 행은 10을 곱하고
# • 두 번째 행은 100을 곱해야 합니다.
arr = np.array([[1, 2, 3], [4, 5, 6]])
arr1 = np.array([[10], [100]])
print('문제 5.')
print(arr * arr1)
print()

# 실습1. 배열 연산(1)
# 6. 아래 배열에서 각 행마다 다른 스칼라 값을 더하기 위해
# • 1차원 배열을 만들어 브로드캐스팅 연산을 수행하세요.
# • 첫 번째 행에 100, 두 번째 행에 200, 세 번째 행에 300을 더하세요.
arr = np.array([[10, 20],
                [30, 40],
                [50, 60]])

arr1 = np.array([100,200,300])
arr1 = arr1.reshape(3, -1)
print('문제 6.')
print(arr + arr1)
