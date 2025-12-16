def solution(survey, choices):
    d = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for _idx, _survey in enumerate(survey):
        score = 4 - choices[_idx]
        if score > 0:
            d[_survey[0]] = d.get(_survey[0]) + abs(score)
        elif score < 0:
            d[_survey[1]] = d.get(_survey[1]) + abs(score)
    s = ''
    arr = []
    for key, value in d.items():
        arr.append([key, value])
        if len(arr) == 2:
            s += sorted(arr, key=lambda x:(-x[1],x[0]))[0][0]
            arr = []
    return s