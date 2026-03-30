class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        max_heap=[]
        for num in arr:
            heapq.heappush(max_heap,(-abs(x-num),-num))
            if len(max_heap)>k:
                heapq.heappop(max_heap)
        print(max_heap)
        return sorted([-num for dist, num in max_heap])
        