def fibonacci(n, memo):
    if n <= 1:
        return n
    
    if memo[n] != -1:
        return memo[n]
    
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    
    return memo[n]

n = 10
memo = [-1] * (n + 1)
print(fibonacci(n, memo))  # 결과: 55