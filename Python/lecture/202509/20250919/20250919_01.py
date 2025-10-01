# 파이썬의 선언하는 모든 객체 힙 영역에 들어감

# 함수의 범위(Scope)

'''
    변수의 범위란?
    변수가 살아있는(접근 가능한)영역을 범위(Sope)라고 합니다.

    집 = 전역범위
    방 = 지역볌위
    방안의 물건은 그 방에서만 사용 가능
    거실의 물건은 모든 방에서 사용 가능 
'''

# 전역 변수 (Global Variable)

global_var = '전역 변수'


def my_func():
    # 지역 변수 (Local Variable)

    local_var = '지역 변수'
    print(global_var)
    print(local_var)


print(global_var)  # 전역 변수 접근 가능
# print(local_var) # 에러! 함수 밖에서 지역 변수 접근 불가

# Global 키워드
# 함수 안에서 전역 변수를 "수정"하려면 global 키워드를 사용합니다.

count = 0  # 전역 변수

# def increment_wrong():
# count = count + 1 # 에러 지역변수로 취급됨


def increment_right():
    global count
    count = count + 1


score = 0


def add_score(points):
    global score
    score += points
    print(f'점수 획득 : 현재 점수 : {score}')


def reset_score():
    global score
    score = 0

    print('점수 초기화')


add_score(100)
add_score(200)

print(score)

reset_score()

print(score)

# 전역 변수 사용 주의

# 전역 변수는 편리하지만 과도하게 사용하면 코드가 복잡해집니다.

total = 0
count = 0


def add_number(num):
    global total, count
    total += num
    count += 1


def get_average():
    global total, count  # global 남용
    return total / count if count > 0 else 0


# 좋은 예
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


numbers = [56, 53, 56, 64]

# 함수에 원본 그대로 넘어옴


def num_append(numbers):
    numbers.append(6)


numbers = [1, 2, 3, 4, 5]

print('함수 호출 전 numbers : ', numbers)

num_append(numbers)

print('함수 호출 후 numbers : ', numbers)

# 불변 타입
# 정수 , 실수, 문자열, 튜플

# 가변 타입
# 리스트, 딕셔너리, 셋


info_dic = {'name': '김철수', 'age': 20}


def change_info(info):
    info['name'] = '이영희'
    info['age'] = 25


print('함수 호출 전 info_dic:', info_dic)
change_info(info_dic)
print('함수 호출 전 info_dic:', info_dic)


# def outer():
#     a = 10

#     def inner():
#         nonlocal a
#         a += 5
#         print(f'[inner] a : {a}')
#     inner()
#     print(f'[outer] a : {a}')


# outer()
