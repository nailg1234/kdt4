def solution(ingredient):
    # 1 빵
    # 2 야채
    # 3 고기
    # 빵 - 야채 - 고기 - 빵
    hamburger = [1, 2, 3, 1]
    ham_cnt = 0
    stack = []

    for ele in ingredient:
        stack.append(ele)
        if len(stack) > 3:
            if stack[-4:] == hamburger:
                ham_cnt += 1
                del stack[-4:]
    return ham_cnt


print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1])) # 2
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2])) # 0


# def solution(ingredient):
#     # 1 빵
#     # 2 야채
#     # 3 고기
#     # 빵 - 야채 - 고기 - 빵
#     hamburger = "1231"
#     in_l = "".join([str(i) for i in ingredient])
#     cnt = 0
#     print(in_l)
#     while in_l.find(hamburger) + 1:
#         cnt += 1
#         idx = in_l.find(hamburger)
#         in_l = in_l[:idx] + in_l[idx+4:]
#         print(in_l)
#     return cnt