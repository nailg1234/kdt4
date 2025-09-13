# 분수의 덧셈

# 문제 설명
#   첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1,
#   두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다.
#   두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

# 제한사항
#   0 <numer1, denom1, numer2, denom2 < 1,000

def solution(numer1, denom1, numer2, denom2):
    # 분모 맞추고 덧셈 계산
    num1 = numer1 * denom2
    num2 = numer2 * denom1

    num3 = num1 + num2
    num4 = denom1 * denom2

    # 기약분수 만들기
    n = 1
    while True:
        if (num3 < n) or (num4 < n):
            break

        if (num3 % n == 0) and (num4 % n == 0):
            num3 //= n
            num4 //= n
            n = 1

        n += 1

    answer = [num3, num4]
    return answer
