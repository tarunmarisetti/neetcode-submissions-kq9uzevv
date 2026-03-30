class Solution:
    def __init__(self):
        self.cache={}
    
    def tribonacci(self, n: int) -> int:
        if n<=2:
            return 1 if n!=0 else 0
        if n in self. cache:
            return self.cache[n]
        self.cache[n]= self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)
        return self.cache[n]
        