def solution(absolutes, signs):
    return sum([i if signs[idx] else -i for idx, i in enumerate(absolutes)])