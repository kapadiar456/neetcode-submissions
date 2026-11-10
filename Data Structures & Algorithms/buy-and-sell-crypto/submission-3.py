class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = len(prices)-1
        maxProfit = 0
        while l<r:
            buyPrice = min(prices[l:r])
            sellPrice = prices[r]
            profit = sellPrice-buyPrice
            maxProfit = max(profit, maxProfit)
            r-=1
        return maxProfit
