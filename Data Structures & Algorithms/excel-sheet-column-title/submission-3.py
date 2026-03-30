class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res=''
        # print(ord('A'))
        while columnNumber:
            columnNumber-=1
            offset=columnNumber%26
            res+=(chr(ord('A')+offset))
            columnNumber//=26
        return res[::-1]

