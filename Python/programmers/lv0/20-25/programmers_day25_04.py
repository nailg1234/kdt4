# 다음에 올 숫자

# 문제 설명
    # 등차수열 혹은 등비수열 common이 매개변수로 주어질 때,
    # 마지막 원소 다음으로 올 숫자를 return 하도록 solution 함수를 완성해보세요.

# 제한사항
    # 2 < common의 길이 < 1,000
    # -1,000 < common의 원소 < 2,000
    # common의 원소는 모두 정수입니다.
    # 등차수열 혹은 등비수열이 아닌 경우는 없습니다.
    # 등비수열인 경우 공비는 0이 아닌 정수입니다.

def solution(common):
    answer = 0
    if common[-2] - common[-3] == common[-1] - common[-2]:
        answer = common[-1] + common[-1] - common[-2]
    else:
        answer = common[-1] * (common[-1] // common[-2])

    return answer if common[-1] < 0 else answer

print(solution([1, 2, 3, 4]))
print(solution([2, 4, 8]))
