# 매개변수와 인자

'''
    매개변수 (Parameter): 함수 정의 시 사용하는 변수
    인자(Argument): 함수 호출시 전달하는 실제 값
'''


def multiply(x, y):  # x, y는 매개변수
    return x * y


result = multiply(3, 5)

# 위치 인자(Positional Arguments)


def introduce(name, age, city):
    print(f'{name} {age} {city}')


# name = 김철수, age = 25, city = 서울
introduce('김철수', 25, '서울')

# 키워드 인자

# 순서와 상관없이 이름을 전달


def introduce2(city='서울', age=25, name='김철수'):
    print(f'{name} {age} {city}')


introduce2('김철수', 25, '서울')


def introduce3(name='김철수', age=25, city='부산'):
    print(f'{name} {age} {city}')


# 위치 인자, 키워드 혼용
introduce3('김김김', city='서울', age=28)

# 위치 인자는 키워드 인자보다 앞에 와야함

# 반환값(return)
# 단일 값 반환


def square(n):
    return n ** 2


result = square(5)
print(result)  # 25

# 여러 값 반환


def calculate_stats(number):
    total = sum(number)
    avg = total / len(number)
    maxnum = max(number)
    minnum = min(number)

    return total, avg, maxnum, minnum


numbers = [100, 140, 230, 200]

a, b, c, d = calculate_stats(numbers)

print('total : ', a)
print('avg : ', b)
print('max : ', c)
print('num : ', d)

stats = calculate_stats(numbers)

print(stats)

# return의 특징


def check_positive(number):
    if number > 0:
        return "양수"
    elif number < 0:
        return "음수"
    else:
        return '0'

    print('코드가 실행이 될까요?')

# return은 함수를 종료 시킨다.


check_positive(4)
check_positive(-1)
check_positive(0)

# 조기 반환(Early Return)


def divide(a, b):
    # 예외 상황을 먼저 처리
    if b == 0:
        return "0으로 나눌 수 없습니다."

    return a / b


print(divide(10, 2))
print(divide(10, 0))

# 기본값 매개변수


def greet(name, greeting="안녕하세요."):
    print(f'{greeting} {name}')


greet('김철수')

greet('이영희', '반갑습니다.')

# 여러 기본값


def create_profile(name, age=25, city='서울', job='개발자'):
    return {
        'name': name,
        'age': age,
        'city': city,
        'job': job
    }


print(create_profile('박민수'))
print(create_profile('김철수', 35))
print(create_profile('이영희', job='모델', city='부산'))

# 가변 위치 인자(*args)


def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num

    return total


print(sum_all(1, 2, 3))
print(sum_all())

# 가변 키워드 인자 (**kwargs)


def print_info(**user):
    # 키워드 인자를 딕셔너리로 받습니다.
    print(type(user))
    print('user', user)
    for key, value in user.items():
        print(f'{key} : {value}')


print(print_info(name='김철수', age=20, city='서울'))


def create_student(**info):
    '''
        학생 정보를 생성합니다.
    '''
    student = {
        "name": info.get('name', '이름 없음'),
        "age": info.get('age', 20),
        "grade": info.get('grade', 1),
        "subjects": info.get('subjects', []),
    }

    return student


student1 = create_student(name='김철수', subjects=['python'])
print(student1)  # {'name': '김철수', 'age': 20, 'grade': 1, 'subjects': []}
