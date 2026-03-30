class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # adj_lst
        adjLst={}
        for u,v in edges:
            if u not in adjLst:
                adjLst[u]=[]
            if v not in adjLst:
                adjLst[v]=[]
            adjLst[u].append(v)
            adjLst[v].append(u)
        
        q=deque([(0,-1)]) #(child, parent)
        visited=set()
        visited.add(0)
        while q:
            child, parent=q.popleft()
            for neigh in adjLst.get(child,[]):
                if neigh==parent:
                    continue
                elif neigh in visited:
                    return False
                visited.add(neigh)
                q.append((neigh, child))
        return len(visited)==n


        