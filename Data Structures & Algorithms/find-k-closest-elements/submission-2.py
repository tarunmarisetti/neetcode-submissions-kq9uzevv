class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        min_heap=[]
        for num in arr:
            dist=abs(num-x)
            heapq.heappush(min_heap,(-dist,-num))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        return sorted([ -num for dist, num in min_heap ])

        