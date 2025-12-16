def solution(board, moves):
    cnt = 0
    stack = []
    moves.reverse()
    while moves:
        pop_value = moves.pop()
        for row_idx in range(len(board)):
            doll = board[row_idx][pop_value-1]
            if doll :
                board[row_idx][pop_value-1] = 0
                stack.append(doll)
                break;
        while len(stack) > 1 and stack[-1] == stack[-2]:
            del stack[-2:]
            cnt += 2
    return cnt