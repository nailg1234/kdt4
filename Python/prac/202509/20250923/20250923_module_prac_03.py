# 실습3. 로또 번호 뽑기
# 문제 설명
# 1. 1~45까지의 수 중에서 랜덤으로 6개의 숫자를 뽑는다.
# 2. 6개의 숫자 중 중복되는 숫자가 없도록 한다.
# 3. 오름차순으로 정렬한 결과를 출력한다.

import random

lotto_list = []

while len(lotto_list) < 6:
    '''
        random.randint(1, 45) -> 1 ~ 45 사이의 정수형 난수 반환
    '''
    lotto_num = random.randint(1, 45)
    if lotto_num not in lotto_list:
        lotto_list.append(lotto_num)

print(sorted(lotto_list))






