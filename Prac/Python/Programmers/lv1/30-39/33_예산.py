def solution(d, budget):
    answer = len(d)
    sorted_list = sorted(d)
    for i in range(1, len(sorted_list) + 1):
        if sum(sorted_list[:i]) > budget:
            return i-1
        
    return answer