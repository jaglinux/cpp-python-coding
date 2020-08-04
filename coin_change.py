def coin(coins, target):
    if coins[0] != 0:
        coins.insert(0, 0)
    dp= [[0 for _ in range(target+1)] for _ in range(len(coins))]
    dp[0][0] = 1

    for i in range(len(coins)):
        for j in range(target+1):
            if i == 0:
                pass
            else:
                if coins[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]

    print(dp)
    return dp[-1][-1]

ways = coin([1,5,10], 8)
print(ways)
