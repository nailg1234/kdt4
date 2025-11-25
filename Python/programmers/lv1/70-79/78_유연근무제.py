def solution(schedules, timelogs, startday):
    cnt = 0
    for s in zip(schedules, timelogs):
        s_hour = s[0] // 100
        s_min = s[0] % 100 
        s_limit = s_hour * 60 + s_min + 10
        day = startday
        is_p = True
        for time in s[1]:
            if day in [1, 2, 3, 4, 5]:
                t_hour = time // 100
                t_min = time % 100
                if s_limit < t_hour * 60 + t_min:
                    is_p = False
                    break
            if day == 7:
                day = 1
            else:
                day += 1
        if is_p :
            cnt += 1 
    return cnt