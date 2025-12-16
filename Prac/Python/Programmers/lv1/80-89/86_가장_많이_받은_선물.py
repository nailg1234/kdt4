def solution(friends, gifts):
    rec_d = dict() # 받은 선물
    sen_d = dict() # 보낸 선물
    next_d = dict() # 다음달에 받을 선물
    for _f in friends:
        rec_d[_f] = dict()
        sen_d[_f] = dict()
        next_d[_f] = dict()
    for gift in gifts:
        sender, receiver = gift.split()
        rec_d[receiver][sender] = rec_d[receiver].get(sender, 0) + 1
        rec_d[receiver]['total'] = rec_d[receiver].get('total', 0) + 1
        sen_d[sender][receiver] = sen_d[sender].get(receiver, 0) + 1
        sen_d[sender]['total'] = sen_d[sender].get('total', 0) + 1
    # 선물을 주고 받은 기록이 있을 때 선물 횟수가 더 높은 사람이 1개
    # 선물을 주고 받은 기록이 하나도 없음 or 주고 받은 수가 같을 때는 선물지수가 높은사람
    for _f in friends:
        next_d[_f]['gift_point'] = sen_d[_f].get('total', 0) - rec_d[_f].get('total', 0)
    l = []
    for _sen_f in friends:
        for _rec_f in friends:
            if _rec_f == _sen_f or sorted([_rec_f, _sen_f]) in l:
                continue
            if sen_d[_sen_f].get(_rec_f, 0) > sen_d[_rec_f].get(_sen_f, 0):
                next_d[_sen_f]['gift'] = next_d[_sen_f].get('gift', 0) + 1
            elif sen_d[_sen_f].get(_rec_f, 0) < sen_d[_rec_f].get(_sen_f, 0):
                next_d[_rec_f]['gift'] = next_d[_rec_f].get('gift', 0) + 1
            elif sen_d[_sen_f].get(_rec_f, 0) == sen_d[_rec_f].get(_sen_f, 0):
                if next_d[_sen_f]['gift_point'] > next_d[_rec_f]['gift_point']:
                    next_d[_sen_f]['gift'] = next_d[_sen_f].get('gift', 0) + 1
                elif next_d[_sen_f]['gift_point'] < next_d[_rec_f]['gift_point']:
                    next_d[_rec_f]['gift'] = next_d[_rec_f].get('gift', 0) + 1
            l.append(sorted([_rec_f, _sen_f]))
    result = 0
    for key in next_d:
        result = max(next_d[key].get('gift', 0), result)
    return result