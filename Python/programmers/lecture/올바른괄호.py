def solution(s):
    stack = 0
    for ch in s:
        if ch == '(':
            stack += 1
        else:  # ch == ')'
            if stack == 0:  # 닫는게 없는데 ')' 나오면
                return False
            stack -= 1

    return stack == 0


print(solution(')()())))))((()()()))'))
