# 문제 1. 딕셔너리 핵심 개념 통합 실습
# 1. user라는 이름의 빈 딕셔너리 생성
#
user = dict()
# user = {}
print()

# 2. 사용자 기본 정보 추가
user['username'] = 'skywalker'
user['email'] = 'sky@example.com'
user['level'] = 5
print('user', user)
print()

# 3. 값 읽기
email_value = user['email']
print('email_value', email_value)
print()

# 4. 값 수정
user['level'] = 6
print('user', user)
print()

# 5. 안전하게 키 조회
print(user.get('phone', '미입력'))
print()

# 6. 항목 추가 및 삭제
user.update({'nickname': 'sky'})
del user['email']
print(user.setdefault('signup_date', '2025-07-10'))
print('user', user)
print()
# 문제 2. 학생 점수 관리
students = {}

names = ['Alice', 'Bob', 'Charlie']
score = [85, 90, 95]

students = dict(zip(names, score))

students.update({'David': 80})
students['Alice'] = 88

del students['Bob']

print('students', students)


print()
print()
print()
print()
print()
print()
print()
print()
