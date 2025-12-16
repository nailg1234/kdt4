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
