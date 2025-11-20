def solution(n):
    n_one_count = bin(n)[2:].count('1')
    i = 1
    while True:
        if n_one_count == bin(n + i)[2:].count('1'):
            break
        i += 1
    return n + i