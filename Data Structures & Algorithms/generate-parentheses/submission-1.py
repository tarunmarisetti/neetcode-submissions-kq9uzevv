class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path=[]
        res=[]
        def backtrack(left,right,path):
            if len(path)==n*2:
                res.append(path)
            if left<n:
                backtrack(left+1,right,path+"(")
            if right<left:
                backtrack(left,right+1, path+(")"))
        backtrack(0,0,'')
        return res
        