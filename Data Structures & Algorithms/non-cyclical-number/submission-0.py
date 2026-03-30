class Solution:
    def sumOfSquares(self,num):
        summ=0
        while(num):
            r=num%10
            summ+=r**2
            num=num//10
        return summ

    def isHappy(self, n: int) -> bool:
        slow=self.sumOfSquares(n)
        fast=self.sumOfSquares(self.sumOfSquares(n))
        while slow!=fast:
            fast=self.sumOfSquares(self.sumOfSquares(fast))
            slow=self.sumOfSquares(slow)
        return True if fast==1 else False