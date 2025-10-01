# 아래 가격표를 참고하여 금액을 입력하고 원하는 식품을 선택하면 해당식품을 구매할수있는지 판단하여 출력하는 프로그램을 만들어보세요
# 김밥 2,500원
# 삼각김밥 1,500원
# 도시락 4,000원

# 입력 금액이 식품가격 이상이면 구매성공 메세지
# 금액이 부족할 경우 "금액이 부족합니다" 출력

price = int(input("금액을 입력해주세요.  "))

foodname = input("식품명을 입력해주세요.  ")

if foodname == '도시락':
    if price >= 4000:
        print('도시락 구매성공')
    else:
        print('금액이 부족합니다.')
elif foodname == '김밥':
    if price >= 2500:
        print('김밥 구매성공')
    else:
        print('금액이 부족합니다.')
elif foodname == '삼각김밥':
    if price >= 1500:
        print('삼각김밥 구매성공')
    else:
        print('금액이 부족합니다.')
else:
    print('잘못된 메뉴입니다.')
