from collections import Counter

def solution(k, tangerine):
    # 귤 크기별 개수를 센다
    counter = Counter(tangerine)

    # 귤 갯수를 큰 순서대로
    counter = sorted(counter.values(), reverse=True)

    total = 0 # 지금까지 담은 귤 갯수
    kinds = 0 # 선택된 귤 종류 수

    for c in counter:
        total += c # 해당 크기 귤을 모두 담기
        kinds += 1 # 크기 종류 +1

        if total >= k: # 원하는 만큼의 k개 이상 담았다면 끝
            break

    return kinds

