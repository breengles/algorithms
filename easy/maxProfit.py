from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        max_profit = 0

        while sell < len(prices):
            cur_profit = prices[sell] - prices[buy]
            if cur_profit < 0:
                buy = sell
                sell += 1
            else:
                if cur_profit > max_profit:
                    max_profit = cur_profit

                sell += 1

        return max_profit

