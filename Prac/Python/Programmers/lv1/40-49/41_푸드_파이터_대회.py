def solution(food):
    tmp_str = "".join([str(i) * (food[i]//2) for i in range(1, len(food))])
    return tmp_str + '0' + tmp_str[::-1]
print(solution([1, 3, 4, 6])) # "1223330333221"
print(solution([1, 7, 1, 2])) # "111303111"