import math
def solution(n):
    return (math.sqrt(n) + 1) ** 2 if math.sqrt(n) == int(math.sqrt(n)) else -1