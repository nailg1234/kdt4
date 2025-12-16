# 안전지대

# 문제 설명
# 다음 그림과 같이 지뢰가 있는 지역과 지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.

# 지뢰는 2차원 배열 board에 1로 표시되어 있고 board에는 지뢰가 매설 된 지역 1과, 지뢰가 없는 지역 0만 존재합니다.
# 지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때, 안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.

def solution(board):
    
    danger_list = []
    i_list = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, +1], [1, -1], [1, 0], [1, 1]]
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]:
                danger_list.append([i, j])
                
    for [w1, h1] in danger_list:
        for [w2, h2] in i_list:
            if 0 <= w1 + w2 < len(board) and 0 <= h1 + h2 < len(board):
                if board[w1+w2][h1+h2] != 1:
                    board[w1+w2][h1+h2] = 1

    return [x for sub_list in board for x in sub_list].count(0)

print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))