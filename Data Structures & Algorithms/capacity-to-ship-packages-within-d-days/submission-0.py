class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_shipped(cap):
            ships,currCap=1,cap
            for weight in weights:
                if currCap-weight<0:
                    ships+=1
                    if ships>days:
                        return False
                    currCap=cap
                currCap-=weight
            return True

        left,right=max(weights),sum(weights)
        res=right
        while left<=right:
            mid=(left+right)//2
            if can_shipped(mid):
                res=mid
                right=mid-1
            else:
                left=mid+1
        return res

        
        