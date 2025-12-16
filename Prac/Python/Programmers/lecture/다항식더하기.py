# 다항식 더하기

# 문제 설명
# 한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다.
# 다항식을 계산할 때는 동류항끼리 계산해 정리합니다.
# 덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때,
# 동류항끼리 더한 결괏값을 문자열로 return 하도록 solution 함수를 완성해보세요.
# 같은 식이라면 가장 짧은 수식을 return 합니다.

def solution(polynomial):
    terms = polynomial.split(" + ")  # [3x, 7, x]
    x_sum = 0  # x개수
    const_sum = 0  # 숫자

    for term in terms:
        if 'x' in term:
            x_num = term.replace('x', '')
            x_sum += int(x_num) if x_num else 1
        else:
            const_sum += int(term)
    answer = []
    if x_sum:
        answer.append(f'{x_sum}x' if x_sum > 1 else 'x')

    if const_sum:
        answer.append(str(const_sum))

    return " + ".join(answer)


print(solution("3x + 7 + x"))
print(solution("x + x + x"))
