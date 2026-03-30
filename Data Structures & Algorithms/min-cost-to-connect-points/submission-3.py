class DSU:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[0]*n

    def find(self,node):
        if self.parent[node]!=node:
            self.parent[node]=self.find(self.parent[node])
        return self.parent[node]

    def union(self, nodeA, nodeB):
        rootA=self.find(nodeA)
        rootB=self.find(nodeB)

        if rootA==rootB:
            return False
        if self.rank[rootA]>self.rank[rootB]:
            self.parent[rootB]=rootA
        elif self.rank[rootA]<self.rank[rootB]:
            self.parent[rootA]=rootB
        else:
            self.parent[rootB]=rootA
            self.rank[rootA]+=1
        return True


    
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        dsu=DSU(n)
        edges=[]
        for i in range(n):
            x1,y1=points[i]
            for j in range(i+1,n):
                x2,y2=points[j]
                dist=abs(x1-x2)+abs(y1-y2)
                edges.append((dist,i,j))

        total_cost=0
        edges.sort()  #required for krushkals
        for dist,u,v in edges:
            if dsu.union(u,v):
                total_cost+=dist
        return total_cost



