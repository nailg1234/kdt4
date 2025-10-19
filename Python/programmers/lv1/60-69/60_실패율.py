def solution(N, stages):
    failrate = []
    for i in range(1, N + 1):
        cnt = stages.count(i)
        if cnt:
            s_len = len([j for j in stages if j >= i])
            failrate.append([i, cnt / s_len])
        else:
            failrate.append([i, -i])
    failrate.sort(key = lambda x : x[1], reverse = True)
    return [arr[0] for arr in failrate]
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3])) # [3,4,2,1,5]
print(solution(4, [4,4,4,4,4])) # [4,1,2,3]