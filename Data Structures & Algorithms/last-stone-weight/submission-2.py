class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones)>=2:
            stone1W=-heapq.heappop(stones)
            stone2W=-heapq.heappop(stones)
            if stone1W!=stone2W:
                heapq.heappush(stones, -abs(stone1W-stone2W))
        return -stones[0] if stones else 0


        