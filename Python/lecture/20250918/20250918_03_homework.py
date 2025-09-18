# *args 사용 연습
# 문제 1. 숫자 여러 개의 평균 구하기
# 숫자를 몇 개든 받을 수 있는 average() 함수를 만들어보세요.
def average(*args):
    return sum(args)/len(args)


print(average(1, 2, 3, 4))

# 문제 2. 가장 긴 문자열 찾기(max 함수에 대해 찾아보고 풀기)
# 여러 개의 문자열을 받아, 가장 긴 문자열을 반환하는 함수를 만들어보세요


def find_max_len(*args):

    len_list = [len(_s) for _s in args]

    return args[len_list.index(max(len_list))]


print(find_max_len('231', '7533', '65367', '1575678678'))
