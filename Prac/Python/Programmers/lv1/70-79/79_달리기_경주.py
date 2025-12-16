def solution(players, callings):
    d = dict()
    for _idx, _p in enumerate(players):
        if _idx:
            if _idx == len(players)-1:
                d[_p] = [_idx, players[_idx-1], '']
            else:
                d[_p] = [_idx, players[_idx-1], players[_idx+1]]
        else:
            d[_p] = [_idx, '', players[_idx+1]]
    for calling in callings:
        key1 = d[calling][1] # 직전
        key2 = calling # 호명        
        key3 = d[key1][1] # 맨앞 error 없으면 1등
        key4 = d[key2][2] # 맨뒤 없으면 꼴등
        value1 = d[key1] # 직전
        value2 = d[key2] # 호명
        value1[0], value2[0] = value2[0], value1[0] # 인덱스 변경
        value2[1] = value1[1] if key3 else '' # 현재 이전
        value1[2] = value2[2] if key4 else '' # 직전 다음
        value1[1] = key2 # 직전 이전
        value2[2] = key1 # 현재 다음
        if key3:
            d[key3][2] = key2
        if key4:
            d[key4][1] = key1
    l = list(d.items())
    l = sorted(l, key=lambda x:x[1])
    return list(map(lambda x:x[0], l))