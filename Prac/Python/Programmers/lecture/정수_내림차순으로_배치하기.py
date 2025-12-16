# 정수 내림차순으로 배치하기

def solution(n):
    '''
        1. 정수를 -> 문자열
        2. 문자열 -> 리스트
        3. 리스트를 정렬 -> 내림차순으로 정렬 -> 반환값 리스트
        4. 리스트 -> 문자열
        5. 문자열 -> 정수
    '''
    new_list = sorted(list(str(n)), reverse=True)

    return int(''.join(new_list))


print(solution(118372))
