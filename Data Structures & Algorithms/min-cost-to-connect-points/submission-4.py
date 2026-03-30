'''using krushka's 
krushkals use DSU and it is mainly used for finding MST
why?
Kruskal’s algorithm is specifically designed
 to find a minimum spanning tree in an undirected weighted graph. 
 By reversing the edge order, it can also find a maximum spanning tree, 
 but it is not applicable to shortest-path problems.
 '''

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
            for j in range(i+1, n):
                x2,y2=points[j]
                dist=abs(x1-x2)+abs(y1-y2)
                edges.append((dist, i,j))
        edges.sort()
        # Kruskal’s algorithm always uses a disjoint set to efficiently detect cycles,
        #  and sorting edges by weight is required because the algorithm greedily picks 
        # the smallest valid edge at each step.
        totalCost=0
        for w,u,v in edges:
            if dsu.union(u,v):
                totalCost+=w
        return totalCost