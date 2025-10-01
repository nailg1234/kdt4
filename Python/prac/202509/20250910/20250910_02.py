# 변수(Variable) - 데이터를 담는 상자
'''
변수란
게임 -> 플레이어의 점수 기억
쇼핑몰 -> 상품의 가격을 저장
SNS -> 사용자의 이름을 기억

데이터를 저장하는 공간을 변수 라고 합니다.
'''

'''
상자(변수)에 물건(데이터)을 넣습니다.
이름표(변수명)로 상자를 구분합니다.
필요할 때 상자에서 물건을 꺼내 사용합니다.
'''

# 변수 선언
# 변수이름 = 값

age = 20
name = "김철수"
height = 175.5
# = -> 할당 연산자 (넣는다는 의미, 수학의 등호와는 다름!!!!)
# 변수의 값은 바꿀 수 있다.

# 재할당
age = 30
print(age)

# 스네이크 케이스(snake_case)
student_name = "김철수"
user_age = 25
total_Score = 100

x = 10
y = 20

# 값의 교환, 여러 변수 할당
x, y = y, x
# x, y = 20, 10
X, Y = 30, "a"
# sep = 여러값 구분자, end = '줄바꿈 구분자'
print('X', X, sep='   ', end=' ')
print('Y', Y)


# 자료형
# 정수, 실수, 문자, 문자열
# 정수 => 2, 3, 12, 25
# 실수 => 1.1, 41.123, 3.1415
# 문자 => 'a', 'B'
# 문자열 => "aaa", "Hello"
print('"파이썬"은 가장 널리 사용되는 프로그래밍 언어 입니다.')
print("'파이썬'은 가장 널리 사용되는 프로그래밍 언어 입니다.")

true = True
false = False

print('true', true)
print('false', false)

print('true', type(true))
print('false', type(false))

a = "1"
b = '1'
a1 = int(a)
b1 = float(b)
print('a type:', type(a1))
print('b type:', type(b1))
print(b1)


c = 2  # 정수형 int
d = 2.1  # 실수형 float

print(int(True))
print(int(False))
# 문자열 포메팅 f-string
print(f'c의 숫자는 {c} {d}입니다.')
