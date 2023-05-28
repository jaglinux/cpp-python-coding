def knapSack(W, weight, profit, n):
    def rec(index, w):
        print(index, w)
        if index == n:
            return 0
        result1 = 0 + rec(index+1, w)
        result2 = 0
        if w - weight[index] >= 0:
            result2 = profit[index] + rec(index+1, w-weight[index])
        return max(result1, result2)
    return rec(0, W)

if __name__ == '__main__':
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    W = 50
    n = len(profit)
    print(knapSack(W, weight, profit, n))
