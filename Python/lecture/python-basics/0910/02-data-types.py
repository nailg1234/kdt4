# ========================================
# 변수(Variable) - 데이터를 담는 상자
# ========================================

''' 
변수(Variable)란 무엇인가요?
- 게임 → 플레이어의 점수를 기억
- 쇼핑몰 → 상품의 가격을 저장
- SNS → 사용자의 이름을 기억

변수는 컴퓨터 메모리에서 데이터를 저장하는 공간입니다.
프로그램이 실행되는 동안 필요한 정보를 담아두는 역할을 합니다.
'''

''' 
변수를 상자에 비유해서 이해해보세요:
1. 상자(변수) = 데이터를 담는 공간
2. 물건(데이터) = 저장할 값 (숫자, 문자 등)
3. 이름표(변수명) = 상자를 구분하는 이름
4. 필요할 때 상자에서 물건을 꺼내 사용합니다.

예시: age라는 상자에 20이라는 숫자를 넣어두고,
      나중에 필요할 때 age 상자에서 20을 꺼내 사용
'''

# ========================================
# 변수 선언과 할당 연산자
# ========================================

# 변수 선언 문법: 변수이름 = 값
age = 20          # age라는 변수에 20 저장
name = "김철수"    # name이라는 변수에 "김철수" 저장
height = 175.5    # height라는 변수에 175.5 저장

print(f"나이: {age}, 이름: {name}, 키: {height}")

# = 는 할당 연산자 (Assignment Operator)
# 주의: 수학의 등호(=)와는 다른 의미입니다!
# 오른쪽 값을 왼쪽 변수에 "넣는다", "할당한다"는 의미

# ========================================
# 변수의 값 변경 (재할당)
# ========================================

print(f"변경 전 나이: {age}")    # 20 출력

# 변수의 값은 언제든지 바꿀 수 있습니다 (재할당)
age = 30                        # age 변수에 새로운 값 30 할당
print(f"변경 후 나이: {age}")    # 30 출력

# 이전 값 20은 사라지고, 새로운 값 30이 저장됩니다

# ========================================
# 변수명 작성법: 스네이크 케이스(snake_case)
# ========================================

"""
Python에서 권장하는 변수명 작성법:
- 모든 글자를 소문자로 작성
- 단어와 단어 사이를 언더스코어(_)로 연결
- 의미가 명확하도록 서술적으로 작성
"""

# 좋은 변수명 예시 (snake_case)
student_name = "김철수"         # 학생 이름
user_age = 25                  # 사용자 나이
total_score = 100              # 총점
shopping_cart_items = 5        # 장바구니 아이템 수
is_login_successful = True     # 로그인 성공 여부

print(f"학생: {student_name}, 나이: {user_age}, 점수: {total_score}")

# ========================================
# 다중 할당과 변수 교환
# ========================================

# 여러 변수에 동시에 값 할당
x = 10
y = 20
print(f"교환 전 - x: {x}, y: {y}")

# 값의 교환 (Python의 편리한 기능!)
x, y = y, x  # 이것은 x, y = 20, 10과 같습니다
print(f"교환 후 - x: {x}, y: {y}")

# 한 번에 여러 변수에 다른 값들 할당
X, Y = 30, "a"
print(f"X: {X}, Y: {Y}")

# print 함수의 옵션들
# sep: 여러 값들 사이의 구분자 설정
# end: 줄바꿈 문자 설정 (기본값은 '\n')
print('X는', X, sep='   ', end='')  # 구분자를 공백 3개로, 줄바꿈 없이
print('Y는', Y)                    # 일반적인 출력

# ========================================
# 자료형(Data Types) 상세 설명
# ========================================

"""
Python의 주요 자료형들:
1. 정수(int): 소수점이 없는 숫자 → 2, 3, 12, 25, -10
2. 실수(float): 소수점이 있는 숫자 → 1.1, 41.123, 3.1415
3. 문자(char): 한 글자 → 'a', 'B', '가' (Python에서는 길이 1인 문자열)
4. 문자열(str): 여러 글자의 조합 → "hello", "안녕하세요"
5. 불린(bool): 참/거짓 값 → True, False
"""

# 1. 정수형 (Integer)
student_count = 30              # 학생 수
temperature = -5                # 기온
year = 2024                    # 연도

# 2. 실수형 (Float)
pi = 3.14159                   # 원주율
average_score = 85.5           # 평균 점수
body_temperature = 36.5        # 체온

# 3. 문자열 (String)
greeting_message = "안녕하세요!"  # 인사말
programming_language = "Python"  # 프로그래밍 언어명

# 4. 불린 (Boolean)
is_student = True              # 학생인가? (참)
is_adult = False              # 성인인가? (거짓)

# type() 함수로 자료형 확인
print(f"student_count의 타입: {type(student_count)}")       # <class 'int'>
print(f"pi의 타입: {type(pi)}")                           # <class 'float'>
print(f"greeting_message의 타입: {type(greeting_message)}")  # <class 'str'>
print(f"is_student의 타입: {type(is_student)}")           # <class 'bool'>

# ========================================
# 문자열에서 따옴표 사용하기
# ========================================

# 문자열 안에 따옴표를 포함시키는 방법들:

# 방법 1: 큰따옴표 안에 작은따옴표 사용
message1 = '"파이썬"은 가장 널리 사용되는 프로그래밍 언어 입니다.'
print(message1)

# 방법 2: 작은따옴표 안에 큰따옴표 사용
message2 = "'파이썬'은 가장 널리 사용되는 프로그래밍 언어 입니다."
print(message2)

# 방법 3: 이스케이프 문자(\) 사용
message3 = "\"파이썬\"은 최고의 언어입니다."
message4 = '\'파이썬\'은 최고의 언어입니다.'
print(message3)
print(message4)

# ========================================
# 불린(Boolean) 자료형 상세
# ========================================

# 불린 변수명은 is_, has_, can_ 등으로 시작하는 것이 관례
is_raining = True              # 비가 오고 있나요?
has_license = False           # 면허증이 있나요?
can_drive = True             # 운전할 수 있나요?

print(f'비가 오나요? {is_raining}, 타입: {type(is_raining)}')
print(f'면허증이 있나요? {has_license}, 타입: {type(has_license)}')

# ========================================
# 자료형 변환 (Type Conversion)
# ========================================

"""
때로는 한 자료형을 다른 자료형으로 변환해야 할 때가 있습니다.
int(), float(), str() 함수를 사용하여 변환할 수 있습니다.
"""

# 문자열을 숫자로 변환
string_number = "123"           # 문자열 "123"
converted_int = int(string_number)     # 정수 123으로 변환
converted_float = float(string_number)  # 실수 123.0으로 변환

print(f"원본: {string_number} (타입: {type(string_number)})")
print(f"정수 변환: {converted_int} (타입: {type(converted_int)})")
print(f"실수 변환: {converted_float} (타입: {type(converted_float)})")

# 숫자를 문자열로 변환
number = 456
converted_string = str(number)   # "456"으로 변환
print(f"원본: {number} (타입: {type(number)})")
print(f"문자열 변환: {converted_string} (타입: {type(converted_string)})")

# 주의: 변환할 수 없는 경우 에러 발생
# a = "1a"  # 문자가 섞여 있어서 숫자로 변환 불가능
# a1 = int(a)  # ValueError 발생!

# ========================================
# f-string을 이용한 문자열 포매팅
# ========================================

"""
f-string (f-문자열)은 Python 3.6부터 도입된 강력한 문자열 포매팅 방법입니다.
문자열 앞에 f를 붙이고, 중괄호 {} 안에 변수나 표현식을 넣어 사용합니다.
"""

student_age = 20
student_grade = 85.7

# f-string 사용법
print(f'학생의 나이는 {student_age}세이고, 성적은 {student_grade}점입니다.')

# 중괄호 안에서 계산도 가능
print(f'내년 나이: {student_age + 1}세')
print(f'성적 반올림: {round(student_grade)}점')

# ========================================
# 실습 문제 1: 영화 정보 출력
# ========================================

# 영화 정보를 변수에 저장
title = "Inception"                    # 영화 제목
director = "Christopher Nolan"         # 감독명
year = 2010                           # 개봉연도
genre = "Sci-Fi"                      # 장르

# f-string을 사용하여 영화 정보 출력
print(f"영화 제목: {title}")
print(f"감독: {director}")
print(f"개봉연도: {year}")
print(f"장르: {genre}")

# 한 줄로 모든 정보 출력
print(f"Title: {title}, Director: {director}, Year: {year}, Genre: {genre}")

# ========================================
# 실습 문제 2: 자기소개 출력 (여러 줄 문자열)
# ========================================

# 개인 정보를 변수에 저장
person_name = "Ethan"                 # 이름
person_age = 30                       # 나이
person_mbti = "ESFP"                  # MBTI 성격유형

# 여러 줄 문자열(""")과 f-string 조합 사용
introduction = f"""안녕하세요!
제 이름은 {person_name}이고,
{person_age}살입니다.
제 MBTI는 {person_mbti}예요.
만나서 반갑습니다!"""

print(introduction)

# 한 줄로도 출력 가능
print(f"안녕하세요! 제 이름은 {person_name}, {person_age}살, 제 MBTI는 {person_mbti}예요.")

# ========================================
# 추가 팁: 변수 사용 시 주의사항
# ========================================

"""
변수 사용 시 주의사항:
1. 변수를 선언하기 전에는 사용할 수 없습니다
2. 대소문자를 구분합니다 (name과 Name은 다른 변수)
3. 예약어(if, for, while 등)는 변수명으로 사용할 수 없습니다
4. 의미 있는 변수명을 사용하여 코드 가독성을 높이세요
"""

# 좋은 습관 예시
user_birth_year = 1995                    # 의미가 명확한 변수명
current_year = 2024
calculated_age = current_year - user_birth_year

print(f"출생년도: {user_birth_year}")
print(f"현재년도: {current_year}")
print(f"나이: {calculated_age}세")

print("\n" + "="*50)
print("Python 변수와 데이터 타입 학습 완료!")
print("="*50)
