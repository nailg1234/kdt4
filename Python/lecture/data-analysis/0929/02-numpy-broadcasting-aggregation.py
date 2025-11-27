import numpy as np

# ============================================================================
# np.random.normal() - 랜덤 숫자 만들기 (평균 중심)
# ============================================================================
"""
np.random.normal(평균, 범위, 개수)

쉽게 설명:
- 평균 주변에서 랜덤 숫자를 만들어줌
- 평균에서 멀어질수록 나올 확률이 낮아짐
- 예: 평균 키 170cm 주변에서 랜덤 키 만들기
"""

print('=== 1. 기본 사용법 ===')
# 평균 0 주변의 랜덤 숫자 10개
numbers = np.random.normal(size=10)
print('랜덤 숫자 10개:', numbers)
print()

print('=== 2. 평균 지정하기 ===')
# 평균 100 주변의 랜덤 숫자 10개 (예: 시험 점수)
scores = np.random.normal(loc=100, scale=15, size=10)
print('시험 점수 10개:', scores)
print('평균:', round(scores.mean(), 1))
print()

print('=== 3. 2차원 배열로 만들기 ===')
# 3행 4열의 랜덤 숫자
matrix = np.random.normal(loc=50, scale=10, size=(3, 4))
print('3x4 랜덤 배열:\n', matrix)
print()

print('=== 4. 실전 예제: 키 데이터 만들기 ===')
# 평균 키 170cm 주변에서 랜덤 키 100개 만들기
heights = np.random.normal(loc=170, scale=7, size=100)
print('키 10명:', [round(h, 1) for h in heights[:10]])
print('평균 키:', round(heights.mean(), 1), 'cm')
print('가장 큰 키:', round(heights.max(), 1), 'cm')
print('가장 작은 키:', round(heights.min(), 1), 'cm')
print()


# ============================================================================
# reshape() - 배열의 형태 변경
# ============================================================================
"""
array.reshape(new_shape)
또는
np.reshape(array, new_shape)

중요:
- 전체 요소 개수는 변하지 않음
- 원본 배열은 변경되지 않음 (새 view 반환)
- -1을 사용하면 자동으로 크기 계산
"""

print('=== 1. 기본 reshape ===')
# 1차원 → 2차원
arr = np.arange(12)  # [0, 1, 2, ..., 11]
print('원본 배열:', arr)
print('원본 shape:', arr.shape)  # (12,)

reshaped = arr.reshape(3, 4)  # 3행 4열
print('\n3x4로 변환:\n', reshaped)
print('변환 후 shape:', reshaped.shape)  # (3, 4)
print()

print('=== 2. 다양한 형태로 변환 ===')
arr = np.arange(24)

# 2차원 변환
matrix_2x12 = arr.reshape(2, 12)
print('2x12 행렬:\n', matrix_2x12)

matrix_4x6 = arr.reshape(4, 6)
print('\n4x6 행렬:\n', matrix_4x6)

matrix_6x4 = arr.reshape(6, 4)
print('\n6x4 행렬:\n', matrix_6x4)
print()

print('=== 3. 3차원으로 변환 ===')
# 24개 요소 → (2, 3, 4)
tensor = arr.reshape(2, 3, 4)
print('3차원 텐서 shape:', tensor.shape)
print('3차원 텐서:\n', tensor)
print()

print('=== 4. -1 사용: 자동 크기 계산 ===')
"""
-1의 의미:
- "나머지를 자동으로 계산해줘"
- 한 차원에만 사용 가능
- 전체 요소 개수를 기준으로 자동 계산

예: 12개 요소를 (3, -1)로 reshape
→ 12 / 3 = 4이므로 (3, 4)가 됨
"""
arr = np.arange(12)

auto_reshape1 = arr.reshape(3, -1)  # (3, 4)로 자동 계산
print('(3, -1) → shape:', auto_reshape1.shape)
print(auto_reshape1)

auto_reshape2 = arr.reshape(-1, 4)  # (3, 4)로 자동 계산
print('\n(-1, 4) → shape:', auto_reshape2.shape)
print(auto_reshape2)

auto_reshape3 = arr.reshape(2, 2, -1)  # (2, 2, 3)으로 자동 계산
print('\n(2, 2, -1) → shape:', auto_reshape3.shape)
print(auto_reshape3)
print()

print('=== 5. 1차원으로 펼치기 ===')
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print('원본 2차원 배열:\n', matrix)

# 방법 1: reshape(-1)
flattened1 = matrix.reshape(-1)
print('\nreshape(-1):', flattened1)

# 방법 2: flatten() - 복사본 생성
flattened2 = matrix.flatten()
print('flatten():', flattened2)

# 방법 3: ravel() - view 반환 (더 빠름)
flattened3 = matrix.ravel()
print('ravel():', flattened3)
print()

print('=== 6. 열 벡터, 행 벡터 변환 ===')
"""
reshape를 사용한 벡터 형태 변환:
- 행 벡터: (1, n)
- 열 벡터: (n, 1)
"""
arr = np.array([1, 2, 3, 4, 5])
print('원본 배열:', arr, '| shape:', arr.shape)

# 행 벡터 (1행 n열)
row_vector = arr.reshape(1, -1)
print('\n행 벡터:\n', row_vector, '| shape:', row_vector.shape)

# 열 벡터 (n행 1열)
col_vector = arr.reshape(-1, 1)
print('\n열 벡터:\n', col_vector, '| shape:', col_vector.shape)
print()

print('=== 7. reshape 오류 예시 ===')
"""
요소 개수가 맞지 않으면 오류 발생
"""
arr = np.arange(12)  # 12개 요소
print('배열 크기:', arr.size)

try:
    wrong_reshape = arr.reshape(3, 5)  # 3 * 5 = 15 (불가능)
except ValueError as e:
    print('오류 발생:', e)
print()

print('=== 8. 실전 예제: 이미지 데이터 변환 ===')
"""
이미지 처리에서 reshape는 필수:
- (높이, 너비, 채널) ↔ (배치, 높이, 너비, 채널)
- 2D ↔ 1D (머신러닝 입력)
"""
# 가상의 RGB 이미지 데이터 (28x28x3)
image = np.random.randint(0, 256, size=(28, 28, 3))
print('원본 이미지 shape:', image.shape)  # (28, 28, 3)

# 1D 벡터로 펼치기 (머신러닝 입력용)
image_flat = image.reshape(-1)
print('펼친 이미지 shape:', image_flat.shape)  # (2352,)

# 다시 원래 형태로 복원
image_restored = image_flat.reshape(28, 28, 3)
print('복원된 이미지 shape:', image_restored.shape)  # (28, 28, 3)
print('복원 성공?', np.array_equal(image, image_restored))  # True
print()

print('=== 9. 배치 처리를 위한 reshape ===')
"""
딥러닝에서 자주 사용하는 패턴
"""
# 100개의 28x28 흑백 이미지
images = np.random.rand(100, 28, 28)
print('이미지 데이터 shape:', images.shape)

# 각 이미지를 1D로 펼치기 (100, 784)
images_flat = images.reshape(100, -1)
print('펼친 데이터 shape:', images_flat.shape)

# 다시 원래 형태로
images_restored = images_flat.reshape(100, 28, 28)
print('복원된 데이터 shape:', images_restored.shape)
print()

print('=== 10. newaxis를 사용한 차원 추가 ===')
"""
reshape의 대안: np.newaxis
- 새로운 차원을 추가할 때 더 직관적
- None과 동일
"""
arr = np.array([1, 2, 3, 4, 5])
print('원본:', arr.shape)

# 행 벡터 (1, 5)
row = arr[np.newaxis, :]
print('행 벡터:', row.shape)

# 열 벡터 (5, 1)
col = arr[:, np.newaxis]
print('열 벡터:', col.shape)
print()


# ============================================================================
# 핵심 정리
# ============================================================================
"""
np.random.normal() 핵심:
1. 정규 분포(가우시안 분포) 난수 생성
2. loc(평균), scale(표준편차), size(배열 크기) 지정
3. 실제 데이터 시뮬레이션에 유용
4. randn()보다 유연하지만 조금 느림

reshape() 핵심:
1. 배열의 형태를 변경 (전체 요소 개수는 동일)
2. 원본은 변경하지 않음 (새 view 반환)
3. -1 사용으로 자동 크기 계산 가능
4. 이미지/텐서 데이터 변환에 필수
5. flatten(), ravel()로 1D 변환 가능

주의사항:
- reshape는 요소 개수가 맞아야 함
- normal()은 충분히 큰 샘플에서 평균/표준편차가 정확함
"""

print('=' * 70)
print('normal()과 reshape() 학습 완료!')
print('=' * 70)
