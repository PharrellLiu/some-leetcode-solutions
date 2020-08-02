from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        profit = 0
        i = 1
        len_prices = len(prices)
        while i < len_prices:
            profit += prices[i] - prices[i - 1]
            if profit < 0:
                profit = 0
            max_profit = max(max_profit, profit)
            i += 1
        return max_profit
