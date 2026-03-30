class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow=[1]*n
        for row in range(1, m):
            currRow=[1]*n
            for i in range(1,len(currRow)):
                currRow[i]=currRow[i-1]+prevRow[i]
            prevRow=currRow 
            # print(prevRow)        
        return prevRow[-1]
        