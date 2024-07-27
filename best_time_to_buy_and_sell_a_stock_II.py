class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            buy = prices[i - 1]
            if buy < prices[i]:
                profit += prices[i] - buy
        return profit

solution = Solution()
print(solution.maxProfit([7,6,4,3,1]))