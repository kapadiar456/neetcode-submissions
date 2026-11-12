class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = len(prices)-1
        maxProfit = 0
        while l<r:
            buyPrice = prices[l]
            sellPrice = prices[r]
            profit = sellPrice-buyPrice
            maxProfit = max(profit, maxProfit)
            if sellPrice<buyPrice:
                l+=1
            else:
                r-=1
        return maxProfit
