class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        maxArea = 0
        while l < r:
            minVal = min(heights[l], heights[r])
            area = minVal*(r-l)
            maxArea = max(area, maxArea)
            if minVal == heights[l]:
                l+=1
            else:
                r-=1
        return maxArea
