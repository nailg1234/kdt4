# ============================================================================
# NumPy (Numerical Python) 완벽 가이드
# ============================================================================

# python -m venv 폴더이름
# python -m venv venv

# ============================================================================
# 1. NumPy란 무엇인가?
# ============================================================================
"""
NumPy는 파이썬에서 과학계산을 위한 핵심 라이브러리입니다.
데이터과학, 머신러닝, 과학 연구 분야에서 가장 중요한 도구 중 하나입니다.

주요 특징:
1. 다차원 배열 객체 (ndarray)
2. 빠른 연산 속도
3. 메모리 효율성
4. 벡터화 연산 지원
5. 선형대수, 푸리에 변환, 난수 생성 등 다양한 수학 함수 제공
"""

# ============================================================================
# 2. 왜 NumPy를 사용해야 하는가?
# ============================================================================
"""
문제점: 파이썬은 인터프리터 언어로 실행속도가 느립니다.

해결책 1 - 속도 개선:
- NumPy는 C언어로 구현되어 있어 대용량 데이터 연산을 매우 빠르게 처리
- 일반 파이썬 리스트보다 10~100배 이상 빠름

해결책 2 - 메모리 효율성:
- 파이썬 리스트: 각 요소가 객체로 저장되어 메모리 오버헤드가 큼
  예) [1, 2, 3] → 각 숫자가 별도의 파이썬 객체로 저장
- NumPy 배열: 연속된 메모리 공간에 같은 타입의 데이터를 저장
  예) array([1, 2, 3]) → 연속된 메모리에 정수만 저장

해결책 3 - 벡터화 연산:
- 반복문 없이 전체 배열에 대한 연산을 한번에 수행
- 코드가 간결하고 가독성이 좋음
"""


import numpy as np
print('Numpy 버전:', np.__version__)
print('Numpy 설치 경로:', np.__file__)
print()

# ============================================================================
# 3. ndarray - NumPy의 핵심 자료구조
# ============================================================================
"""
ndarray (N-dimensional array):
- NumPy의 핵심 자료구조
- 같은 타입의 요소들을 담는 다차원 컨테이너
- 고정된 크기의 동질적인(homogeneous) 배열

핵심 속성:
- dtype: 배열 요소의 데이터 타입
- shape: 배열의 형태 (각 차원의 크기)
- ndim: 배열의 차원 수
- size: 배열의 전체 요소 개수
- itemsize: 각 요소의 바이트 크기
"""

arr = np.array([1, 2, 3, 4, 5])

print('=== ndarray 기본 속성 ===')
print('1. 객체 타입:', type(arr))  # <class 'numpy.ndarray'>
print('2. 데이터 타입:', arr.dtype)  # int64 (64비트 정수)
print('3. 배열 모양:', arr.shape)  # (5,) - 1차원 배열, 5개 요소
print('4. 차원 수:', arr.ndim)  # 1 - 1차원
print('5. 전체 요소 수:', arr.size)  # 5개
print()

# ============================================================================
# 4. 파이썬 리스트 vs NumPy 배열
# ============================================================================
"""
중요한 차이점을 이해하는 것이 NumPy 학습의 첫걸음입니다.
"""

print('=== 차이점 1: 타입 고정성 ===')
"""
파이썬 리스트:
- 서로 다른 타입의 요소를 담을 수 있음 (이질적)
- 각 요소가 독립적인 파이썬 객체
- 유연하지만 메모리와 속도 측면에서 비효율적

NumPy 배열:
- 모든 요소가 같은 타입이어야 함 (동질적)
- 다른 타입이 섞이면 자동으로 상위 타입으로 변환
- 변환 우선순위: bool < int < float < complex < string
"""
python_list = [1, 2.5, '3', True]  # 다양한 타입 가능
numpy_array = np.array([1, 2, 3, True])  # True는 1로 변환됨
print('파이썬 리스트:', python_list)
print('Numpy 배열:', numpy_array)  # [1 2 3 1] - 모두 정수로 통일
print()

print('=== 차이점 2: 연산 방식 ===')
"""
파이썬 리스트 + 연산:
- 리스트 연결(concatenation)
- [1,2,3] + [4,5,6] = [1,2,3,4,5,6]

NumPy 배열 + 연산:
- 요소별(element-wise) 연산
- [1,2,3] + [4,5,6] = [5,7,9]
- 벡터화 연산으로 매우 빠름
"""
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print('리스트 더하기:', list1 + list2)  # [1, 2, 3, 4, 5, 6] - 연결

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print('Numpy 배열 더하기:', arr1 + arr2)  # [5 7 9] - 요소별 덧셈
print()

# ============================================================================
# 5. 다양한 데이터 타입의 배열 생성
# ============================================================================
"""
NumPy는 다양한 데이터 타입을 지원합니다:
- 정수형: int8, int16, int32, int64
- 부동소수점: float16, float32, float64
- 복소수: complex64, complex128
- 불린: bool
- 문자열: string_, unicode_
"""

print('=== 정수 배열 ===')
int_array = np.array([1, 2, 3, 4, 5])
print('정수 배열:', int_array)
print('데이터 타입:', int_array.dtype)  # int64 (시스템에 따라 다를 수 있음)
print()

print('=== 실수 배열 ===')
"""
실수가 하나라도 포함되면 전체가 실수형으로 변환됩니다.
"""
float_array = np.array([1.1, 2.2, 3.3, 4.4, 5])
print('실수 배열:', float_array)
print('데이터 타입:', float_array.dtype)  # float64
print()

print('=== 명시적 타입 지정 ===')
"""
dtype 매개변수로 원하는 데이터 타입을 명시적으로 지정할 수 있습니다.
장점:
- 메모리 절약 (float32는 float64의 절반 메모리 사용)
- 호환성 (특정 라이브러리나 하드웨어 요구사항 충족)
"""
specified_array = np.array(['1', '2', 3, 4, 5], dtype=np.float32)
print('명시적 배열:', specified_array)
print('데이터 타입:', specified_array.dtype)  # float32
print()

print('=== 문자열 배열 ===')
"""
<U10 의미:
- <: little-endian (바이트 순서)
- U: 유니코드 문자열
- 10: 최대 문자 길이
"""
string_array = np.array(['apple', 'banana', 'cherry'])
print('문자열 배열:', string_array)
print('데이터 타입:', string_array.dtype)  # <U6 (가장 긴 문자열 기준)
print()

# ============================================================================
# 6. 다차원 배열
# ============================================================================
"""
NumPy의 진정한 힘은 다차원 배열 처리에서 나타납니다.

1차원 배열: 벡터 (vector)
2차원 배열: 행렬 (matrix)
3차원 배열: 텐서 (tensor)
4차원 이상: 고차원 텐서
"""

print('=== 2차원 배열 (행렬) ===')
"""
행렬 표현:
[1, 2, 3]
[2, 3, 4]
[4, 5, 6]

shape (3, 3) 의미:
- 첫 번째 3: 행(row)의 개수
- 두 번째 3: 열(column)의 개수
"""
matrix = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [4, 5, 6]
])

print('2차원 배열:\n', matrix)
print('모양:', matrix.shape)  # (3, 3) - 3행 3열
print('차원:', matrix.ndim)  # 2 - 2차원
print('크기:', matrix.size)  # 9 - 총 9개 요소
print()

print('=== 반복문으로 배열 생성 ===')
"""
프로그래밍 방식으로 배열을 생성할 수 있습니다.
실무에서 데이터를 동적으로 생성할 때 유용합니다.
"""
rows = []
for i in range(3):
    row = [i * 3 + j for j in range(4)]  # [0, 1, 2, 3], [3, 4, 5, 6], ...
    rows.append(row)

matrix2 = np.array(rows)
print('동적 생성 행렬:\n', matrix2)
print()

print('=== 3차원 배열 (텐서) ===')
"""
3차원 배열의 이해:
- 여러 개의 2차원 행렬을 쌓은 형태
- 이미지 처리: (높이, 너비, 색상채널)
- 동영상 처리: (프레임, 높이, 너비)
- 딥러닝: (배치크기, 높이, 너비)

shape (2, 3, 4) 의미:
- 2: 2개의 행렬
- 3: 각 행렬은 3행
- 4: 각 행렬은 4열
"""
tensor = np.array([
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ],
    [
        [13, 14, 15, 16],
        [17, 18, 19, 20],
        [21, 22, 23, 24],
    ],
])

print('3차원 배열 모양:', tensor.shape)  # (2, 3, 4)
print('차원:', tensor.ndim)  # 3
print('크기:', tensor.size)  # 24개 요소
print()

# ============================================================================
# 7. NumPy 내장 함수로 배열 생성
# ============================================================================

print('=== arange: 연속된 숫자 배열 ===')
"""
np.arange(start, stop, step)
- 파이썬 range()와 유사하지만 NumPy 배열 반환
- stop 값은 포함되지 않음 (미만)
- step에 실수도 사용 가능
"""
arr1 = np.arange(10)  # 0부터 9까지
print('0부터 9까지:', arr1)

arr2 = np.arange(1, 11)  # 1부터 10까지
print('1부터 10까지:', arr2)

arr3 = np.arange(1, 21, 2)  # 1, 3, 5, ..., 19
print('1부터 20까지 홀수만:', arr3)

arr4 = np.arange(1, 11, 0.5)  # 0.5 간격
print('1부터 11까지 0.5 간격:', arr4)
print()

print('=== linspace: 균등 간격 배열 ===')
"""
np.linspace(start, stop, num, endpoint=True)
- 시작과 끝 사이를 균등하게 나눈 숫자들
- num: 생성할 요소의 개수
- endpoint=True: 끝값 포함 (기본값)
- endpoint=False: 끝값 미포함

계산 공식:
- endpoint=True: step = (stop - start) / (num - 1)
- endpoint=False: step = (stop - start) / num

사용 예시:
- 그래프 그리기 (x축 좌표 생성)
- 수치해석 (등간격 샘플링)
- 신호처리 (시간 축 생성)
"""
arr1 = np.linspace(0, 10, 5)  # 0, 2.5, 5, 7.5, 10
print('0부터 10까지 5개 요소:', arr1)

arr2 = np.linspace(0, 10, 5, endpoint=False)  # 0, 2, 4, 6, 8
print('끝값 제외:', arr2)
print()

print('=== zeros: 0으로 채운 배열 ===')
"""
용도:
- 배열 초기화
- 누적 계산용 배열 준비
- 이미지 처리 (검은색 이미지 생성)
"""
zeros_1d = np.zeros(5)
print('1차원 zeros:', zeros_1d)

zeros_2d = np.zeros((3, 4))
print('2차원 zeros:\n', zeros_2d)

zeros_2d_int = np.zeros((3, 4), dtype=int)
print('2차원 zeros (정수):\n', zeros_2d_int)

matrix = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [4, 5, 6]
])
# 기존 배열과 같은 모양의 영 배열
zeros_copy = np.zeros_like(matrix)
print('zeros_like:\n', zeros_copy)
print()

print('=== ones: 1로 채운 배열 ===')
"""
용도:
- 가중치 초기화
- 마스크 배열 생성
- 곱셈 항등원
"""
ones_1d = np.ones(5)
print('1차원 ones:', ones_1d)

ones_2d = np.ones((3, 4))
print('2차원 ones:\n', ones_2d)

ones_2d_bool = np.ones((3, 4), dtype=bool)
print('2차원 ones (불린):\n', ones_2d_bool)
print()

print('=== full: 특정 값으로 채운 배열 ===')
"""
용도:
- 초기값이 있는 배열 생성
- 기본값 설정
"""
full_array = np.full((3, 4), 7)
print('7로 채운 배열:\n', full_array)

matrix = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [4, 5, 6]
])
full_like = np.full_like(matrix, 999)
print('999로 채운 배열:\n', full_like)
print()

print('=== empty: 빈 배열 (주의!) ===')
"""
주의사항:
- 메모리만 할당하고 초기화하지 않음
- 쓰레기 값(garbage value)이 들어있음
- 빠르지만 위험할 수 있음
- 반드시 나중에 값을 채워야 함

사용 시기:
- 즉시 값을 채울 예정일 때
- 속도가 매우 중요할 때
"""
empty_array = np.empty((2, 3))
print('빈 배열 (쓰레기값):\n', empty_array)
print()

print('=== eye: 단위 행렬 (항등 행렬) ===')
"""
단위 행렬 (Identity Matrix):
- 대각선은 1, 나머지는 0
- 행렬 곱셈의 항등원 (A × I = A)

용도:
- 선형대수 연산
- 머신러닝 초기화
- 공분산 행렬 생성
"""
identity = np.eye(3)
print('3x3 항등 행렬:\n', identity)

matrix = np.eye(4, 5)  # 4행 5열
print('4x5 대각 행렬:\n', matrix)

matrix = np.eye(4, k=1)  # 대각선을 위로 1칸 이동
print('위쪽 대각선:\n', matrix)

matrix = np.eye(4, k=-1)  # 대각선을 아래로 1칸 이동
print('아래쪽 대각선:\n', matrix)
print()

print('=== identity: 정방 항등 행렬 ===')
"""
eye와의 차이:
- identity는 정사각형만 생성 가능
- eye는 직사각형도 가능하고 대각선 위치 조정 가능
"""
identity = np.identity(4)
print('4x4 항등 행렬:\n', identity)
print()

# ============================================================================
# 8. 난수 생성
# ============================================================================

print('=== 균일 분포 난수 ===')
"""
균일 분포 (Uniform Distribution):
- 특정 구간 안에서 모든 값이 똑같은 확률로 나옴
- 치우침 없이 고르게 퍼져 있는 확률 분포

사용 예:
- 게임 개발 (랜덤 아이템 드롭)
- 시뮬레이션 (몬테카를로 방법)
- 초기화 (가중치 랜덤 초기화)
"""
random_uniform = np.random.rand(3, 3)  # 0~1 사이 균일 분포
print('0~1 균일 분포:\n', random_uniform)

rounded = np.round(random_uniform, 2)  # 소수점 2자리
print('0~1 균일 분포 (반올림):\n', rounded)

# 특정 범위로 스케일링
low, high = 10, 20
random_range = low + (high - low) * np.random.rand(3, 3)
print(f'{low}~{high} 균일 분포:\n', random_range)

# 더 직관적인 방법
uniform = np.random.uniform(low=0, high=100, size=(2, 3))
print('0~100 균일 분포:\n', uniform)
print()

print('=== 정규 분포 난수 ===')
"""
정규 분포 (Normal Distribution / Gaussian Distribution):
- 평균을 중심으로 좌우 대칭인 종 모양 분포
- 자연계의 많은 현상이 정규 분포를 따름
- 표준 정규 분포: 평균 0, 표준편차 1

68-95-99.7 규칙:
- 평균 ± 1σ: 68% 데이터
- 평균 ± 2σ: 95% 데이터
- 평균 ± 3σ: 99.7% 데이터

사용 예:
- 실제 데이터 시뮬레이션 (키, 몸무게, 시험 점수)
- 머신러닝 가중치 초기화
- 노이즈 추가
"""
random_normal1 = np.random.randn(3, 3)
print('표준 정규 분포:\n', random_normal1)

# 평균 100, 표준편차 15인 정규 분포 (예: 시험 점수)
mean, std = 100, 15
scores = mean + std * np.random.randn(1000)
print('시험 점수 시뮬레이션 (일부):', scores[:10])
print('실제 평균:', round(scores.mean(), 2))
print('실제 표준편차:', round(scores.std(), 2))
print()

print('=== 정수 난수 ===')
"""
randint(low, high, size)
- low 이상 high 미만의 정수
- 이산 균일 분포

사용 예:
- 게임 (주사위, 카드)
- 랜덤 샘플링
- 랜덤 인덱스 생성
"""
random_int = np.random.randint(0, 10, size=(3, 4))
print('0~9 정수 난수:\n', random_int)

# 주사위 시뮬레이션
dice = np.random.randint(1, 7, size=10)
print('주사위 10번 굴리기:', dice)
print()

print('=== 재현 가능한 난수 (시드 설정) ===')
"""
시드 (Seed):
- 난수 생성의 시작점
- 같은 시드 = 같은 난수 시퀀스
- 디버깅과 재현성을 위해 중요

사용 시기:
- 실험 재현
- 디버깅
- 테스트 코드 작성
"""
np.random.seed(42)  # 시드 고정
random1 = np.random.rand(5)
print('첫 번째 난수:', random1)

np.random.seed(42)  # 같은 시드 사용
random2 = np.random.rand(5)
print('두 번째 난수:', random2)
print('같은 난수인가?', np.array_equal(random1, random2))  # True
print()

print('=== 새로운 난수 생성 방식 (권장) ===')
"""
default_rng (Random Generator):
- NumPy 1.17 이상에서 권장하는 방식
- 더 나은 성능과 통계적 품질
- 여러 generator를 독립적으로 사용 가능

장점:
- 스레드 안전성
- 더 빠른 속도
- 더 좋은 난수 품질
"""
rng = np.random.default_rng(seed=42)
random3 = rng.random((2, 3))  # 0~1 균일 분포
print('새로운 방식 난수:\n', random3)

# 독립적인 generator 생성
rng1 = np.random.default_rng(seed=42)
rng2 = np.random.default_rng(seed=42)
print('독립적 generator 1:', rng1.random(3))
print('독립적 generator 2:', rng2.random(3))
print()

# ============================================================================
# 9. 핵심 정리
# ============================================================================
"""
NumPy 핵심 개념 요약:

1. ndarray는 동질적(같은 타입), 고정 크기의 다차원 배열
2. 파이썬 리스트보다 빠르고 메모리 효율적
3. 벡터화 연산으로 반복문 없이 전체 배열 연산 가능
4. dtype으로 데이터 타입 명시 가능
5. shape, ndim, size로 배열 구조 파악
6. 다양한 생성 함수: zeros, ones, arange, linspace 등
7. 난수 생성: 균일 분포, 정규 분포, 정수 난수
8. 시드 설정으로 재현 가능한 난수 생성

"""

print('=' * 70)
print('NumPy 기초 학습 완료!')
print('=' * 70)
