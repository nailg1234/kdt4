# 차원 추가와 제거
# newaxis 와 expand_dims
# 새로운 차원을 추가하여 브로드 캐스팅이나 연산을 가능하게 합니다.

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print('원본 : \n', arr)  # [1 2 3 4 5]
print('모양 : ', arr.shape)  # (5,)

# newaxis
row_vec = arr[np.newaxis, :]
print('행 벡터 \n', row_vec)
print('행 벡터 shape', row_vec.shape)

col_vec = arr[:, np.newaxis]
print('열 벡터 \n', col_vec)
print('열 벡터 shape', col_vec.shape)

arr = np.array([1, 2, 3, 4, 5])
# 첫 번째 축에 추가
arr_expanded0 = np.expand_dims(arr, axis=0)

# 두 번째 축에 추가
arr_expanded1 = np.expand_dims(arr, axis=1)

print('axis = 0 \n', arr_expanded0)
print('axis = 1 \n', arr_expanded1)

# squeeze
arr = np.array([[[1, 2, 3]]])

print('원본 \n', arr)
print('모양 \n', arr.shape)
print()
squeezed = np.squeeze(arr)
print('squeezed \n', squeezed)
print('squeezed 모양 \n', squeezed.shape)
print()
squeezed0 = np.squeeze(arr, axis=1)
print('squeezed0 \n', squeezed0)
print('squeezed0 모양 \n', squeezed0.shape)


# 배열 평탄화 Flattening

# flatten : 항상 복사본 반환 ('안전하지만 메모리 사용')
# ravel : 가능하면 뷰 반환(빠르지만 주의 필요)

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print('2차원 배열')
print(arr)

flattened = arr.flatten()
print('flattened 결과 : ', flattened)

flattened[0] = 999
print('2차원 배열')
print(arr)
print()

raveled = arr.ravel()
print('raveled 결과 : ', raveled)
raveled[0] = 999
print()
print('2차원 배열')
print(arr)
print('raevled 결과 : ', raveled)
print()

raveled_copy = arr.ravel().copy()
raveled_copy[1] = 999

print('2차원 배열')
print(arr)
print('raveled_copy 결과\n', raveled_copy)

# unique 유니큐

arr = np.array([1, 2, 3, 5, 3, 4, 5, 6, 8, 9, 7, 6, 5, 4, 3, 8, 9, 0, 8, 7, 6])
uniq, idx, inv, cnt = np.unique(arr,
                                return_index=True,
                                return_inverse=True,
                                return_counts=True)

print('고유 값 : ', uniq)
print('첫 등장 인덱스 : ', idx)
print('원본 -> 고유 값 인덱스 : ', inv)
print('등장 횟수', cnt)
print()

# 배열 결합 (Concatenation)
# 배열 이어 붙이기
# 같은 차원의 배열들을 특정 축을 따라 연결
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([7, 8, 9])

concat_1d = np.concatenate([a, b, c])
print('결합 결과', concat_1d)


A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# ============ axis = 0 ============

concat_v = np.concatenate([A, B], axis=0)
print('axis = 0 (수직결합):')
print(concat_v)
print(concat_v.shape)

# ============ axis = 1 ============

concat_h = np.concatenate([A, B], axis=1)
print('axis = 1 (수평결합):')
print(concat_h)
print(concat_h.shape)

# vstack, hstack
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

vstacked = np.vstack([a, b])
print('v stack (수직)')
print(vstacked)


hstacked = np.hstack([a, b])
print('h stack (수평)')
print(hstacked)

# 배열 분할
# split

# 하나의 배열을 여러 개의 작은 배열로 나누는 작업
# 데이터를 배치로 나누거나 훈련/검증 세트로 분리할때 사용합니다.

arr = np.arange(12)
print(arr)
print()

splits_equal = np.split(arr, 3)  # 3개로 균등 분할
print('splits_equal', splits_equal)

for i, sub in enumerate(splits_equal):
    print(i+1, sub)

splits_idx = np.split(arr, [3, 7])  # 해당 인덱스 3, 7에서 분할


arr = np.arange(24).reshape(4, 6)
print(arr)
'''
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]]
'''
row_splits = np.split(arr, 2, axis=0)

for i, sub in enumerate(row_splits):
    print(i+1, sub)
print()


col_splits = np.split(arr, 2, axis=1)

for i, sub in enumerate(col_splits):
    print(i+1, sub)
print()


arr = np.array([3, 2, 1, 2, 4, 5, 6, 7])
sorted_copy = np.sort(arr)

print(arr)
print(sorted_copy)
print(arr)

arr.sort()
print(arr)

arr2 = np.array([
    [2, 1, 5],
    [3, 2, 1]
])

sorted_axis0 = np.sort(arr2, axis=0)  # 열 방향
print(sorted_axis0)
print()

sorted_axis1 = np.sort(arr2, axis=1)  # 행 방향
print(sorted_axis1)
print()

sorted_None = np.sort(arr2, axis=None)  # 평탄화 후 정렬
print(sorted_None)
print()

# argsort
#
names = np.array(['김철수', '이영희', '박민수', '정수진', '최동욱'])
scores = np.array([85, 92, 78, 95, 88])

for name, score in zip(names, scores):
    print(f'{name} {score}')
# 점수 순으로 정렬
sorted_idx = np.argsort(scores)[::-1]  # 높은 순

for i, idx in enumerate(sorted_idx, 1):
    print(f'{i}위 {names[idx]} {scores[idx]}점')
