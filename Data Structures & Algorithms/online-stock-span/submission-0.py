class StockSpanner:

    def __init__(self):
        self.stk=[]
        

    def next(self, price: int) -> int:
        count=0
        self.stk.append(price)
        i=len(self.stk)
        while i and self.stk[i-1]<=price:
            count+=1
            i-=1
        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)