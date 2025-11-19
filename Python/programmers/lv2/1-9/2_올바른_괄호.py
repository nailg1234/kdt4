def solution(s):
    if s[-1] == '(': # s 가 '(' 로 끝나면 return False
        return False
    else:
        close_stack_list = [] # ')' 쌓을 스택
        s_list = list(s)
        while len(s_list):
            pop_value = s_list.pop()
            if pop_value == ')': # ')'
                close_stack_list.append(pop_value) # ')' close_stack.push()
            else: # '('
                if len(close_stack_list): # close_stack에 요소 있는 경우
                    close_stack_list.pop() # ')' close_stack.pop()
                else:
                    return False # close_stack에 요소가 없는 경우 짝이 맞지 않으므로 return False
        else:
            if len(close_stack_list):
                return False
    return True