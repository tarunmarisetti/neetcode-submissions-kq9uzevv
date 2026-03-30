class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_no_of_hours_to_complete(k):
            total_time=0
            for p in piles:
                total_time+=math.ceil(float(p)/k)
            return total_time

        left=1
        right=max(piles)
        res=right
        while left<=right:
            k=(left+right)//2
            total_time=get_no_of_hours_to_complete(k)
            if total_time<=h:
                res=k
                right=k-1
            else:
                left=k+1
        return res
        