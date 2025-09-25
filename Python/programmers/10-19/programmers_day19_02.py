# 잘라서 배열로 저장하기

# 문제 설명
#   문자열 my_str과 n이 매개변수로 주어질 때, my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요.

# 제한사항
#   1 ≤ my_str의 길이 ≤ 100
#   1 ≤ n ≤ my_str의 길이
#   my_str은 알파벳 소문자, 대문자, 숫자로 이루어져 있습니다.

def solution(my_str, n):
    return [my_str[i : i + n] for i in range(0, len(my_str), n)]