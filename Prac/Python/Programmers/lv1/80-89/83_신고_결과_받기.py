def solution(id_list, report, k):
    d = dict()
    stop_l = []
    for _id in id_list:
        d[_id] = set()
    for _r in report:
        user_id, report_id = _r.split()
        d[report_id].add(user_id)
    for _id in id_list:
        if len(d[_id]) >= k:
            stop_l.append(_id)
    d2 = dict()
    for _id in id_list:
        for stop_id in stop_l:
            if _id in d[stop_id]:
                d2[_id] = d2.get(_id, 0) + 1
    result = []        
    for _id in id_list:
        result.append(d2.get(_id, 0))
    return result