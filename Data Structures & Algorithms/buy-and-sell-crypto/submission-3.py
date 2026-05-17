class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        L = 0
        R = 1
        while R < len(prices):
            if prices[L] > prices[R]:
                L = R
            else:
                profit = prices[R] - prices[L]
                max_profit = max(max_profit, profit)
            R+=1
        return max_profit


        