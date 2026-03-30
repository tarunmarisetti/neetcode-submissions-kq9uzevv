class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        finalRes=[]
        n=len(s)
        wordSet=set(wordDict)
        def backtrack(i,res):
            if i==n:
                finalRes.append(" ".join(res))
            
            for j in range(i, n):
                if s[i:j+1] in wordSet:
                    res.append(s[i:j+1])
                    backtrack(j+1, res)
                    res.pop()
        backtrack(0,[])
        return finalRes
        