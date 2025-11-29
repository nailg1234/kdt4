def solution(n, w, num):
    l, l2 = [], []
    idx_row, idx_col = -1, -1
    state = True
    for i in range(1, n + 1):
        if i == num:
            idx_row = len(l)
        if state:
            l2.append(i)
        else:
            l2.insert(0, i)
        if len(l2) == w or n == i:
            if len(l2) != w:
                while len(l2) < w:
                    if state:
                        l2.append(0)
                    else:
                        l2.insert(0, 0)
            l.append(l2)
            l2 = []
            state = not state
    idx_col = l[idx_row].index(num)
    result = 0
    for _row in l[::-1]:
        if _row[idx_col]:
            result += 1
            if _row[idx_col] == num:
                break
    return result