class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_lst=defaultdict(list)
        for u,v,t in times:
            adj_lst[u].append((v,t))
        
        min_heap=[]
        heapq.heappush(min_heap,((0,k)))  
        visited=set()
        t=0
        while min_heap:
            time,node=heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            t=time
            for neighbourNode,time1 in adj_lst[node]:
                heapq.heappush(min_heap,(time+time1,neighbourNode))
        return t if len(visited)==n else -1

        