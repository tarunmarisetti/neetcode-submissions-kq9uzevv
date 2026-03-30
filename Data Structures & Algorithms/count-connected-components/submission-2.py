class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # using dfs
        adj_lst=[[] for _ in range(n)]

        for u, v in edges:
            adj_lst[u].append(v)
            adj_lst[v].append(u)
        
        def dfs(node):
            for neigh in adj_lst[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    dfs(neigh)

        visited=set()
        count=0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count+=1
        return count
        
        