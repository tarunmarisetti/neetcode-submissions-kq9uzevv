class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        min_heap=[-stone for stone in stones]
        heapq.heapify(min_heap)
        while len(min_heap)>=2:
            stone1=-heapq.heappop(min_heap)
            stone2=-heapq.heappop(min_heap)
            diff=stone1-stone2
            if diff>0:
                heapq.heappush(min_heap,-diff)
        return -min_heap[0] if min_heap else 0

        