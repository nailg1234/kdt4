def solution(s, n):
    answer = ''
    for ch in s:
        if ch.isupper():  # 대문자 처리
            answer += chr(((ord(ch) - ord('A')) + n) % 26 + ord('A'))
        elif ch.islower():  # 소문자 처리
            answer += chr(((ord(ch) - ord('a')) + n) % 26 + ord('a'))
        else:  # 공백
            answer += ch

    return answer
