def solution(park, routes):
    row_max_idx = len(park) - 1
    col_max_idx = len(park[0]) - 1
    s_loc = [] # s row, col
    x_loc = [] # x row, col
    for _row_idx, _row in enumerate(park):
        for _col_idx, _col in enumerate(_row):
            if _col == 'S':
                s_loc.extend([_row_idx, _col_idx])
            elif _col == 'X':
                x_loc.append([_row_idx, _col_idx])
    for _r in routes:
        l = _r.split()
        op, move = l[0], int(l[1])
        idx = 0
        if op == 'N': # 위쪽
            for _m in range(1, move + 1):
                idx = s_loc[0] - _m
                if idx < 0:
                    break
                if [idx, s_loc[1]] in x_loc:
                    break
            else:
                s_loc = [idx, s_loc[1]]
        elif op == 'S': # 아래쪽
            for _m in range(1, move + 1):
                idx = s_loc[0] + _m
                if idx > row_max_idx:
                    break
                if [idx, s_loc[1]] in x_loc:
                    break
            else:
                s_loc = [idx, s_loc[1]]
        elif op == 'W': # 왼쪽
            for _m in range(1, move + 1):
                idx = s_loc[1] - _m
                if idx < 0:
                    break
                if [s_loc[0], idx] in x_loc:
                    break
            else:
                s_loc = [s_loc[0], idx]
        elif op == 'E': # 오른쪽
            for _m in range(1, move + 1):
                idx = s_loc[1] + _m
                if idx > col_max_idx:
                    break
                if [s_loc[0], idx] in x_loc:
                    break
            else:
                s_loc = [s_loc[0], idx]
    return s_loc