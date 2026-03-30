class MyQueue:

    def __init__(self):
        self.pushStk=[]
        self.popStk=[]
        

    def push(self, x: int) -> None:
        self.pushStk.append(x)

    def pop(self) -> int:
        if not self.popStk:
            while self.pushStk:
                self.popStk.append(self.pushStk.pop())
        return self.popStk.pop()
        

    def peek(self) -> int:
        if not self.popStk:
            while self.pushStk:
                self.popStk.append(self.pushStk.pop())
        return self.popStk[-1]

    def empty(self) -> bool:
        return max(len(self.pushStk), len(self.popStk))==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()