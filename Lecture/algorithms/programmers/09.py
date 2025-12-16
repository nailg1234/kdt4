def solution(n):
    '''
        정수를 -> 문자열
        문자열 -> 리스트
        리스트를 정렬 -> 내림차순으로 정렬 -> 반환값 리스트

        리스트 -> 문자열
        문자열 -> 정수
    '''
    new_str = str(n)
    new_list = list(new_str)
    sorted_list = sorted(new_list, reverse=True)

    answer_str = ''.join(sorted_list)
    answer = int(answer_str)

    return answer


solution(118372)
