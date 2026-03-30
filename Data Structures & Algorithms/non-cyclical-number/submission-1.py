class Solution:
    def isHappy(self, n: int) -> bool:
        def getNextNum(n):
            num=0
            while n:
                r=n%10
                num+=r**2
                n=n//10
            return num
        seen=set()
        while n:
            n=getNextNum(n)
            if n==1:
                return True
            if n in seen:
                return False
            seen.add(n)

            