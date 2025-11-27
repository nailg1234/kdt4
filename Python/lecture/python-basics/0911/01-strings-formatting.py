# ===========================
# 1. 비교 연산자 (x, y 값 비교)
# ===========================

x = 10
y = 20

# == : 두 값이 같으면 True, 다르면 False
print(f'x == y: {x == y}')  # 10과 20은 같지 않으므로 False

# != : 두 값이 다르면 True
print(f'x != y: {x != y}')  # 10과 20은 다르므로 True

# > : 왼쪽 값이 크면 True
print(f'x > y : {x > y}')   # 10은 20보다 작으므로 False

# >= : 왼쪽 값이 크거나 같으면 True
print(f'x >= y: {x >= y}')  # 10은 20보다 작으므로 False

# < : 왼쪽 값이 작으면 True
print(f'x < y : {x < y}')   # 10은 20보다 작으므로 True

# <= : 왼쪽 값이 작거나 같으면 True
print(f'x <= y: {x <= y}')  # 10은 20보다 작으므로 True

# x, y 값을 15로 다시 설정
x = 15
y = 15

print(f'x <= y: {x <= y}')  # 15는 15와 같으므로 True
print(f'x >= y: {x >= y}')  # 15는 15와 같으므로 True


# ===========================
# 2. 논리 연산자 (and, or, not)
# ===========================

# and : 양쪽 조건이 모두 True여야 True
print(True and True)    # 둘 다 True → True
print(True and False)   # 한쪽이 False → False
print(False and True)   # 한쪽이 False → False
print(False and False)  # 둘 다 False → False

# or : 둘 중 하나라도 True면 True
print(True or True)     # 둘 다 True → True
print(True or False)    # 하나가 True → True
print(False or True)    # 하나가 True → True
print(False or False)   # 둘 다 False → False

# not : True ↔ False 반전
print(f'not True : {not True}')     # True → False
print(f'not False : {not False}')   # False → True

# and, or 혼합
# (True and False) → False, False or True → True
print(True and False or True)
# (False or True) → True, (True and True) → True, True and False → False
print(True and (False or True) and False)


# ===========================
# 3. if 조건문 기초
# ===========================

age = 20

# age가 18 이상이면 성인 출력
if age >= 18:
    print("성인입니다.")


# ===========================
# 4. 문자열을 조건으로 사용
# ===========================

name = "ethan"
name = ""  # 빈 문자열로 바꿨으므로 False로 평가됨

# 문자열이 비어 있지 않으면 True → 출력
if name:
    print("이름이 존재합니다.")  # 출력되지 않음 (name은 "")


# ===========================
# 5. True / False 조건문
# ===========================

if True:
    print("무조건 실행")  # 항상 실행됨

if False:
    print("실행되지 않습니다.")  # 실행 안됨

if True:
    pass  # 실행할 코드가 없을 때 pass 사용
print('조건문관 상관없습니다.')  # if와 상관없이 항상 실행


# ===========================
# 7. 단축 평가 (short-circuit evaluation)
# ===========================

# and : 앞 조건이 False면 뒤 조건은 확인하지 않음
# 따라서 print("단축 평가")는 실행되지 않음
if False and print("단축 평가"):
    print('실행')

# or : 앞 조건이 False면 뒤 조건을 확인함
# print("단축 평가")가 실행되고, 그 결과 None(False 취급)이지만
# 마지막 True 때문에 조건문이 실행됨
if False or print("단축 평가") or True:
    print('실행')


# ===========================
# 8. if ~ else 기본
# ===========================

name = ""  # 빈 문자열 → False 취급됨

if name:
    print(f'이름은: {name}')
else:
    print('이름을 작성해주세요')  # 실행됨

if False:
    print('if 실행')
else:
    print('else 실행')  # 실행됨


# ===========================
# 10. if ~ elif ~ else (다중 조건문)
# ===========================

name = '철수'

if name == '김철수':
    print(f'김철수 입니다.')
elif name == '철수':
    print(f'철수 입니다.')
else:
    print('이름을 입력해주세요.')


# ===========================
# 11. 나이와 학년 조건문
# ===========================

age = 20
name = '철수'
grade = 2

# name이 빈 문자열이 아니므로 True → 출력됨
if name:
    print(f'이름: {name}')

# 나이가 20보다 큰지 검사
if age > 20:
    print('성인입니다.')
else:
    print('미성년자입니다.')  # age = 20이므로 else 실행

# 학년 검사
if grade > 3:
    print('3학년 입니다')
elif grade == 2:
    print('2학년 입니다')  # grade = 2이므로 실행
else:
    print('1학년 입니다')


if True:
    if True:
        if True:
            pass
        if True:
            pass
        if True:
            pass
