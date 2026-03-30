class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        prevRow=[0]*cols
        prevRow[0]=grid[0][0]
        for i in range(1,len(prevRow)):
            prevRow[i]=grid[0][i]+prevRow[i-1]
        
        for row in range(1, rows):
            currRow=[0]*cols
            currRow[0]=grid[row][0]+prevRow[0]
            for i in range(1, len(currRow)):
                currRow[i]=min(prevRow[i],currRow[i-1])+grid[row][i]
            prevRow=currRow
        return prevRow[-1]