def solution(name, yearning, photo):
    result = []
    for peoples in photo:
        result.append(sum([yearning[name.index(p)] for p in list(set(peoples) & set(name))]))
    return result