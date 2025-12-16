def solution(people, limit):
    # 몸무게를 오름 차순으로 정렬
    people.sort()
    
    # [50, 50, 70, 80]

    # 가장 가벼운 사람 위치
    left = 0

    # 가장 무거운 사람 위치
    right = len(people) - 1

    # 필요한 보트의 수
    boats = 0

    while left <= right:
        # 가장 가벼운 사람 + 가장 무거운 사람 같이 탈 수 있으면 태움
        if people[left] + people[right] <= limit:
            left += 1
        
        # 무거운 사람은 무조건 탑승
        right -= 1

        # 보트 1대 사용
        boats += 1

    return boats