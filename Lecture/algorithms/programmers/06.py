def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer += 1
    return answer


print(solution([149, 180, 192, 170], 167))  # 3)
print(solution([180, 120, 140],	190))  # 0)


def solution(quiz):

    return ['O'if eval(s.split("=")[0]) == eval(s.split("=")[1]) else 'X' for s in quiz]


print(solution(["3 - 4 = -3", "5 + 6 = 11"]))  # ["X", "O"])
print(solution(["19 - 6 = 13", "5 + 66 = 71",
                "5 - 15 = 63", "3 - 1 = 2"]))  # [	["O", "O", "X", "O"]]


def solution(str1, str2):
    if str2 in str1:
        return 1
    else:
        return 2


print(solution("ab6CDE443fgh22iJKlmn1o",	"6CD"))  # 1)
print(solution("ppprrrogrammers",	"pppp"))  # 2)
print(solution("AbcAbcA",	"AAA"))  # 2)
