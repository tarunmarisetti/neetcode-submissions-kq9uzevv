class CountSquares:

    def __init__(self):
        self.points=[]
        self.pointsCount=defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.pointsCount[tuple(point)]+=1

    def count(self, point: List[int]) -> int:
        res=0
        qx,qy=point
        for x,y in self.points:
            if (abs(qx-x)!=abs(qy-y)) or qx==x or qy==y:
                continue
            res+=self.pointsCount[(x,qy)] * self.pointsCount[(qx,y)]
        return res
        
