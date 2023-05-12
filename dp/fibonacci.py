dp= {}

def main(n):
    if n in dp:
        return dp[n]
    if n <= 1:
        return n
    print(n, n-1, n-2)
    dp[n] = main(n-1) + main(n-2)
    return dp[n]

print(main(4))

## With DP
# 4 3 2
# 3 2 1
# 2 1 0
# 3

## Without DP
# 4 3 2
# 3 2 1
# 2 1 0
# 2 1 0
# 3
