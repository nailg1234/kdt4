# 실습3. NumPy 종합 연습(2)
import numpy as np

# 4. 0~9 난수로 이루어진 (4, 4) 배열을 생성하고, 각각 인덱싱으로 추출해 출력하세요.(for 이용)
# • 주대각선 요소 (왼쪽 위 → 오른쪽 아래)
# • 부대각선 요소 (오른쪽 위 → 왼쪽 아래)
arr = np.random.randint(0, 10, (4, 4))

print('문제 5.')
print('주 대각선 : ', [ele[idx] for idx, ele in enumerate(arr)])
print('부 대각선 : ', [ele[::-1][idx] for idx, ele in enumerate(arr)])
print()
# 5. 0~9 난수로 이루어진 (3, 4, 5) 3차원 배열을 생성하고
# 두 번째 층에서 첫 번째 행과 마지막 열의 값을 출력하세요.

arr = np.random.randint(0, 10, (3, 4, 5))
print('문제 6.')
print('두 번째 층의 첫 행 마지막 열 값:', arr[1, 0, -1])