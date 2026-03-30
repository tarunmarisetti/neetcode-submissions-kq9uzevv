class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows=len(obstacleGrid)
        cols=len(obstacleGrid[0])
        
        prevRow=[0]*cols
        for col in range(cols):
            if obstacleGrid[0][col]==1:
                break
            prevRow[col]=1
        

        for row in range(1,rows):
            currRow=[0]*cols
            currRow[0]=1 if obstacleGrid[row][0]==0 and prevRow[0]==1 else 0
            for i in range(1, len(currRow)):
                if obstacleGrid[row][i]==1:
                    currRow[i]=0
                else:
                    currRow[i]=currRow[i-1]+prevRow[i]
            prevRow=currRow
        return prevRow[-1]
        
       
        
        