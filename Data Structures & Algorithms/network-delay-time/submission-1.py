class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_lst={i:[] for i in range(1,n+1)}
        
        for u,v,time in times:
            adj_lst[u].append((v,time))
        # print(adj_lst)
        min_heap=[(0,k)]
        t=0
        visited=set()
        while min_heap:
            time,node=heapq.heappop(min_heap)
            # print(time,node)
            if node in visited:
                continue
            visited.add(node)
            t=time
            for neighbor,neighbor_time in adj_lst[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (t+neighbor_time, neighbor))
            # print(min_heap)
        # print(t)
        return t if len(visited)==n else -1

        