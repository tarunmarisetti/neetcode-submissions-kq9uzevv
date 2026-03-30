class CountSquares:

    def __init__(self):
        self.pointsDict=defaultdict(int)
        self.points=[]
        
    def add(self, point: List[int]) -> None:
        self.pointsDict[tuple(point)]+=1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        qx,qy=point
        res=0
        for x,y in self.points:
            # the currpoint and the query point should be diagonal
            if (abs(x-qx)!=abs(y-qy)) or (qx==x and qy==y):
                continue
            res+=self.pointsDict[(x,qy)]*self.pointsDict[(qx,y)]
        return res


