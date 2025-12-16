def solution(numbers, hand):
    answer = ''
    left_num = [1, 4, 7, '*']
    center_num = [2, 5, 8, 0]
    right_num = [3, 6, 9, '#']
    
    arr = [left_num, center_num, right_num]
    
    # 0:left, 1:center, 2:right
    left_point = [0, 3]
    right_point = [2, 3]
    number_point = [0, 0]
    
    for number in numbers:
        for idx, l in enumerate(arr):
            if number in l:
                number_point = [idx, l.index(number)]
                break
                
        if number in left_num :
            left_point = number_point
            answer += 'L'
        elif number in right_num :
            right_point = number_point
            answer += 'R'
        else :
            a, b = number_point[0], number_point[1]
            _left = abs(left_point[0] - a) + abs(left_point[1] - b)
            _right = abs(right_point[0] - a) + abs(right_point[1] - b)
            
            if _left > _right :
                right_point = number_point
                answer += 'R'
            elif _left < _right :
                left_point = number_point
                answer += 'L'
            else:
                if hand == 'right':
                    right_point = number_point
                    answer += 'R'
                else:
                    left_point = number_point
                    answer += 'L'
    return answer