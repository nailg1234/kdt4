def solution(n):
    s = ''
    while (n // 3 or n % 3):
        s += str(n % 3)
        n //= 3
    s = s[::-1]
    sum = 0
    mul3 = 0
    for i in range(len(s)):
        sum += int(s[i]) * 3 ** mul3
        mul3 += 1
    return sum

print(solution(45)) # 7
print(solution(125)) # 229