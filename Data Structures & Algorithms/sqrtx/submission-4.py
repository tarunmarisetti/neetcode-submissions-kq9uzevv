class Solution:
    def mySqrt(self, x: int) -> int:
        l,r=0,x
        res=0
        while l<=r:
            mid=(l+r)//2
            guess=mid**2
            if guess==x:
                return mid
            elif guess<x:
                res=mid
                l=mid+1
            else:
                r=mid-1
        return res

        