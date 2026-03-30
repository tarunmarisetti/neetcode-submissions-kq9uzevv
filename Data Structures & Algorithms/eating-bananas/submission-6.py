class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def getEatingRate(k):
            count=0
            for pile in piles:
                count+=math.ceil(pile/k)
            return count

        l,r=1,max(piles)
        res=r
        while l<=r:
            mid=(l+r)//2
            k=getEatingRate(mid)
            if k<=h:
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res


        