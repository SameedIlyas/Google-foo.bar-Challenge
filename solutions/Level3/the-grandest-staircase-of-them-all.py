def solution(n):
    # Initialize a list to store the count of ways for each number of steps
    dp = [0] * (n + 1)

    # There is one way to get a sum of 0, which is an empty list
    dp[0] = 1
    
    # Iterate through all possible numbers to form the sum
    for num in range(1, n):
        for current_sum in range(n, num - 1, -1):
            dp[current_sum] += dp[current_sum - num]
    
    return dp[n]
