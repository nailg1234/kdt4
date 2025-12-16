# 소인수분해

# 문제 설명
#   소인수분해란 어떤 수를 소수들의 곱으로 표현하는 것입니다.
#   예를 들어 12를 소인수 분해하면 2 * 2 * 3 으로 나타낼 수 있습니다. 따라서 12의 소인수는 2와 3입니다. 자연수 n이 매개변수로 주어질 때 n의 소인수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.

# 제한사항
#   2 ≤ n ≤ 10,000

def solution(n):

    i = 2
    new_set = set()
    while n != i:
        if not n % i:
            new_set.add(i)
        i += 1
    print(new_set)
    new_list = list()

    for j in new_set:
        k = 2

        while k < j :

            if j // k and not j % k :
                break
            
            k += 1
        else:
            new_list.append(j)
    
    return sorted(new_list) if new_list else [n]


print(solution(100))