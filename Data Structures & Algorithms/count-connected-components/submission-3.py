class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #using DSU
        parent=list(range(n))
        rank=[0]*n

        def find(x):
            if parent[x]!=x:
                # path compression
                parent[x]=find(parent[x])
            return parent[x]
        
        def union(nodeA, nodeB):
            rootA,rootB=find(nodeA),find(nodeB)
            if rootA==rootB:
                return False
            if rank[rootA]>rank[rootB]:
                parent[rootB]=rootA
            elif rank[rootA]<rank[rootB]:
                parent[rootA]=rootB
            else:
                parent[rootB]=rootA
                rank[rootA]+=1
            return True
        
        for u, v in edges:
            union(u,v)
        
        count=0
        for i in range(n):
            if parent[i]==i:
                count+=1
        return count
        