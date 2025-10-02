def solution(arr, divisor):
    l = sorted([ele for ele in arr if not ele % divisor])
    return l if l else [-1]