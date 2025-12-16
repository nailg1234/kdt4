# 직사각형 넓이 구하기

# 문제 설명
#     2차원 좌표 평면에 변이 축과 평행한 직사각형이 있습니다.
#     직사각형 네 꼭짓점의 좌표
#     [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]가 담겨있는
#     배열 dots가 매개변수로 주어질 때,
#     직사각형의 넓이를 return 하도록 solution 함수를 완성해보세요.

# 제한사항
#     dots의 길이 = 4
#     dots의 원소의 길이 = 2
#     -256 < dots[i]의 원소 < 256
#     잘못된 입력은 주어지지 않습니다.


def solution(dots):
    
    list_x = [x for [x, y] in dots]
    x_min = min(list_x)
    x_max = max(list_x)

    list_y = [y for [x, y] in dots]
    y_min = min(list_y)
    y_max = max(list_y)
    
    return (x_max - x_min) * (y_max - y_min)