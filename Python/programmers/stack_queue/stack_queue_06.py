# 주식가격

# 문제 설명
#   초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

# 제한사항
#   prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
#   prices의 길이는 2 이상 100,000 이하입니다.

def solution(prices):
    
    prices_len = len(prices)
    j_num, l_list = 0, [] 

    for i in range(prices_len - 1): # 마지막 가격 비교대상이 없기 때문에 반복 제외
        for j in range(1, prices_len - i): # 큰 for문 끝날때마다 작은 for문 탐색 범위 조정
            j_num = j # 작은 가격 몇번째 인덱스에서 찾았는지 체크용
            
            if prices[i] > prices[j + i]: # 현재 가격보다 작은 가격 찾았으면 작은 for문 빠져나옴
                break

        l_list.append(j_num) # 작은 가격 찾은 인덱스 넣기

    else:
        l_list.append(0) # for - else 마지막 가격 비교대상 없어서 무조건 0

    return l_list