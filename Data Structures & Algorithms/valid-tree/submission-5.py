class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_lst=defaultdict(list)
        # the no of edges shoukd be less than n-1 to be a valid tree
        if len(edges)>n-1:
            return False
        for u,v in edges:
            adj_lst[u].append(v)
            adj_lst[v].append(u)
        
        q=deque([(0,-1)]) #(child, parent)
        visited=set()
        visited.add(0)
        while q:
            child, parent=q.popleft()
            for neigh in adj_lst[child]:
                if neigh==parent:
                    continue
                elif neigh in visited:
                    return False
                visited.add(neigh)
                q.append((neigh, child))
        return len(visited)==n
                

        