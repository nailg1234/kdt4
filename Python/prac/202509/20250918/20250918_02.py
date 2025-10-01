# 함수 (function)
#   특정 작업을 수행하는 코드의 묶음
#   한 번 정의 하면 필요할 때 마다 호출하여 재사용할 수 있습니다.

# 함수를 사용하는 이유
#   코드 재사용성 : 같은 코드를 반복 작성할 필요 없음
#   모듈화 : 프로그램을 작은 단위로 나누어 관리
#   가독성 향상 : 코드의 의도를 명확히 표현
#   유지보수 용이 : 수정이 필요할 때 함수만 변경
#   추상화 : 복잡한 로직을 단순한 인터페이스로 제공

# 함수 사용전 - 같은 코드 반복
print('=' * 20)
print('첫번째 섹션')
print('=' * 20)

print('=' * 20)
print('두번째 섹션')
print('=' * 20)

# 함수 사용 코드 재사용


def print_section(title):
    print('=' * 20)
    print(f'{title} 섹션')
    print('=' * 20)


print_section('첫번째')
print_section('두번째')

# 함수 정의와 호출
# 함수 정의(Definition)
# def 함수이름(매개변수):
#     # 실행코드
#     return 반환값

# # 함수 호출(Call)
# 결과 = 함수이름(인자)


def say_hello():
    print('안녕하세요')


say_hello()


def greet(name):
    print(f'안녕하세요 {name} 님!')


greet('김철수')
greet('이영희')


def add(a, b):
    result = a + b
    return result


sum_result = add(1, 5)
print(sum_result)

# 사각형 넓이


def calculate_area(width, height):
    # 문서화 문자열 (Docstring)
    '''
    직사각형의 넓이를 계산합니다.

    parameters:
        width (float): 직사각형의 너비
        height (float) : 직사각형의 높이

    return:
        float: 직사각형의 넓이
    '''

    return width * height


print(calculate_area.__doc__)
print(calculate_area(10, 20))
help(calculate_area)


def greet(name, message="안녕!", sss="hihi"):
    print(f'{name} {message} {sss}')


greet('john')
greet('김철수', '안녕하세요')


def add(a, b=2, c=1, d=4):
    print(a + b + c + d)


print(add(1))
