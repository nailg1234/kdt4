# 평행

# 문제 설명
    # 점 네 개의 좌표를 담은 이차원 배열  dots가 다음과 같이 매개변수로 주어집니다.

# [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
# 주어진 네 개의 점을 두 개씩 이었을 때, 두 직선이 평행이 되는 경우가 있으면 1을 없으면 0을 return 하도록 solution 함수를 완성해보세요.

# 제한사항
    # dots의 길이 = 4
    # dots의 원소는 [x, y] 형태이며 x, y는 정수입니다.
    # 0 ≤ x, y ≤ 100
    # 서로 다른 두개 이상의 점이 겹치는 경우는 없습니다.
    # 두 직선이 겹치는 경우(일치하는 경우)에도 1을 return 해주세요.
    # 임의의 두 점을 이은 직선이 x축 또는 y축과 평행한 경우는 주어지지 않습니다.

def solution(dots):
    dots_list = []
    calc_list = []
    for coord1 in dots:
        dots_list.append(coord1)
        for coord2 in dots:
             if not coord2 in dots_list:
                _x = coord1[0] - coord2[0]
                _y = coord1[1] - coord2[1]
                calc_list.append([_x, _y])
    
    for calc_coord in calc_list :
        if calc_list.count(calc_coord) == 2:
            return 1
    
    calc_list2 = [x/y for [x, y] in calc_list]
    
    for calc in calc_list2 :
        if calc_list2.count(calc) == 2:
            return 1

    return 0

print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))	#1
print(solution([[3, 5], [4, 1], [2, 4], [5, 10]]))	#0
print(solution([[1, 1], [2, 2], [3, 3], [5, 5]]))	#1
