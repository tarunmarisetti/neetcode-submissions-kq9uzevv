class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        def dfs(node):
            for neighbor in adj_lst[node]:
                if not visited[neighbor]:
                    visited[neighbor]=True
                    dfs(neighbor)


        adj_lst=[[] for _ in range(n)]
        visited=[False]*n
        for u,v in edges:
            adj_lst[u].append(v)
            adj_lst[v].append(u)

        count=0
        for node in range(n):
            if not visited[node]:
                visited[node]=True
                count+=1
                dfs(node)
        return count
        