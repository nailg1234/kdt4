import math


def solution(chicken):
    # (주문한 치킨 수 - 1) // (필요한 쿠폰 수 - 1)
    # 9 마리를 사면 1마리가 서비스랑 같다.
    answer = max((chicken, 1) - 1) // 9
    # 9로 나누어 떨어지는 경우 마지막에 쿠폰 1장이
    # 교환이 안되는 부분을 보정
    return answer


solution(0)


def solution(chicken):
    service = 0  # 서비스 치킨 수
    coupons = chicken  # 처음 받은 쿠폰 수

    while coupons >= 10:  # 10장 이상이면 교환
        new_service = coupons // 10
        service += new_service
        coupons = new_service + (coupons % 10)

    return service


print(solution(100))  # 11
print(solution(1081))  # 120


def solution(a, b):
    gcd = math.gcd(a, b)
    b //= gcd

    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5

    if b == 1:
        return 1
    else:
        return 2


print(solution(7, 20))  # 1
print(solution(11,	22))  # 1
print(solution(12,	21))  # 2


def solution(bin1, bin2):
    # 2진수 -> 10진수
    # N -> 10진수 : INT(문자열, N진수)'
    bin_int1 = int(bin1, 2)
    bin_int2 = int(bin2, 2)

    # 10진수 -> 2진수
    # 10진수 ->  2, 8, 16진수 : bin(), oct(), hex()

    # 2진수 1 - 10 - 11 - 100
    # 8진수 7 - 10 - 11 - 17 - 20 ... 77 - 100
    # 16진수 9 - A - B - C - D - E - F - 10
    return bin(bin_int1 + bin_int2)[2:0]


print(solution("10", "11"))  # "101"


def solution(babbling):
    s_list = ["aya", "ye", "woo", "ma"]
    cnt = 0
    for ba in babbling:
        _ba = ba
        for s in s_list:
            if s in _ba:
                _ba = _ba.replace(s, '*')
        else:
            if len(_ba) == _ba.count('*'):
                cnt += 1

    return cnt


print(solution(["aya", "yee", "u", "maa", "wyeoo"]))  # 1
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))  # 3
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
