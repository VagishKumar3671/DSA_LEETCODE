class Solution(object):
    def maxProfit(self, prices):
        # Edge case: only one price, can't sell
        if len(prices) == 1:
            return 0
        
        # If prices are non-decreasing, profit is max - min
        if sorted(prices) == prices:
            return prices[-1] - prices[0]
        
        max_sum = 0
        mins = prices[0]
        
        # Iterate through prices to find best buy/sell
        for i in range(1, len(prices)):
            temp = prices[i] - mins
            max_sum = max(temp, max_sum)
            mins = min(mins, prices[i])
        
        return max_sum
