def solution(mats, park):
    answer = -1
    for _row_idx, _row in enumerate(park):
        for _col_idx, _col in enumerate(_row):
            if _col == '-1':
                answer = max(answer, 1)
                col_cnt = 1
                row_cnt = 1
                for __col_idx in range(_col_idx + 1, len(park[0])):
                    if park[_row_idx][__col_idx] == '-1':
                        col_cnt += 1
                    else:
                        break
                for i in range(1, col_cnt):
                    if len(park) > _row_idx + i and park[_row_idx + i][_col_idx] == '-1':
                        row_cnt += 1
                    else:
                        break
                if col_cnt > 1 and row_cnt > 1:
                    n = min(col_cnt, row_cnt)
                    row_l = []
                    col_l = []
                    for _r_idx in range(1, n):
                        for _c_idx in range(1, n):
                            if park[_row_idx + _r_idx][_col_idx + _c_idx] != '-1':
                                row_l.append(_r_idx)
                                col_l.append(_c_idx)
                    if not row_l and not col_l:
                        answer = max(answer, n)
    low_l = []
    if answer in mats:
        return answer
    else:
        for mat in mats:
            if answer > mat:
                low_l.append(mat)
        if low_l:
            return max(low_l)
        else:
            return -1