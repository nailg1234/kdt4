def safe_get(lst, index, default=None):
    """
    리스트에서 안전하게 값 가져오기
    - lst: 리스트
    - index: 인덱스
    - default: 기본값
    """
    # 여기에 코드 작성

    if len(lst) > index:
        return lst[index]
    else:
        return default


        # 테스트
numbers = [10, 20, 30]
print(safe_get(numbers, 1))      # 20
print(safe_get(numbers, 10))     # None
print(safe_get(numbers, 10, -1))  # -1
