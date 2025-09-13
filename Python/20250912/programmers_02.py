# 프로그래머스 - 최빈값 구하기
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


solution([1, 1, 2, 2, 3, 4, 5])
