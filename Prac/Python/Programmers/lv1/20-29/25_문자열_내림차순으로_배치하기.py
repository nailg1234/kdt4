def solution(s):
    lower_list = sorted([_s for _s in s if _s.islower()], reverse=True)
    upper_list = sorted([_s for _s in s if _s.isupper()], reverse=True)
    return "".join(lower_list) + "".join(upper_list)