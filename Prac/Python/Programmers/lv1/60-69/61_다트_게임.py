def solution(dartResult):
    d = {'*':'@', 'S':'**1', 'D':'**2', 'T':'**3', '#':'*(-1)'}
    arr = []
    arr2 = []
    tmp_str = ''
    for _s in dartResult:
        if _s.isdecimal():
            if tmp_str:
                if tmp_str.isdecimal():
                    tmp_str += _s
                else:
                    arr.append(tmp_str)
                    tmp_str = _s
            else:
                tmp_str = _s
        else:
            tmp_str += _s
    else:
        arr.append(tmp_str)
    for i in range(len(arr)):
        for key in d:
            arr[i] = arr[i].replace(key, d[key])
        if '@' in arr[i]:
            if i > 0:
                arr2[i-1] = arr2[i-1] + '*2'
            arr[i] = arr[i].replace('@', '*2')
        arr2.append(arr[i])
    return (sum([eval(i) for i in arr2]))

print(solution('1S2D*3T')) # 37
print(solution('1D2S#10S')) # 9
print(solution('1D2S0T')) # 3
print(solution('1S*2T*3S')) # 23
print(solution('1D#2S*3S')) # # 5
print(solution('1T2D3D#')) # -4
print(solution('1D2S3T*')) # 59