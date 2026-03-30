class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk=[]
        max_area=0
        for i, curr_height in enumerate(heights):
            index_store=i
            while stk and stk[-1][0]> curr_height:
                prev_height,index=stk.pop()
                max_area=max(max_area, prev_height*(i-index))
                index_store=index
            stk.append((curr_height,index_store))
        
        n=len(heights)
        while stk:
            height,index=stk.pop()
            max_area=max(max_area, height*(n-index))
        return max_area
        