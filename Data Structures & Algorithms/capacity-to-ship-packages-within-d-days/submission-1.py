class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShipped(capacity):
            ships=1
            currCap=capacity
            for weight in weights:
                if currCap-weight<0:
                    ships+=1
                    if ships>days:
                        return False
                    currCap=capacity #this is fresh capacity as we gave a new ship (above we incremeted ship)
                currCap-=weight
            return True

        l=max(weights)
        r=sum(weights)
        res=r
        while l<=r:
            mid=(l+r)//2
            if canShipped(mid):
                res=min(res,mid)
                r=mid-1
            else:
                l=mid+1
        return res
        
        