import math
def solution(number, limit, power):
    result = []
    for i in range(1, number + 1):
        s = set()
        for j in range(1, int(math.sqrt(i)) + 1):
            if i % j == 0:
                s.add(j)
                s.add(i // j)
        result.append(power if len(s) > limit else len(s))
    return sum(result)