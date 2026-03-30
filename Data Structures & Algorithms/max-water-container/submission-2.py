class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea=float('-inf')
        l=0
        r=len(heights)-1
        while l<r:
            height=min(heights[l],heights[r])
            currArea=height*(r-l)
            maxArea=max(maxArea, currArea)
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return maxArea
        