# 파이썬 내장함수 및 random 모듈 완전 가이드

"""
이 가이드는 파이썬에서 자주 사용되는 내장함수들과 random 모듈의 
다양한 함수들을 실전 예제와 함께 설명합니다.

주요 내용:
1. random 모듈 - 난수 생성과 무작위 선택
2. 수학 관련 내장함수 - abs, round, min, max, sum 등
3. 문자열/리스트 관련 내장함수 - len, sorted, reversed 등
4. 타입 변환 함수 - int, float, str, list, tuple 등
5. 입출력 함수 - input, print의 고급 활용
6. 기타 유용한 함수들 - zip, enumerate, range 등
"""

from collections import Counter
import random
import math

print("=" * 80)
print("🎲 RANDOM 모듈 - 난수 생성과 무작위 선택")
print("=" * 80)

# ================================
# 1. random 모듈 기본 함수들
# ================================

print("\n[ 1. random.random() - 0.0 이상 1.0 미만의 실수 ]")
print("기본 난수 생성기, 가장 기본적인 함수")

for i in range(5):
    rand_float = random.random()
    print(f"  시도 {i+1}: {rand_float:.6f}")

print("\n활용 예제: 확률 기반 이벤트")


def probability_event(success_rate):
    """주어진 확률로 성공/실패를 결정"""
    return random.random() < success_rate


# 30% 확률로 성공하는 이벤트 10번 시뮬레이션
successes = 0
for i in range(10):
    if probability_event(0.3):  # 30% 확률
        successes += 1
        print(f"  시도 {i+1}: ✅ 성공!")
    else:
        print(f"  시도 {i+1}: ❌ 실패")

print(f"  총 성공률: {successes}/10 = {successes*10}%")

print("\n" + "-" * 60)
print("[ 2. random.randint(a, b) - a 이상 b 이하의 정수 ]")
print("양 끝값을 포함하는 정수 난수 생성")

print("주사위 굴리기 (1~6):")
dice_results = []
for i in range(10):
    dice = random.randint(1, 6)
    dice_results.append(dice)
    print(f"  굴리기 {i+1}: {dice}")

print(f"결과 분석: 평균 = {sum(dice_results)/len(dice_results):.2f}")

print("\n로또 번호 생성기 (1~45 중 6개, 중복 없음):")
lotto_numbers = []
while len(lotto_numbers) < 6:
    number = random.randint(1, 45)
    if number not in lotto_numbers:  # 중복 방지
        lotto_numbers.append(number)

lotto_numbers.sort()  # 정렬해서 보기 좋게
print(f"  🎰 로또 번호: {lotto_numbers}")

print("\n" + "-" * 60)
print("[ 3. random.choice(sequence) - 시퀀스에서 하나의 요소 선택 ]")
print("리스트, 튜플, 문자열 등에서 무작위로 하나 선택")

# 기본 사용법
colors = ['빨강', '파랑', '노랑', '초록', '보라']
foods = ('피자', '햄버거', '치킨', '파스타', '스시')
greeting = "안녕하세요"

print("무작위 선택 예제:")
for i in range(5):
    chosen_color = random.choice(colors)
    chosen_food = random.choice(foods)
    chosen_char = random.choice(greeting)
    print(f"  {i+1}: {chosen_color} 색의 {chosen_food}, 문자 '{chosen_char}'")

print("\n실전 활용: 랜덤 문장 생성기")
subjects = ['고양이가', '강아지가', '새가', '토끼가', '코끼리가']
actions = ['뛰어다니고', '잠을 자고', '밥을 먹고', '노래하고', '춤추고']
objects = ['공원에서 놀았다', '집에서 쉬었다', '친구를 만났다', '모험을 떠났다']

print("🎭 랜덤 동화 생성:")
for i in range(3):
    sentence = f"{random.choice(subjects)} {random.choice(actions)} {random.choice(objects)}"
    print(f"  이야기 {i+1}: {sentence}")

print("\n" + "-" * 60)
print("[ 4. random.choices(sequence, k=n) - 중복 허용하여 n개 선택 ]")
print("동일한 요소가 여러 번 선택될 수 있음")

menu = ['떡볶이', '순대', '튀김', '김밥', '라면']

print("분식점 주문 시뮬레이션 (중복 주문 가능):")
# 5번 주문 (같은 메뉴 여러 번 주문 가능)
orders = random.choices(menu, k=5)
print(f"  주문 내역: {orders}")

# 주문 통계
order_count = Counter(orders)
print("  주문 통계:")
for item, count in order_count.items():
    print(f"    {item}: {count}개")

print("\n가중치가 있는 선택 (weights 매개변수):")
# 각 메뉴별로 선택될 확률을 다르게 설정
weights = [30, 20, 25, 15, 10]  # 떡볶이가 가장 인기
weighted_orders = random.choices(menu, weights=weights, k=10)
print(f"  가중치 적용 주문: {weighted_orders}")

weighted_count = Counter(weighted_orders)
print("  가중치 적용 통계:")
for item, count in weighted_count.items():
    percentage = (count / 10) * 100
    print(f"    {item}: {count}개 ({percentage}%)")

print("\n" + "-" * 60)
print("[ 5. random.sample(sequence, k) - 중복 없이 k개 선택 ]")
print("동일한 요소는 한 번만 선택됨")

participants = ['김철수', '이영희', '박민수', '최지연', '정다영',
                '윤서준', '한소미', '조현우', '신예린', '오태현']

print("🏆 경품 추첨 (중복 당첨 없음):")
winners = random.sample(participants, k=3)
prizes = ['1등: 아이폰', '2등: 에어팟', '3등: 스타벅스 기프티콘']

for i, winner in enumerate(winners):
    print(f"  {prizes[i]} - {winner}")

print(f"\n당첨자 외 참가자: {[p for p in participants if p not in winners]}")

print("\n팀 나누기:")
team_size = 4
teams = []
remaining = participants.copy()

team_num = 1
while len(remaining) >= team_size:
    team = random.sample(remaining, k=team_size)
    teams.append(team)
    print(f"  팀 {team_num}: {team}")

    # 선택된 사람들을 remaining에서 제거
    for member in team:
        remaining.remove(member)
    team_num += 1

if remaining:
    print(f"  남은 인원: {remaining}")

print("\n" + "-" * 60)
print("[ 6. random.shuffle(sequence) - 리스트를 무작위로 섞기 ]")
print("원본 리스트를 직접 수정 (in-place 연산)")

# 카드 덱 만들기
suits = ['♠', '♥', '♦', '♣']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = [f"{suit}{rank}" for suit in suits for rank in ranks]

print(f"카드 덱 생성 완료: 총 {len(deck)}장")
print(f"셔플 전 처음 10장: {deck[:10]}")

# 카드 섞기
random.shuffle(deck)
print(f"셔플 후 처음 10장: {deck[:10]}")

# 카드 나누기
print("\n🃏 포커 게임: 각자 5장씩 배분")
players = ['플레이어1', '플레이어2', '플레이어3', '플레이어4']
hands = {player: [] for player in players}

for _ in range(5):  # 5장씩 나누어주기
    for player in players:
        card = deck.pop()  # 덱에서 카드 한 장 빼기
        hands[player].append(card)

for player, cards in hands.items():
    print(f"  {player}: {cards}")

print("\n" + "-" * 60)
print("[ 7. random.uniform(a, b) - a와 b 사이의 실수 ]")
print("특정 범위의 실수 난수 생성")

print("온도 시뮬레이션 (18.5°C ~ 25.3°C):")
for day in range(7):
    temperature = random.uniform(18.5, 25.3)
    print(f"  {day+1}일차: {temperature:.1f}°C")

print("\n키와 몸무게 랜덤 생성:")
for i in range(5):
    height = random.uniform(150, 190)  # 키 (cm)
    weight = random.uniform(45, 85)    # 몸무게 (kg)
    bmi = weight / ((height/100) ** 2)
    print(f"  사람 {i+1}: {height:.1f}cm, {weight:.1f}kg (BMI: {bmi:.1f})")

print("\n" + "=" * 80)
print("🔢 수학 관련 내장함수")
print("=" * 80)
