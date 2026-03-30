class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        l,r=0,n-1
        maxLeft=height[0]
        maxRight=height[n-1]
        waterTrapped=0
        while l<r:
            if maxLeft<maxRight:
                l+=1
                maxLeft=max(maxLeft, height[l])
                waterTrapped+=maxLeft-height[l]
            else:
                r-=1
                maxRight=max(maxRight, height[r])
                waterTrapped+=maxRight-height[r]
        return waterTrapped

        