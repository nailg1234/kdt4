def solution(arr):
    
    arr.reverse() 
    stack_list = []
    stack_list.append(arr.pop()) # stack_list 초기 값
    
    while len(arr):
        pop_value = arr.pop() # 뒤집은 배열 pop()
        if stack_list[-1] == pop_value: #stack_list의 peek과 arr.pop()이 같으면 push() 생략
            continue
            
        stack_list.append(pop_value) #stack_list.push()
    
    return stack_list