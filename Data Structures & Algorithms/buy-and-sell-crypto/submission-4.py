class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        j = 0
        maxProf = 0
        for i in range(len(prices)):
            j = i
            while prices[i] <= prices[j] and j < len(prices)-1:
                j+=1
                prof = prices[j] - prices[i]
                maxProf = max(prof, maxProf)
        return maxProf
