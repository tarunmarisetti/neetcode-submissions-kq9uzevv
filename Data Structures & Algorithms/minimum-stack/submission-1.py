class MinStack:

    def __init__(self):
        self.stk=[]

    def push(self, val: int) -> None:
        minEle=val
        if self.stk:
            minEle=min(self.stk[-1][1], minEle)
        self.stk.append((val,minEle))

    def pop(self) -> None:
        self.stk.pop()[0]
        

    def top(self) -> int:
        return self.stk[-1][0]
        

    def getMin(self) -> int:
        return self.stk[-1][1]
