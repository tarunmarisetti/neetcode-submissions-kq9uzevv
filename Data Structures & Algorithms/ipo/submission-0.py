class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_profit=[] #max_heap
        capital_profit=[(c,p) for c , p in zip(capital,profits)]
        heapq.heapify(capital_profit)#min_heap

        for _ in range(k):
            while capital_profit and capital_profit[0][0]<=w:
                capital,profit=heapq.heappop(capital_profit)
                heapq.heappush(max_profit,-profit)

            if not max_profit:
                break
            w+=-heapq.heappop(max_profit)
        return w        