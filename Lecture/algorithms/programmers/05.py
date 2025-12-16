from collections import Counter


def solution(cipher, code):
    # [start: end(포함 안함): step]
    return cipher[code-1::code]


print(solution("dfjardstddetckdaccccdegk", 4))  # "attack"


def solution(my_string):
    # eval() 문자열 수식을 계산해주는 내장 함수
    answer = eval(my_string)
    return answer


print(solution("3 + 4"))


'''
    {
        a: 3
        b: 2
        c: 3
        d: 1
    }
'''


def solution(s):
    counts = Counter(s)
    result = [ch for ch in counts if counts[ch] == 1]
    # [d]

    return ''.join(sorted(result))


print(solution("abcabcadc"))  # "d"
print(solution("abdc"))  # "abcd"
print(solution("hello"))  # "eho"

# Stack lIFO


def solution(s):
    stack = 0
    for ch in s:
        if ch == '(':
            stack += 1
        else:  # ch == ')'
            if stack == 0:  # 닫는게 없는데 ')' 나오면 잘못되었다 판단
                return False
            stack -= 1

    return stack == 0  # 모두 짝이 맞아야 올바른 괄호


solution("()()")  # true
solution("(())()")  # true
solution(")()(")  # false
solution("(()(")  # false

print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
