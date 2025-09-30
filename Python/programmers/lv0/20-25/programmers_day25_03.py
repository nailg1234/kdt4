# 연속된 수의 합

# 문제 설명
    # 연속된 세 개의 정수를 더해 12가 되는 경우는 3, 4, 5입니다.
    # 두 정수 num과 total이 주어집니다.
    # 연속된 수 num개를 더한 값이 total이 될 때,
    # 정수 배열을 오름차순으로 담아 return하도록 solution함수를 완성해보세요.

# 제한사항
    # 1 ≤ num ≤ 100
    # 0 ≤ total ≤ 1000
    # num개의 연속된 수를 더하여 total이 될 수 없는 테스트 케이스는 없습니다.

def solution(num, total):
    sum_list = []
    _i = 1
    j = total // num
    j_p = j
    j_m = j

    for i in range(num):
        if _i:
            j_p += 1
            sum_list.insert(0, j_m)
            _i = 0
        else:
            j_m -= 1
            sum_list.append(j_p)
            _i = 1  
    return sum_list

print(solution(3, 12))
print(solution(5, 15))
print(solution(4, 14))
print(solution(5, 5))

# num	total	result
# 3	12	[3, 4, 5]
# 5	15	[1, 2, 3, 4, 5]
# 4	14	[2, 3, 4, 5]
# 5	5	[-1, 0, 1, 2, 3]
