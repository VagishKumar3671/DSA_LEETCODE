class Solution(object):
    def maxProfit(self, prices):
        if len(prices) == 1:
            return 0
        if sorted(prices) == prices:
            return prices[-1] - prices[0]
        if sorted(prices, reverse=True) == prices:
            return 0
        max_sum = 0
        mins = prices[0]
        for i in range(1, len(prices)):
            max_sum = max(prices[i] - mins, max_sum)
            mins = min(mins, prices[i])
            
        return max_sum
