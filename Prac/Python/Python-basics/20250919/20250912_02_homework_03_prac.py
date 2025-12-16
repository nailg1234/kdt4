# 문제3. 1부터 n까지의 합
def sum_to_n(n):
    """
    예 : sum_to_n(5) 1 + 2 + 3 + 4 + 5 = 15
    """
    if n == 1:
        return 1

    return n + sum_to_n(n-1)


print(sum_to_n(5))

# 문제5. 문자열 뒤집기
'''
    "hello" -> "olleh"
'''

def reverse_string(s):
    if not s :
        return ''
    
    return s[-1] + reverse_string(s[:-1])

print(reverse_string("hello"))