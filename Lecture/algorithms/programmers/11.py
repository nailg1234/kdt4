def solution(s, n):
    answer = ''
    for ch in s:
        if ch.isupper():  # 대문자 처리
            n1 = ((ord(ch) - ord('A')) + n) % 26
            answer += chr(n1 + ord('A'))
        elif ch.islower():  # 소문자 처리
            n2 = (ord(ch) - ord('a') + n) % 26
            answer += chr(n2 + ord('a'))
        else:  # 공백은 그대로
            answer += ch

    return answer


solution("AB", 1)
solution("z", 1)
solution("a B z", 4)
