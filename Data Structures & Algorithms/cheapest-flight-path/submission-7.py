class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_lst={i:[] for i in range(n)}
        for u,v,cost in flights:
            adj_lst[u].append((cost,v))
        # print(adj_lst)
        min_heap=[(0,0,src)] #(cost, k, node)
        best={}
        while min_heap:
            cost,stops,node=heapq.heappop(min_heap)
            if stops>k+1:
                continue
            if node==dst:
                return cost
            if (stops,node)in best and best[(stops,node)]<=cost:
                continue
            best[(stops, node)]=cost
            for neighCost,neighbor in adj_lst[node]:
                heapq.heappush(min_heap,(cost+neighCost, stops+1, neighbor))
        return  -1


        