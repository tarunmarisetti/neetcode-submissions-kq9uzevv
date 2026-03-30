class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        n=len(heights)
        max_area=0
        for i, height in enumerate(heights):
            index_store=i
            while stack and stack[-1][1]>height:
                index,prev_height=stack.pop()
                max_area=max(max_area,(i-index)*prev_height)
                index_store=index    
            stack.append((index_store,height))
        print(stack)
        for index,height in stack:
            max_area=max(max_area,(n-index)*height)
        return max_area
        