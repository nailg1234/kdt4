def solution(today, terms, privacies):
    answer = []
    d = dict()
    for _s in terms:
        l = _s.split()
        d[l[0]] = int(l[1])
    for _idx, _p in enumerate(privacies, start = 1):
        l = _p.split()
        term = d[l[1]] # 유효기간
        nums = l[0].split('.')
        v = int(nums[1]) + term + int(nums[0]) * 12
        v = int(str(v) + nums[2])
        todays = today.split('.')
        t = int(todays[1]) + int(todays[0]) * 12
        t = int(str(t) + todays[2])
        if v <= t:
            answer.append(_idx)
    return answer