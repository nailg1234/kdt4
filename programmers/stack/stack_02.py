# 올바른 괄호

# 문제 설명
#   괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어

# "()()" 또는 "(())()" 는 올바른 괄호입니다.
# ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
# '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

# 제한사항
#   문자열 s의 길이 : 100,000 이하의 자연수
#   문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.

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