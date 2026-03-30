class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_lst=defaultdict(list)
        in_degree=[0]*(len(edges)+1)
        for u,v in edges:
            adj_lst[u].append(v)
            adj_lst[v].append(u)
            in_degree[u]+=1
            in_degree[v]+=1
        
        # print(in_degree)
        queue=deque([i for i in range(1,len(in_degree)) if in_degree[i]==1])
        while queue:
            node=queue.popleft()
            in_degree[node]-=1
            for neighbour in adj_lst[node]:
                in_degree[neighbour]-=1
                if in_degree[neighbour]==1:
                    queue.append(neighbour)
        # print(in_degree)
        for u,v in reversed(edges):
            if in_degree[u]>0 and in_degree[v]>0:
                return [u,v]





        