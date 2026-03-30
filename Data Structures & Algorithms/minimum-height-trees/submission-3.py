class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # we can solve this using topological sort
        # like layer by layer

        if n==1:
            return [0]
        adj_lst=defaultdict(list)
        neighborNodesCount=[0]*n
        for u,v in edges:
            adj_lst[u].append(v)
            adj_lst[v].append(u)
            neighborNodesCount[u]+=1
            neighborNodesCount[v]+=1
        
        q=deque([i for i, neighCount in enumerate(neighborNodesCount) if neighCount==1])

        while q:
            if n<=2:
                return list(q)

            for _ in range(len(q)):
                leave=q.popleft()
                n-=1
                for neigh in  adj_lst[leave]:
                    neighborNodesCount[neigh]-=1
                    if neighborNodesCount[neigh]==1:
                        q.append(neigh)
            




        