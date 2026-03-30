class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)>n-1:
            return False
        adj_lst=[[] for _ in range(n)]
        for u,v in edges:
            adj_lst[u].append(v)
            adj_lst[v].append(u)

        visited=set()
        queue=deque([(0,-1)])
        visited.add(0)
        while queue:
            node,parent=queue.popleft()
            for neigh in adj_lst[node]:
                if neigh==parent:
                    continue
                elif neigh in visited:
                    return False 
                visited.add(neigh)
                queue.append((neigh,node))
        return len(visited)==n
        