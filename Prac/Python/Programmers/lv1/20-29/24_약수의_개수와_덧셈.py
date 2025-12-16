def solution(left, right):
    div_list = []
    i_list = []
    sum_list = []
    for i in range(left, right + 1):
        j, cnt = 1, 1
        i_list.append(i)
        while(j < i):
            if not i % j:
                cnt += 1
            j += 1
        else:
            div_list.append(cnt)
    else:
        for idx, ele in enumerate(div_list):
            sum_list.append(-i_list[idx]) if ele % 2 else sum_list.append(i_list[idx])
        
    return sum(sum_list)