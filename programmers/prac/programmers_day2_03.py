# 분수의 덧셈

# 문제 설명
#   첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1,
#   두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다.
#   두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

# 제한사항
#   0 <numer1, denom1, numer2, denom2 < 1,000

def solution(numer1, denom1, numer2, denom2):

    num1 = numer1 * denom2 + numer2 * denom1
    num2 = denom1 * denom2
    n = 1
    while (num1 >= n) or (num2 >= n):
        if (num1 % n == 0) and (num2 % n == 0):
            num1 //= n
            num2 //= n
            n = 1
        n += 1

    return [num1, num2]
