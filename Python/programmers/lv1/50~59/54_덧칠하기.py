def solution(n, m, section):
    lst = []
    cnt = 0
    for i in section:
        if lst:
            if lst[0] + m > i:
                lst.append(i)
            else:
                cnt += 1
                lst = [i]
        else:
            lst.append(i)
    return cnt + 1

print(solution(8, 4, [2, 3, 6])) # 2
print(solution(5, 4, [1, 3])) # 1
print(solution(4, 1, [1, 2, 3, 4])) # 4
