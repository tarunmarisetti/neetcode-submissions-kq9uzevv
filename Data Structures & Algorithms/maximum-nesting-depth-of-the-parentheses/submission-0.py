class Solution:
    def maxDepth(self, s: str) -> int:
        stk=[]
        opens=0
        maxOpens=0
        for char in s:
            if char=='(':
                opens+=1
                maxOpens=max(maxOpens, opens)
            elif char==')':
                opens-=1
        return maxOpens
        