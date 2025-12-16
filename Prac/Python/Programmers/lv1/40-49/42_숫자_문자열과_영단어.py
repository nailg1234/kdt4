def solution(s):
    s = s.replace('zero', '0').replace('one', '1').replace('two', '2').replace('three', '3')
    s = s.replace('four', '4').replace('five', '5').replace('six', '6').replace('seven', '7')
    s = s.replace('eight', '8').replace('nine', '9')
    return int(s)
print(solution("one4seveneight")) # 1478
print(solution("23four5six7")) # 234567
print(solution("2three45sixseven")) # 234567
print(solution("123")) # 123