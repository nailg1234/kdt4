def solution(keymap, targets):
    result = []
    for target in targets:
        cnt = 0
        for _t in target:
            key_min = -1
            for key in keymap:
                if _t in key:
                    if key_min > -1:
                        key_min = min(key_min, key.index(_t) + 1)
                    else:
                        key_min = key.index(_t) + 1
            if key_min > -1:
                cnt += key_min
            else:
                result.append(-1)
                break
        else:
            result.append(cnt)
    return result

print(solution(["ABACD", "BCEFD"], ["ABCD","AABB"])) # [9, 4]
print(solution(["AA"], ["B"]))	# [-1]
print(solution(["AGZ", "BSSS"], ["ASA","BGZ"]))	# [4, 6]
print(solution(["AAA",'ZZZ'], ["SASS",'SDFA']))	# [-1]