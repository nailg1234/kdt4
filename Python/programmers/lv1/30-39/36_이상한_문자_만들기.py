def solution(s):
    s_list = []
    for word in s.split(" "):
        _ss = ''
        for idx, _s in enumerate(word):
            if idx % 2:
                _ss += _s.lower()
            else:
                _ss += _s.upper()
        else:
            s_list.append(_ss)
    
    return " ".join(s_list)