class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def find_hours(k):
            total_time=0
            for pile in piles:
                total_time+=math.ceil(float(pile)/k)
            return total_time

        l=1
        r=max(piles)
        res=r
        while l<=r:
            k=(l+r)//2
            total_time=find_hours(k)
            if total_time<=h:
                res=k
                r=k-1
            else:
                l=k+1
        return res

        