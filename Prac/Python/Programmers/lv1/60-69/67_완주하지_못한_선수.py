def solution(participant, completion):
    cnt_dic = {}
    result = ''

    for p in participant:
        cnt_dic[p] = cnt_dic.get(p, 0) + 1

    for c in completion:
        cnt_dic[c] -= 1
    
    for key in cnt_dic.keys():
        if cnt_dic[key] > 0:
            result = key
            break
        
    return result

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"])) # "leo"
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])) # "vinko"
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])) # "mislav"