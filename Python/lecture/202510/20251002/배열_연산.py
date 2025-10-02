# 실습1. 배열 연산(1)
import numpy as np

# 1. 다음 배열을 생성하고, 모든 요소에 3을 더하세요.
arr = np.array([1, 2, 3, 4])
result = arr + 3
print('문제 1.\n', result)
print()

# 2. 아래 2차원 배열에서 각 요소를 -1로 곱한 새로운 배열을 만드세요.
arr = np.array([[5, 10],
                [15, 20]])
result = arr * -1
print('문제 2.\n', result)
print()

# 3. 아래 두 배열의 요소별 곱셈과 나눗셈 결과를 각각 출력하세요.
arr1 = np.array([2, 4, 6])
arr2 = np.array([1, 2, 3])
mul1 = arr1 * arr2
div1 = arr1 / arr2
print('문제 3.\n', mul1)
print('문제 3.\n', div1)
print()

# 4. 아래 배열에서 모든 요소를 최대값 100으로 만들기 위해 필요한 값을 더한 결과 배열을 브로드
# 캐스팅으로 만드세요.
arr = np.array([[95, 97],
                [80, 85]])
add_val = 100 - arr
print('문제 4.\n', add_val)
result = arr + add_val
print(result)
print()

# 5. 아래 2차원 배열에서 각 행에 다른 값을 곱하여 새로운 배열을 만드세요.(브로m드캐스팅 이용)
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
# • 첫 번째 행은 10을 곱하고
# • 두 번째 행은 100을 곱해야 합니다.
mul_val = np.array([[10], [100]])
result = arr * mul_val
print('문제 5.\n', result)
print()

# 6. 아래 배열에서 각 행마다 다른 스칼라 값을 더하기 위해
# • 1차원 배열을 만들어 브로드캐스팅 연산을 수행하세요.
# • 첫 번째 행에 100, 두 번째 행에 200, 세 번째 행에 300을 더하세요.
arr = np.array([[10, 20],
                [30, 40],
                [50, 60]])

add_val = np.array([100, 200, 300])
reshaped = add_val.reshape(-1, 1)
result = arr + reshaped
print('문제 6.\n', result)
