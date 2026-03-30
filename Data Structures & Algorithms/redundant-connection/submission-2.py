class DSU:

    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[0]*n

    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]

    def union(self,a,b):
        rootA,rootB=self.find(a),self.find(b)
        if rootA==rootB:
            return False
        elif self.rank[rootA]>self.rank[rootB]:
            self.parent[rootB]=rootA
        elif self.rank[rootB]>self.rank[rootA]:
            self.parent[rootA]=rootB
        else:
            self.parent[rootB]=rootA
            self.rank[rootA]+=1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu=DSU(len(edges))
        for u,v in edges:
            if not dsu.union(u-1,v-1):
                return [u,v]
        