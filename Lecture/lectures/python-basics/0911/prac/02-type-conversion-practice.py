# # ===========================
# # 1. 사용자 입력 (날씨 예제)
# # ===========================

# weather = input('오늘의 날씨를 입력하세요. (비/ 맑음):')

# if weather == '비':       # 사용자가 '비'라고 입력하면
#     print("우산을 챙기세요!")

# if weather == '맑음':    # 사용자가 '맑음'이라고 입력하면
#     print("선크림을 바르세요!")


# # ===========================
# # 2. 홀짝 판별 프로그램
# # ===========================

# num = int(input('정수를 입력하세요:'))  # 사용자에게 숫자 입력받음

# if num % 2:  # num % 2 → 0(짝수) → False, 1(홀수) → True
#     print('홀수입니다.')
# else:
#     print('짝수입니다.')

# # ===========================
# # 3. 나이에 따른 영화 관람
# # ===========================

# age = int(input('나이를 입력하세요.'))

# if age >= 19:
#     print('청소년 관람불가 가능')
# elif age >= 16:
#     print('15세 이상관람 가능')
# elif age >= 13:
#     print('12세 이상관람 가능')
# else:
#     print('전체 관람 가능')

# # ===========================
# # 4. 시,분,초 구하기
# # ===========================

# second = int(input('초를 입력해주세요.'))

# # 시간을 구하는 식 (60초 * 60분) 1시간
# if second >= 3600:
#     print(f'{second // 3600} 시', end=' ')

# second %= 3600

# # 분을 구하는 식 (60초)
# if second >= 60:
#     print(f'{second // 60} 분', end=' ')

# second %= 60

# print(f'{second} 초')

# # ===========================
# # 5. 편의점 도시락 구매하기
# # ===========================

price_kimbab = 2500
price_samgak = 1500
price_dosirak = 4000

money = int(input('금액을 입력해주세요:'))

food = input('구매할 식품을 입력하세요: (김밥, 삼각김밥, 도시락)')

if food == '김밥':
    if money >= price_kimbab:
        print('구매 성공')
    else:
        print('구매 실패')
elif food == '삼각김밥':
    if money >= price_samgak:
        print('구매 성공')
    else:
        print('구매 실패')
elif food == '도시락':
    if money >= price_dosirak:
        print('구매 성공')
    else:
        print('구매 실패')
else:
    print('잘못된 메뉴 입니다.')
