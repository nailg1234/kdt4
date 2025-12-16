def solution(data, ext, val_ext, sort_by):
    data_col = ['code', 'date', 'maximum', 'remain']
    data_col_idx = data_col.index(ext)
    sort_by_idx = data_col.index(sort_by)
    return sorted(list(filter(lambda x:x[data_col_idx] < val_ext, data)), key = lambda x:x[sort_by_idx])
print(solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], 'date', 20300501,'remain'))