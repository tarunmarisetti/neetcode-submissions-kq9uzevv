class Solution:
    # monotonic increasing stack
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk=[]
        maxArea=float('-inf')
        for i, height in enumerate(heights):
            index=i
            while stk and stk[-1][0]>height:
                prevHeight,prevIndex=stk.pop()
                maxArea=max(maxArea, prevHeight*(i-prevIndex))
                index=prevIndex
            stk.append((height,index))
        
        n=len(heights)
        while stk:
            height,index=stk.pop()
            maxArea=max(maxArea, height*(n-index))
        return maxArea


        