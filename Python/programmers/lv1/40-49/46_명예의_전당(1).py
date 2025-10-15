def solution(k, score):
    arr = []
    result = []
    for i in range(len(score)):
        if i < k:
            arr.append(score[i])
        else:
            if arr and min(arr) < score[i]:
                if len(arr) == k:
                    arr.pop()
                    arr.append(score[i])
        arr.sort(reverse=True)
        result.append(arr[-1])
    return result