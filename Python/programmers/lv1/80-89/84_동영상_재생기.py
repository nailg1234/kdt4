def solution(video_len, pos, op_start, op_end, commands):
    def timeToInt(_time):
        minute, sec = _time.split(':')
        return  int(minute) * 60 + int(sec)
    def intToTime(_int):
        minute, sec = _int // 60, _int % 60
        return str(minute).zfill(2)  + ':' + str(sec).zfill(2)
    def doCommand(_c, i_pos):
        if _c == 'next':
            i_pos += 10
        elif _c == 'prev':
            i_pos -= 10
        if i_pos < 10:
            i_pos = 0
        if i_video_end < i_pos:
            i_pos = i_video_end
        if i_op_start <= i_pos <= i_op_end:
            i_pos = i_op_end
        return i_pos
    i_video_end = timeToInt(video_len)
    i_pos = timeToInt(pos)
    i_op_start = timeToInt(op_start)
    i_op_end = timeToInt(op_end)
    i_pos = doCommand('', i_pos)
    for _c in commands:
        i_pos = doCommand(_c, i_pos)
    return intToTime(i_pos)