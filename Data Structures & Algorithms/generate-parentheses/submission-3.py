class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def backtrack(path,left,right):
            if len(path)==n*2:
                res.append(path)
            if left<n:
                backtrack(path+'(',left+1,right)
            if right<left:
                backtrack(path+')',left,right+1)
        backtrack('',0,0)
        return res
        