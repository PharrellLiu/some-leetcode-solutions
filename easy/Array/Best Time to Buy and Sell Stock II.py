from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        hold = 0
        buyingPrice = 0
        i = 1
        length = len(prices)
        while i < length:
            if prices[i] < prices[i - 1] and hold == 1:
                hold = 0
                profit += prices[i - 1] - buyingPrice
            elif prices[i] > prices[i - 1] and hold == 0:
                hold = 1
                buyingPrice = prices[i - 1]
            i += 1
        if hold == 1:
            profit += prices[-1] - buyingPrice
        return profit
