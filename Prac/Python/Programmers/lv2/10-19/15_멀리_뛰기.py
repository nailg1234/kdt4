def solution(n):
    # DP 배열 생성 (0번 인덱스 부터 사용)
    dp = [0] * (n + 1)
    
    # 기본값 설정
    dp[0] = 1
    dp[1] = 1
    if n >= 2:
        dp[2] = 2
    
    # 피보나치 형태로 개선
    for i in range(3, n + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567 
    
    return dp[n]