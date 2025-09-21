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
    num_arr, num_cnt_arr = [], []

    for ele in array:  # 중복 제거 num_arr 생성
        if ele not in num_arr:
            num_arr.append(ele)

    for ele in num_arr:
        num_cnt_arr.append(array.count(ele))  # count 세기

    max_cnt = max(num_cnt_arr)  # count 최대 값 찾기

    if num_cnt_arr.count(max_cnt) >= 2:  # 최대 값 2개 이상 return -1
        answer = -1
    else:
        answer = num_arr[num_cnt_arr.index(max_cnt)]  # 최대 값 1개 return count

    return answer
