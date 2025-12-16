def solution(my_string, n):
    # 각 문자를 담을 빈 리스트 선언
    list_str = []

    # 리스트에 my_string만큼 돌면서, 각 요소를 n번씩 반복해서 저장해라
    list_str = [(i * n) for i in my_string]

    # 각 요소를 띄어쓰기 없이 조인해서 answer에 반환
    answer = ''.join(list_str)

    return answer


solution("hello", 3)
