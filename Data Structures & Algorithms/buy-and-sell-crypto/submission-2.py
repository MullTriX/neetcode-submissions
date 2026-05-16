class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        win = 0 
        for i, minimum in enumerate(prices):
            for j, maximum in enumerate(prices):
                diff = maximum - minimum
                if j > i and diff > win:
                    win = diff
        return win


        