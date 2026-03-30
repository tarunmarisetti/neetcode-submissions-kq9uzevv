class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s):
            return s==s[::-1]
        res=[]
        path=[]
        n=len(s)
        def backtrack(start):
            if start==n:
                res.append(path[:])
                return
            for i in range(start, n):
                subString=s[start:i+1]
                if is_palindrome(subString):
                    path.append(subString)
                    backtrack(i+1)
                    path.pop()
        backtrack(0)
        return res
        