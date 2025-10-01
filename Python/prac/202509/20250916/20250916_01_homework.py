# 문제 1. 딕셔너리 핵심 개념 통합 실습
# ▪ 1단계: 빈 딕셔너리 생성 : user라는 이름의 빈 딕셔너리를 생성하세요.
# ▪ 2단계: 사용자 기본 정보 추가
# • "username": "skywalker"
# • "email": "sky@example.com"
# • "level": 5
# ▪ 3단계: 값 읽기 - "email" 값을 변수 email_value에 저장하고 출력하세요.
# ▪ 4단계: 값 수정 - "level" 값을 6으로 수정하세요.
# ▪ 5단계: 안전하게 키 조회 - 딕셔너리에 "phone" 키가 없다면 "미입력"이라는 문자열을 출력하도록 하세요.
# ▪ 6단계: 항목 추가 및 삭제
# • update()를 사용해 "nickname": "sky" 항목을 추가하세요.
# • "email" 항목을 삭제하세요.
# • "signup_date" 키가 없다면 "2025-07-10"으로 추가하세요 (setdefault() 사용).
# • 최종 user 딕셔너리를 출력하세요.
# 작성한 코드와 출력 결과를 댓글로 남겨주세요!
user = {}
user.update({"username": 'skywalker', 'email': 'sky@example.com', 'level': 5})

email_value = user.get('email')
print(email_value)

user['level'] = 6

user.get('phone', '미입력')
user.update({"nickname": "sky"})

del user["email"]

if 'signup_date' not in list(user.keys()):
    user.update({'signup_date': '2025-07-10'})

print(user)


# 문제 2. 학생 점수 관리
# 1. 빈 딕셔너리 students를 생성한다.
# 2. "Alice", "Bob", "Charlie" 세 학생의 점수를 각각 85, 90, 95로 추가한다.
# 3. "David" 학생의 점수(80)를 추가한다.
# 4. "Alice"의 점수를 88로 수정한다.
# 5. "Bob"을 딕셔너리에서 삭제한다.
# 6. 최종 students 딕셔너리를 출력한다.

students = dict()

students = {"Alice": 80, "Bob": 90, "Charlie": 95}
students.update({"David": 80, "Alice": 88})
del students['Bob']
print(students)
