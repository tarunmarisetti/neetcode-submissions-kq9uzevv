class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        adj_lst={i:[] for i in range(n)}
        for i in range(n):
            for j in range(n):
                if i!=j:
                    dist=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                    adj_lst[i].append((dist,j))
                    adj_lst[j].append((dist,i))
        # print(adj_lst)

        min_heap=[(0,0)]
        visited=set()
        total_cost=0
        while len(visited)<n:
            dist, point=heapq.heappop(min_heap)
            if point in visited:
                continue
            total_cost+=dist
            visited.add(point)
            for dist, neighbor in adj_lst[point]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (dist, neighbor))
        return total_cost

        print(min_heap)
