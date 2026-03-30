class Solution:
    def trap(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        water_trapped=0
        max_left,max_right=height[left],height[right]
        while left<right:
            if max_left<max_right:
                left+=1
                max_left=max(max_left,height[left])
                water_trapped+=max_left-height[left]
            else:
                right-=1
                max_right=max(max_right,height[right])
                water_trapped+=max_right-height[right]
        return water_trapped

        