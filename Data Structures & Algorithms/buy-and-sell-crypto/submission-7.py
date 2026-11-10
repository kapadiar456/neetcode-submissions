class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        j = 0
        maxProf = 0
        i = 0
        while i < len(prices)-1:
            if prices[j]<prices[i]:
                i = j
            prof = prices[j] - prices[i]
            maxProf = max(prof, maxProf)
            j+=1
            if j>=len(prices):
                break
        return maxProf
