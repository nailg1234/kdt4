# NumPy 차원 추가, 제거, 배열 조작 완전 가이드

import numpy as np

# ============================================================================
# 1. 차원 추가: np.newaxis
# ============================================================================
'''
개념 설명:
    - np.newaxis: 배열에 새로운 차원(축)을 추가
    - 1차원 배열을 2차원으로 변환할 때 주로 사용
    - 브로드캐스팅이나 행렬 연산을 위해 차원을 맞출 때 필요
    
사용 목적:
    - 행 벡터 생성: (5,) → (1, 5)
    - 열 벡터 생성: (5,) → (5, 1)
    - 차원 호환을 위한 shape 조정
'''

arr = np.array([1, 2, 3, 4, 5])
print('원본 배열:', arr)
print('원본 shape:', arr.shape)  # (5,) - 1차원 배열
print()

# 행 벡터로 변환: 앞에 차원 추가
# [1, 2, 3, 4, 5] → [[1, 2, 3, 4, 5]]
row_vec = arr[np.newaxis, :]
print('행 벡터:\n', row_vec)
print('행 벡터 shape:', row_vec.shape)  # (1, 5) - 1행 5열
print()

# 열 벡터로 변환: 뒤에 차원 추가
# [1, 2, 3, 4, 5] → [[1], [2], [3], [4], [5]]
col_vec = arr[:, np.newaxis]
print('열 벡터:\n', col_vec)
print('열 벡터 shape:', col_vec.shape)  # (5, 1) - 5행 1열
print()

# ============================================================================
# 2. 차원 추가: np.expand_dims
# ============================================================================
'''
개념 설명:
    - np.expand_dims: 지정한 위치에 새로운 차원 추가
    - axis 매개변수로 어디에 차원을 추가할지 지정
    - np.newaxis보다 명시적이고 가독성이 좋음
    
axis 이해:
    - axis=0: 맨 앞에 차원 추가 (행 추가)
    - axis=1: 두 번째 위치에 차원 추가 (열 추가)
    - axis=-1: 맨 뒤에 차원 추가
'''

arr = np.array([1, 2, 3, 4, 5])
print('원본:', arr, '- shape:', arr.shape)  # (5,)
print()

# axis=0: 첫 번째 축에 차원 추가
# (5,) → (1, 5)
arr_expanded0 = np.expand_dims(arr, axis=0)
print('axis=0:\n', arr_expanded0)
print('shape:', arr_expanded0.shape)  # (1, 5)
print()

# axis=1: 두 번째 축에 차원 추가
# (5,) → (5, 1)
arr_expanded1 = np.expand_dims(arr, axis=1)
print('axis=1:\n', arr_expanded1)
print('shape:', arr_expanded1.shape)  # (5, 1)
print()

# ============================================================================
# 3. 차원 제거: np.squeeze
# ============================================================================
'''
개념 설명:
    - np.squeeze: 크기가 1인 차원을 제거
    - (1, 5, 1) → (5,) 처럼 불필요한 차원 제거
    - axis를 지정하면 특정 차원만 제거 가능
    
사용 목적:
    - 신경망 출력에서 배치 차원 제거
    - 불필요하게 추가된 차원 정리
    - 차원 단순화로 연산 효율 개선
'''

arr = np.array([[[1, 2, 3]]])  # 3차원 배열
print('원본:\n', arr)
print('원본 shape:', arr.shape)  # (1, 1, 3)
print()

# 모든 크기 1인 차원 제거
# (1, 1, 3) → (3,)
squeezed = np.squeeze(arr)
print('squeeze 후:\n', squeezed)
print('shape:', squeezed.shape)  # (3,)
print()

# 특정 축만 제거: axis=0
# (1, 1, 3) → (1, 3)
squeezed0 = np.squeeze(arr, axis=0)
print('axis=0 squeeze:\n', squeezed0)
print('shape:', squeezed0.shape)  # (1, 3)
print()

# 주의: 크기가 1이 아닌 차원을 squeeze하면 에러
# squeezed2 = np.squeeze(arr, axis=2)  # ValueError: 크기가 1이 아님
print()

# ============================================================================
# 4. 배열 평탄화 (Flattening)
# ============================================================================
'''
개념 설명:
    - flatten: 다차원 배열을 1차원으로 변환
    - 항상 복사본(copy)을 반환 - 원본은 변경되지 않음
    - 메모리를 더 사용하지만 안전함
    
    - ravel: 다차원 배열을 1차원으로 변환
    - 가능하면 뷰(view)를 반환 - 원본과 메모리 공유
    - 빠르지만 원본이 변경될 수 있어 주의 필요
    
선택 기준:
    - 원본 보호 필요 → flatten() 사용
    - 성능 중요 → ravel() 사용 (단, 의도치 않은 변경 주의)
'''

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print('원본 2차원 배열:')
print(arr)
print()

# flatten: 복사본 반환
flattened = arr.flatten()
print('flatten 결과:', flattened)  # [1 2 3 4 5 6 7 8 9]

# flatten으로 만든 배열 수정 → 원본 영향 없음
flattened[0] = 999
print()
print('원본 배열 (변경 없음):')
print(arr)  # 원본은 그대로 1
print('flatten 배열:', flattened)  # 999로 변경됨
print()

# ravel: 뷰 반환 (원본 메모리 공유)
raveled = arr.ravel()
print('ravel 결과:', raveled)

# ravel로 만든 배열 수정 → 원본도 변경됨!
raveled[0] = 999
print()
print('원본 배열 (변경됨!):')
print(arr)  # 원본도 999로 변경됨
print('ravel 배열:', raveled)
print()

# ravel을 사용하되 복사본이 필요한 경우
raveled_copy = arr.ravel().copy()
raveled_copy[1] = 888

print('원본 배열:')
print(arr)  # 999는 유지, 888은 영향 없음
print('ravel().copy() 배열:', raveled_copy)
print()

# ============================================================================
# 5. 고유값 찾기: np.unique
# ============================================================================
'''
개념 설명:
    - np.unique: 배열에서 중복을 제거하고 고유한 값만 반환
    - 자동으로 정렬된 결과 반환
    - 다양한 옵션으로 추가 정보 제공
    
매개변수:
    - return_index=True: 각 고유값의 첫 등장 인덱스
    - return_inverse=True: 원본을 고유값 인덱스로 변환하는 배열
    - return_counts=True: 각 고유값의 등장 횟수
'''

arr = np.array([1, 2, 3, 2, 1, 3, 2, 3, 1, 4, 2, 5, 3, 12, 5])
print('원본 배열:', arr)
print()

# 기본 사용: 중복 제거 + 정렬
uniq = np.unique(arr)
print('고유값만:', uniq)  # [1 2 3 4 5 12]
print()

# 모든 정보 반환
uniq, idx, inv, cnt = np.unique(arr,
                                return_index=True,
                                return_inverse=True,
                                return_counts=True)

print('고유값:', uniq)                    # [1 2 3 4 5 12]
print('첫 등장 인덱스:', idx)            # [0 1 2 9 11 13]
print('원본→고유값 인덱스:', inv)        # 원본 각 요소가 고유값 배열의 몇 번째인지
print('등장 횟수:', cnt)                 # [3 4 4 1 2 1]

# inverse 이해하기:
# 원본 [1, 2, 3, 2, 1, ...]
# → inverse [0, 1, 2, 1, 0, ...] (고유값 배열에서의 인덱스)
# uniq[inv] 하면 원본 배열을 복원할 수 있음
print()

# ============================================================================
# 6. 배열 결합 (Concatenation)
# ============================================================================
'''
개념 설명:
    - np.concatenate: 여러 배열을 하나로 연결
    - 같은 차원의 배열들을 특정 축(axis)을 따라 이어붙임
    - 결합할 배열들은 결합 축을 제외한 나머지 차원이 일치해야 함
    
axis 이해:
    - axis=0: 세로 방향 결합 (행 추가)
    - axis=1: 가로 방향 결합 (열 추가)
'''

# 1차원 배열 결합
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([7, 8, 9])

concat_1d = np.concatenate([a, b, c])
print('1차원 배열 결합:', concat_1d)  # [1 2 3 4 5 6 7 8 9]
print()

# 2차원 배열 결합
A = np.array([
    [1, 2, 3],
    [3, 4, 5]
])
B = np.array([
    [5, 3, 5]
])

print('A shape:', A.shape)  # (2, 3)
print('B shape:', B.shape)  # (1, 3)
print()

# axis=0: 세로 방향 결합 (행 추가)
# A의 밑에 B를 붙임
concat_v = np.concatenate([A, B], axis=0)
print('axis=0 (수직 결합):')
print(concat_v)
print('결과 shape:', concat_v.shape)  # (3, 3)
print()

# axis=1: 가로 방향 결합 (열 추가)
# 주의: A는 (2, 3), B는 (1, 3)이므로 axis=1로 결합 불가
# 행의 개수가 일치하지 않아 에러 발생
# concat_h = np.concatenate([A, B], axis=1)  # ValueError
print()

# ============================================================================
# 7. vstack, hstack - 편리한 결합 함수
# ============================================================================
'''
개념 설명:
    - vstack: 수직(vertical) 스택 - axis=0과 동일
    - hstack: 수평(horizontal) 스택 - axis=1과 동일
    - concatenate보다 직관적인 이름
'''

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# vstack: 위아래로 쌓기
# [[1, 2, 3],
#  [4, 5, 6]]
vstacked = np.vstack([a, b])
print('vstack (수직):')
print(vstacked)
print('shape:', vstacked.shape)  # (2, 3)
print()

# hstack: 좌우로 이어붙이기
# [1, 2, 3, 4, 5, 6]
hstacked = np.hstack([a, b])
print('hstack (수평):')
print(hstacked)
print('shape:', hstacked.shape)  # (6,)
print()

# ============================================================================
# 8. 배열 분할: np.split
# ============================================================================
'''
개념 설명:
    - np.split: 하나의 배열을 여러 개의 작은 배열로 분할
    - 데이터를 배치로 나누거나 훈련/검증 세트로 분리할 때 사용
    
분할 방법:
    1. 균등 분할: 정수로 개수 지정
    2. 인덱스 분할: 특정 위치에서 자르기
'''

arr = np.arange(12)  # [0 1 2 3 4 5 6 7 8 9 10 11]
print('원본 배열:', arr)
print()

# 균등 분할: 3개의 동일한 크기로 분할
# 12개 요소를 3개로 나누면 각 4개씩
splits_equal = np.split(arr, 3)
print('3개로 균등 분할:', splits_equal)
for idx, sub in enumerate(splits_equal, 1):
    print(f'{idx}번째 조각:', sub)
print()

# 인덱스 분할: [0:3], [3:7], [7:]
# 인덱스 3과 7에서 자르기
splits_idx = np.split(arr, [3, 7])
for idx, sub in enumerate(splits_idx, 1):
    print(f'{idx}번째 조각:', sub)
print()

# 2차원 배열 분할
arr = np.arange(24).reshape(4, 6)
print('2차원 배열 (4×6):')
print(arr)
print()

# axis=0: 행 방향 분할 (가로로 자르기)
# 4행을 2개로 나누면 각 2행씩
row_splits = np.split(arr, 2, axis=0)
print('행 방향 분할 (axis=0):')
for i, sub in enumerate(row_splits, 1):
    print(f'{i}번째 조각:\n', sub)
print()

# axis=1: 열 방향 분할 (세로로 자르기)
# 6열을 2개로 나누면 각 3열씩
col_splits = np.split(arr, 2, axis=1)
print('열 방향 분할 (axis=1):')
for i, sub in enumerate(col_splits, 1):
    print(f'{i}번째 조각:\n', sub)
print()

# ============================================================================
# 9. 배열 정렬: np.sort
# ============================================================================
'''
개념 설명:
    - np.sort(): 정렬된 복사본 반환 (원본 유지)
    - arr.sort(): 원본 배열을 직접 정렬 (in-place)
    
axis 매개변수:
    - axis=0: 각 열을 독립적으로 정렬
    - axis=1: 각 행을 독립적으로 정렬
    - axis=None: 평탄화 후 전체 정렬
'''

arr = np.array([3, 1, 2, 5, 4, 2])
print('원본:', arr)

# 복사본 정렬 (원본 유지)
sorted_copy = np.sort(arr)
print('정렬된 복사본:', sorted_copy)
print('원본 (변경 없음):', arr)
print()

# 원본 직접 정렬
arr.sort()
print('원본 정렬 후:', arr)
print()

# 2차원 배열 정렬
arr2 = np.array([
    [2, 1, 5],
    [3, 2, 1]
])
print('원본 2차원 배열:')
print(arr2)
print()

# axis=0: 각 열을 독립적으로 정렬
# 첫 번째 열 [2, 3] → [2, 3]
# 두 번째 열 [1, 2] → [1, 2]
# 세 번째 열 [5, 1] → [1, 5]
sorted_axis0 = np.sort(arr2, axis=0)
print('axis=0 정렬 (열 방향):')
print(sorted_axis0)
print()

# axis=1: 각 행을 독립적으로 정렬
# 첫 번째 행 [2, 1, 5] → [1, 2, 5]
# 두 번째 행 [3, 2, 1] → [1, 2, 3]
sorted_axis1 = np.sort(arr2, axis=1)
print('axis=1 정렬 (행 방향):')
print(sorted_axis1)
print()

# axis=None: 평탄화 후 전체 정렬
sorted_None = np.sort(arr2, axis=None)
print('axis=None 정렬 (전체):')
print(sorted_None)  # [1 1 2 2 3 5]
print()

# ============================================================================
# 10. 정렬 인덱스: np.argsort
# ============================================================================
'''
개념 설명:
    - np.argsort: 정렬 후의 인덱스를 반환
    - 원본 배열의 어떤 요소가 정렬 후 어디로 가는지 알려줌
    - 간접 정렬에 유용 (다른 배열을 같은 순서로 정렬할 때)
    
활용:
    - 점수로 정렬하되 이름도 함께 정렬
    - 여러 배열을 하나의 기준으로 동시 정렬
'''

names = np.array(['김철수', '이영희', '박민수', '정수진', '최동욱'])
scores = np.array([85, 92, 78, 95, 88])

print('원본 데이터:')
for name, score in zip(names, scores):
    print(f'{name}: {score}점')
print()

# 점수 기준으로 정렬 인덱스 구하기
# argsort는 기본적으로 오름차순이므로 [::-1]로 내림차순 변환
sorted_idx = np.argsort(scores)[::-1]
print('정렬 인덱스 (점수 높은 순):', sorted_idx)
print()

# 인덱스를 사용하여 이름과 점수를 함께 정렬
print('점수 순위:')
for rank, idx in enumerate(sorted_idx, 1):
    print(f'{rank}위: {names[idx]} - {scores[idx]}점')

# 출력 예시:
# 1위: 정수진 - 95점
# 2위: 이영희 - 92점
# 3위: 최동욱 - 88점
# 4위: 김철수 - 85점
# 5위: 박민수 - 78점

print()

# ============================================================================
# 핵심 개념 정리
# ============================================================================
'''
1. 차원 조작:
   - 추가: np.newaxis, np.expand_dims
   - 제거: np.squeeze
   - 평탄화: flatten (복사본), ravel (뷰)
   
2. 배열 결합:
   - concatenate: axis 지정하여 결합
   - vstack: 수직 결합 (행 추가)
   - hstack: 수평 결합 (열 추가)
   
3. 배열 분할:
   - split: 균등 분할 또는 인덱스 분할
   - axis로 분할 방향 지정
   
4. 정렬:
   - sort: 값 정렬
   - argsort: 인덱스 정렬 (간접 정렬)
   
5. 기타:
   - unique: 고유값 추출
   - 다양한 옵션으로 추가 정보 획득
'''
# ============================================================================
