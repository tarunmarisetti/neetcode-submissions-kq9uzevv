class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # minimum spanning tree can solve by prims and krushkals
        # below is the prims sol- same like djisktras using set and min_heap
        N=len(points)
        adj_lst={i:[] for i in range(N)}
        for i in range(N):
            x1,y1=points[i]
            for j in range(i+1,N):
                x2,y2=points[j]
                dist=abs(x1-x2)+abs(y1-y2)
                adj_lst[i].append([dist,j])
                adj_lst[j].append([dist,i])
        # print(adj_lst)
        min_heap=[(0,0)]
        visited=set()
        total_cost=0
        while len(visited)<N:
            cost,node=heapq.heappop(min_heap)
            if node in visited:
                continue
            total_cost+=cost
            visited.add(node)
            for neighbor_cost,neighbor in adj_lst[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap,(neighbor_cost, neighbor))
        return total_cost
            

        
        