class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent=list(range(n))
        rank=[0]*n
        def find(x):
            if parent[x]!=x:
                # path compression
                parent[x]=find(parent[x])
            return parent[x]
        
        def union(a,b):
            rootA,rootB=find(a),find(b)
            if rootA==rootB:
                return 
            if rank[rootA]>rank[rootB]:
                parent[rootB]=rootA
            elif rank[rootA]<rank[rootB]:
                parent[rootA]=rootB
            else:
                parent[rootB]=rootA
                rank[rootA]+=1
        
        for u,v in edges:
            union(u,v)

        res=0
        for i in range(n):
            if i==find(i):
                res+=1
        return res
        

        