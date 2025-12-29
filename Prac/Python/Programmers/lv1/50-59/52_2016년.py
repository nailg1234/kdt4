from datetime import date
def solution(a, b):
    s_l = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    d = date(2016, a, b)
    return s_l[d.weekday()]