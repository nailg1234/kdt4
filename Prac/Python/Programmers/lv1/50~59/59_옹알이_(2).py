def solution(babbling):
    b_word_l = ["aya", "ye", "woo", "ma"]
    word_l = ['!', '@', '#', '$']
    cnt = 0
    for ba in babbling:
        _ba = ba
        for idx, b_word in enumerate(b_word_l):
            _ba = _ba.replace(b_word, word_l[idx])
        if not any([s.isalpha() for s in _ba]) and not any([s*2 in _ba for s in word_l]):
            cnt += 1
    return cnt
print(solution(["aya", "yee", "u", "maa"])) # 1
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"])) # 2