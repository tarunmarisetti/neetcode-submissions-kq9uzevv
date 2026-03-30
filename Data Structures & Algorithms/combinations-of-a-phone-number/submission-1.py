class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        combinations={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res=[]
        def backtrack(i,path):
            if len(path)==len(digits):
                res.append(''.join(path))
                return
            for letter in combinations[digits[i]]:
                path.append(letter)
                backtrack(i+1,path)
                path.pop()
        backtrack(0,[]) 
        return res
        