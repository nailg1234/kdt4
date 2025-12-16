def solution(X, Y):
    s = set(X) & set(Y)
    
    x_dic = {}
    for x in X:
        x_dic[x] = x_dic.get(x, 0) + 1

    y_dic = {}
    for y in Y:
        y_dic[y] = y_dic.get(y, 0) + 1

    stack = []
    
    for _s in s:
        for i in range(min(y_dic[_s], x_dic[_s])):
            stack.append(_s)

    stack.sort(reverse=True)

    if set(stack) == {'0'}:
        return '0'
    elif stack :
        return ''.join(stack)
    else:
        return '-1'
        
print(solution("100", "2345")) # "-1"
print(solution("100", "203045")) # "0"
print(solution("100", "123450")) # "10"
print(solution("12321", "42531")) # "321"
print(solution("5525", "1255"))	# "552"