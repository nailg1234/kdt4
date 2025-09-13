# 프로그래머스 - 최빈값 구하기
def solution(array):
    max_arr = []
    is_check = False

    # 파라미터 반복문
    for ele in array:

        print(max_arr)

        is_check = False  # max_arr에 넣었는지 체크
        max_arr_len = len(max_arr)  # 최대값 리스트 길이

        # 최대값 리스트에 값이 존재하면
        if max_arr_len:
            for ele2, cnt2 in max_arr:
                if ele == ele2:
                    is_check = True
                    break

        # 이미 체크 되있으면 지나가기
        if is_check:
            continue

        # 현재 ele 카운트
        cnt = array.count(ele)

        if max_arr_len:  # 최대값 리스트에 값 존재함
            if cnt > max_arr[0][1]:  # 최대값 리스트에 들어있는 요소 cnt보다 현재 ele cnt가 더 크다면
                max_arr.clear()
                max_arr.append([ele, cnt])
            elif cnt == max_arr[0][1]:  # 최대값 리스트에 들어있는 요소 cnt와 같다면
                max_arr.append([ele, cnt])
            else:
                pass
        else:
            max_arr.append([ele, cnt])

    if (len(max_arr) > 1):
        answer = -1
    else:
        answer = max_arr[0][0]

    return answer


print(solution([1, 1, 2, 2]))
