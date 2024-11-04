def fibonacci(n, memo):
    # 기본 조건: n이 0 또는 1인 경우, 피보나치 수는 n 그 자체
    if n <= 1:
        return n
    
    # 메모 배열을 확인: 이미 계산된 값이 있다면, 메모된 값을 반환하여 재귀 호출을 피함
    if memo[n] != -1:
        return memo[n]
    
    # 계산되지 않은 경우: 재귀 호출을 통해 n-1과 n-2 피보나치 값을 계산하고, 결과를 메모 배열에 저장
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    
    # 최종적으로 계산된 피보나치 값을 반환
    return memo[n]


n = 10

# 메모 배열을 -1로 초기화하여 아직 계산되지 않은 값들을 표시. 크기는 n+1로 설정
memo = [-1] * (n + 1)

print(fibonacci(n, memo))  # 결과: 55
