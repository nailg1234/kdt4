# 실습5. 다음 생일까지 남은 날짜 계산하기
# 문제 설명
# 1. 사용자로부터 생일(월-일, 예: 07-25)을 입력 받으세요.
# 2. 오늘 날짜를 기준으로 올해 또는 내년의 생일까지 남은 날짜(일 수)를 계산해서 출력하세요.
# • 올해 생일이 지났으면 내년까지 남은 일수로, 아직 안 지났으면 올해 생일까지 남은 일수로 계산
# 요구 사항
# • 날짜 연산에는 반드시 datetime 모듈을 사용할 것.

import datetime


input_mon, input_day = [int(i) for i in input('생일을 월-일 예:07-25을 입력 받으세요.').split('-')]


date_today = datetime.date.today()

my_birth_day= datetime.date(year = date_today.year, month = input_mon, day = input_day)

if date_today < my_birth_day :
    print('올해 생일 : ', my_birth_day)
else:
    next_year_my_birth_day = datetime.date(year = date_today.year + 1, month = input_mon, day = input_day)
    print('내년 생일 : ', next_year_my_birth_day)


