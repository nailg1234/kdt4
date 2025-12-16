import numpy as np
print('9. 배열의 형태 변경')
print(
'''
    배열의 형태 변경 - numpy_array.reshape(new_shape), np.reshape(numpy_array, new_shape)

    중요
    - 전체 요소 개수는 변하지 않음
    - 원본 배열은 변경되지 않음
    - -1을 사용하면 자동으로 크기 계산
'''
)



print(
'''
    1) 기본 reshape
'''
)
print('1) 기본 reshape')
arr = np.arange(12)
print("# 1차원 -> 2차원 변환")
print('1차원 : ', arr)
print('2차원 : \n', arr.reshape(3, 4))
'''
    # 1차원 -> 2차원 변환
    1차원 :  [ 0  1  2  3  4  5  6  7  8  9 10 11]
    2차원 :
    [[ 0  1  2  3]
    [ 4  5  6  7]
    [ 8  9 10 11]]
'''
print()



print(
'''
    2) 다양한 형태로 변환
'''
)
print('2) 다양한 형태로 변환')
arr = np.arange(24)
print('1차원 : ', arr)
print('2x12 : \n', np.reshape(arr, (2, 12)))
print('4x6 : \n', np.reshape(arr, (4, 6)))
print('6x4 : \n', arr.reshape(6, 4))
'''
    2) 다양한 형태로 변환
    1차원 :  [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
    2x12 :
    [[ 0  1  2  3  4  5  6  7  8  9 10 11]
    [12 13 14 15 16 17 18 19 20 21 22 23]]
    4x6 :
    [[ 0  1  2  3  4  5]
    [ 6  7  8  9 10 11]
    [12 13 14 15 16 17]
    [18 19 20 21 22 23]]
    6x4 :
    [[ 0  1  2  3]
    [ 4  5  6  7]
    [ 8  9 10 11]
    [12 13 14 15]
    [16 17 18 19]
    [20 21 22 23]]
'''
print()



print(
'''
    3) 3차원으로 변환
'''
)
print('3) 3차원으로 변환')
arr = np.arange(24)
print('1차원 : ', arr)
print('3차원 : \n', arr.reshape(2, 3, 4))
'''
    3) 3차원으로 변환
    1차원 :  [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
    3차원 :
    [[[ 0  1  2  3]
    [ 4  5  6  7]
    [ 8  9 10 11]]

    [[12 13 14 15]
    [16 17 18 19]
    [20 21 22 23]]]
'''
print()



print(
'''
    4) -1 사용 : 자동 크기 계산
    -1의 의미
    - 나머지를 자동으로 계산
    - 한 차원에 사용 가능
    - 전체 요소 개수를 기준으로 계산

    사용 예)
    - 12개 요소를 (3, -1)로 reshape -> 12/3 = 4 이므로 (3, 4)가 됨
'''
)
print('4) -1 사용 : 자동 크기 계산')
arr = np.arange(12)
print('(3, -1) \n', arr.reshape(3, -1))
print(f'(3, -1) -> {arr.reshape(3, -1).shape}')
print()
print('(-1, 4) \n', arr.reshape(-1, 4))
print(f'(-1, 4) -> {arr.reshape(-1, 4).shape}')
print()
print('(2, 2, -1)\n', arr.reshape(2, 2, -1))
print(f'(2, 2, -1) -> {arr.reshape(2, 2, -1).shape}')
'''
    4) -1 사용 : 자동 크기 계산
    (3, -1)
    [[ 0  1  2  3]
    [ 4  5  6  7]
    [ 8  9 10 11]]
    (3, -1) -> (3, 4)

    (-1, 4)
    [[ 0  1  2  3]
    [ 4  5  6  7]
    [ 8  9 10 11]]
    (-1, 4) -> (3, 4)

    (2, 2, -1)
    [[[ 0  1  2]
    [ 3  4  5]]

    [[ 6  7  8]
    [ 9 10 11]]]
    (2, 2, -1) -> (2, 2, 3)
'''
print()



print(
'''
    5) 1차원으로 펼치기
'''
)
print('5) 1차원으로 펼치기')
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print('방법 1) matrix.reshape(-1) : \n',matrix.reshape(-1))

# 방법 2) 복사본 생성
print('방법 2) matrix.flatten() : \n',matrix.flatten())

# 방법 3) view 반환(변경시 원본도 변경)
print('방법 3) matrix.ravel() : \n',matrix.ravel())
'''
    5) 1차원으로 펼치기
    방법 1) matrix.reshape(-1) :
    [1 2 3 4 5 6]
    방법 2) matrix.flatten() :
    [1 2 3 4 5 6]
    방법 3) matrix.ravel() :
    [1 2 3 4 5 6]
'''
print()



print(
'''
    6) 열 벡터, 행 벡터 변환
    reshape를 이용한 벡터 형태 변환
    - 행 벡터 : (1, n)
    - 열 벡터 : (n, 1)
'''
)
arr = np.array([1, 2, 3, 4, 5])
print('원본 배열:', arr, '| shape:', arr.shape)
row_vector = np.reshape(arr, (1, -1))
print('\n행 벡터:\n', row_vector, '| shape:', row_vector.shape)
col_vector = np.reshape(arr, (-1, 1))
print('\n열 벡터:\n', col_vector, '| shape:', col_vector.shape)
'''
    6) 열 벡터, 행 벡터 변환
    원본 배열: [1 2 3 4 5] | shape: (5,)

    행 벡터:
    [[1 2 3 4 5]] | shape: (1, 5)

    열 벡터:
    [[1]
    [2]
    [3]
    [4]
    [5]] | shape: (5, 1)
'''
print()



print(
'''
    7) reshape 오류 예시
    - 요소 개수가 맞지 않으면 오류 발생
'''
)
print('7) reshape 오류 예시')
arr = np.arange(12)
print('배열 크기 : ', arr.size)
try:
    wrong_reshape = arr.reshape(3, 5)  # 3 * 5 = 15 (불가능)
except ValueError as e:
    print('오류 발생:', e)
'''
    7) reshape 오류 예시
    배열 크기 :  12
    오류 발생: cannot reshape array of size 12 into shape (3,5)
'''
print()



print(
'''
    8) 실전 예제 : 이미지 데이터 변환
    이미지 처리에서 reshape는 필수
    - (높이, 너비, 채널) <-> (배치, 높이, 너비, 채널)
    - 2D <-> 1D (머신러닝 입력)
'''
)
print('8) 실전 예제 : 이미지 데이터 변환')
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
'''
8) 실전 예제 : 이미지 데이터 변환
원본 이미지 shape: (28, 28, 3)
펼친 이미지 shape: (2352,)
복원된 이미지 shape: (28, 28, 3)
복원 성공? True
'''
print()



print(
'''
    9) 배치 처리를 위한 reshape
    딥러닝에서 자주 사용하는 패턴
'''
)
print('9) 배치 처리를 위한 reshape')
print('딥러닝에서 자주 사용하는 패턴')
images = np.random.rand(100, 28, 28)
print('이미지 데이터 shape:', images.shape)

# 각 이미지를 1D로 펼치기 (100, 784)
images_flat = images.reshape(100, -1)
print('펼친 데이터 shape:', images_flat.shape)

# 다시 원래 형태로
images_restored = images_flat.reshape(100, 28, 28)
print('복원된 데이터 shape:', images_restored.shape)
'''
9) 배치 처리를 위한 reshape
딥러닝에서 자주 사용하는 패턴
이미지 데이터 shape: (100, 28, 28)
펼친 데이터 shape: (100, 784)
복원된 데이터 shape: (100, 28, 28)
'''
print()



print(
'''
    10) newaxis를 사용한 차원 추가
    newaxis
    - reshape의 대안
    - 새로운 차원을 추가할 때 더 직관적
    - None과 동일
'''
)
print('10) newaxis를 사용한 차원 추가')
arr = np.array([1, 2, 3, 4, 5])
row = arr[np.newaxis, :]
print(row, '/', row.shape)
col = arr[:, np.newaxis]
print(col, '/', col.shape)
'''
    10) newaxis를 사용한 차원 추가
    [[1 2 3 4 5]] / (1, 5)
    [[1]
    [2]
    [3]
    [4]
    [5]] / (5, 1)
'''



print(
'''
    reshape 핵심:
    1) 배열의 형태를 변경(전체 요소 개수는 동일)
    2) 원본은 변경하지 않음(새 view 반환)
    3) -1 사용으로 자동 크기 계산 가능
    4) 이미지/텐서 데이터 변환에 필수
    5) flatten(), ravel()로 1D 변환 가능

    주의사항
    - reshape는 요소 개수가 반드시 맞아야 함!
'''
)