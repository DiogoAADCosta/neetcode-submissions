class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest_price = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            lowest_price = min(lowest_price, prices[i])
            profit = prices[i] - lowest_price
            max_profit = max(max_profit, profit)
        return max_profit if max_profit > 0 else 0
