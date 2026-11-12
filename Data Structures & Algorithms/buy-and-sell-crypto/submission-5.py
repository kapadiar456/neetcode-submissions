class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return prices[0]
        j = 1
        maxProf = 0
        i = 0
        while i < len(prices)-1 and j<len(prices)-1:
            if prices[j]<prices[i]:
                i = j
            prof = prices[j] - prices[i]
            maxProf = max(prof, maxProf)
            j+=1
        return maxProf
