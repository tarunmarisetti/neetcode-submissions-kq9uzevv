class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def getEatingRate(k):
            time=0
            for pile in piles:
                time+=math.ceil(pile/k)
            return time

        l,r=1,max(piles)
        res=r
        while l<=r:
            mid=(l+r)//2
            timeNeeded=getEatingRate(mid)
            if timeNeeded<=h:
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res


        