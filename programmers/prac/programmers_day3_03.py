# 최빈값 구하기

# 문제 설명
#   최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다.
#   정수 배열 array가 매개변수로 주어질 때,
#   최빈값을 return 하도록 solution 함수를 완성해보세요.
#   최빈값이 여러 개면 -1을 return 합니다.

# 제한사항
#   0 < array의 길이 < 100
#   0 ≤ array의 원소 < 1000

def solution(array):

    set_list, set_list_cnt = [i for i in set(array)], [array.count(i) for i in set(array)]

    if set_list_cnt.count(max(set_list_cnt)) == 1:
        answer = set_list[set_list_cnt.index(max(set_list_cnt))]
    else:
        answer = -1

    return answer
