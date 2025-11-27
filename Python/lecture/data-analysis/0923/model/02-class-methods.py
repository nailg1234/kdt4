
# ================================
# 2. 수학 관련 내장함수
# ================================

print("\n[ abs() - 절댓값 ]")
print("음수를 양수로, 양수는 그대로")

numbers = [-10, -3.14, 0, 5, 15.7]
print("절댓값 계산:")
for num in numbers:
    print(f"  abs({num}) = {abs(num)}")

print("\n실전 활용: 두 점 사이의 거리")


def distance_1d(x1, x2):
    """1차원에서 두 점 사이의 거리"""
    return abs(x2 - x1)


point_pairs = [(10, 3), (-5, 7), (0, -8)]
for x1, x2 in point_pairs:
    dist = distance_1d(x1, x2)
    print(f"  점 {x1}과 점 {x2} 사이의 거리: {dist}")

print("\n" + "-" * 60)
print("[ round() - 반올림 ]")
print("소수점 자리수 지정 가능")

values = [3.14159, 2.71828, 1.41421, 9.99999, 10.5, 11.5]

print("다양한 반올림:")
for val in values:
    print(f"  {val} → 정수: {round(val)}, 소수점 2자리: {round(val, 2)}")

print("\n성적 평균 계산:")
scores = [85.7, 92.3, 78.9, 88.1, 95.6]
average = sum(scores) / len(scores)
print(f"  원점수들: {scores}")
print(f"  평균: {average} → 반올림: {round(average, 1)}")

print("\n" + "-" * 60)
print("[ min(), max() - 최솟값, 최댓값 ]")
print("여러 값 또는 시퀀스에서 최솟값/최댓값 찾기")

# 여러 값에서 찾기
temp_today = [15.2, 18.7, 22.1, 19.8, 16.3]
print(f"오늘 온도 변화: {temp_today}")
print(f"  최저온도: {min(temp_today)}°C")
print(f"  최고온도: {max(temp_today)}°C")
print(f"  온도차: {max(temp_today) - min(temp_today):.1f}°C")

# 여러 인수로 사용
print(f"\nmin(10, 5, 15, 3) = {min(10, 5, 15, 3)}")
print(f"max(10, 5, 15, 3) = {max(10, 5, 15, 3)}")

# 문자열에서도 사용 가능 (사전순)
names = ['김철수', '이영희', '박민수', '최지연']
print(f"\n이름 리스트: {names}")
print(f"  사전순 첫 번째: {min(names)}")
print(f"  사전순 마지막: {max(names)}")

print("\n성적 분석:")
student_scores = {
    '김철수': 85,
    '이영희': 92,
    '박민수': 78,
    '최지연': 88,
    '정다영': 95
}

# 점수만 추출해서 최고/최저 찾기
scores = student_scores.values()
min_score = min(scores)
max_score = max(scores)

# 최고/최저 점수 받은 학생 찾기
top_student = max(student_scores, key=student_scores.get)
bottom_student = min(student_scores, key=student_scores.get)

print(f"  최고점: {max_score}점 ({top_student})")
print(f"  최저점: {min_score}점 ({bottom_student})")

print("\n" + "-" * 60)
print("[ sum() - 합계 ]")
print("숫자 시퀀스의 총합 계산")

# 기본 사용법
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(f"{numbers}의 합: {total}")

# 시작값 지정
total_with_start = sum(numbers, 100)  # 100부터 시작해서 더함
print(f"{numbers}의 합 (시작값 100): {total_with_start}")

# 실전 활용: 쇼핑몰 장바구니
cart_items = {
    '노트북': 1200000,
    '마우스': 50000,
    '키보드': 120000,
    '모니터': 300000
}

print("\n🛒 쇼핑몰 장바구니:")
for item, price in cart_items.items():
    print(f"  {item}: {price:,}원")

total_price = sum(cart_items.values())
print(f"  총 금액: {total_price:,}원")

# 할인 적용
if total_price >= 1000000:
    discount = total_price * 0.1  # 10% 할인
    final_price = total_price - discount
    print(f"  할인액 (10%): -{discount:,}원")
    print(f"  최종 금액: {final_price:,}원")

print("\n" + "=" * 80)
print("📝 문자열/리스트 관련 내장함수")
print("=" * 80)

# ================================
# 3. 문자열/리스트 관련 내장함수
# ================================

print("\n[ len() - 길이 ]")
print("문자열, 리스트, 튜플, 딕셔너리 등의 길이")

examples = [
    "안녕하세요",
    [1, 2, 3, 4, 5],
    (10, 20, 30),
    {'a': 1, 'b': 2, 'c': 3},
    {1, 2, 3, 4}
]

print("다양한 객체의 길이:")
for i, obj in enumerate(examples, 1):
    print(f"  {i}. {obj} → 길이: {len(obj)}")

print("\n비밀번호 강도 검사:")


def check_password_strength(password):
    """비밀번호 강도를 검사하는 함수"""
    length = len(password)
    if length < 6:
        return "약함 (6자 미만)"
    elif length < 10:
        return "보통 (6-9자)"
    else:
        return "강함 (10자 이상)"


test_passwords = ['123', 'password', 'mypassword123']
for pwd in test_passwords:
    strength = check_password_strength(pwd)
    print(f"  '{pwd}' ({len(pwd)}자): {strength}")

print("\n" + "-" * 60)
print("[ sorted() - 정렬 ]")
print("원본을 변경하지 않고 새로운 정렬된 리스트 반환")

# 기본 정렬
numbers = [64, 34, 25, 12, 22, 11, 90]
names = ['김철수', '이영희', '박민수', '최지연']

print("숫자 정렬:")
print(f"  원본: {numbers}")
print(f"  오름차순: {sorted(numbers)}")
print(f"  내림차순: {sorted(numbers, reverse=True)}")
print(f"  원본 확인: {numbers}")  # 원본은 변경되지 않음

print("\n한글 이름 정렬:")
print(f"  원본: {names}")
print(f"  가나다순: {sorted(names)}")
print(f"  역순: {sorted(names, reverse=True)}")

# key 매개변수 활용
print("\n고급 정렬 - key 매개변수:")
words = ['python', 'java', 'c', 'javascript', 'go']

print(f"원본: {words}")
print(f"길이순 정렬: {sorted(words, key=len)}")
print(f"길이 역순: {sorted(words, key=len, reverse=True)}")

# 학생 성적 정렬
students = [
    ('김철수', 85, 'A'),
    ('이영희', 92, 'A+'),
    ('박민수', 78, 'B'),
    ('최지연', 88, 'A'),
    ('정다영', 95, 'A+')
]

print("\n학생 성적 정렬:")
print("점수순 (오름차순):")
by_score = sorted(students, key=lambda x: x[1])
for name, score, grade in by_score:
    print(f"  {name}: {score}점 ({grade})")

print("\n점수순 (내림차순):")
by_score_desc = sorted(students, key=lambda x: x[1], reverse=True)
for name, score, grade in by_score_desc:
    print(f"  {name}: {score}점 ({grade})")

print("\n" + "-" * 60)
print("[ reversed() - 역순 ]")
print("시퀀스의 요소들을 역순으로 반환 (iterator 객체)")

original_list = [1, 2, 3, 4, 5]
original_string = "Hello"

print(f"리스트 역순: {original_list} → {list(reversed(original_list))}")
print(f"문자열 역순: '{original_string}' → '{''.join(reversed(original_string))}'")

# 실전 활용: 회문(palindrome) 검사


def is_palindrome(text):
    """회문인지 검사하는 함수"""
    # 공백과 대소문자 무시
    clean_text = text.replace(' ', '').lower()
    return clean_text == ''.join(reversed(clean_text))


test_words = ['level', 'hello', 'A man a plan a canal Panama', '기러기', '파이썬']
print("\n회문 검사:")
for word in test_words:
    result = is_palindrome(word)
    print(f"  '{word}': {'✅ 회문' if result else '❌ 회문 아님'}")

print("\n" + "=" * 80)
print("🔄 타입 변환 내장함수")
print("=" * 80)
