class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # using dikstra's algo
        adj_lst=defaultdict(list)

        for u,v,w in times:
            adj_lst[u].append((w,v))
        print(adj_lst)
        
        min_heap=[(0,k)] #[time, node]

        visited=set()

        t=0
        while min_heap:
            time, node =heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            t=time

            for neighTime, neigh in adj_lst[node]:
                heapq.heappush(min_heap,(time+neighTime, neigh))
        return t if len(visited)==n else -1
        