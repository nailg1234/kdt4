def solution(s):
    l = list(s)
    ll = []
    while l :
        pop_value = l.pop()
        if ll :
            if ll[-1] == pop_value:
                del ll[-1]
            else:
                ll.append(pop_value)
        else:
            ll.append(pop_value)
    return 0 if ll else 1