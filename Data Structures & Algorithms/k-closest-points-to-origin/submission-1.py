class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap=[]
        for x, y in points:
            dist=x**2+y**2
            if len(max_heap)==k:
                heapq.heappushpop(max_heap, (-dist,(x,y)))
            else:
                heapq.heappush(max_heap, (-dist,(x,y)))


        return[dist[1] for dist in max_heap]

        