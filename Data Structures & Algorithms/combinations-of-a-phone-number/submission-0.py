class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        path=[]
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        def backtrack(index):
            if len(path)==len(digits):
                res.append(''.join(path))
                return
            
            combination=digitToChar[digits[index]]
            for char in combination:
                path.append(char)
                backtrack(index+1)
                path.pop()
        backtrack(0)
        return res
            


        

        