class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows=len(obstacleGrid)
        cols=len(obstacleGrid[0])
        ways=[[0]*cols for _ in range(rows)]

        for row in range(rows):
            if obstacleGrid[row][0]==1:
                break
            ways[row][0]=1
        
        for col in range(cols):
            if obstacleGrid[0][col]==1:
                break
            ways[0][col]=1
        # print(ways)

        for row in range(1, rows):
            for col in range(1,cols):
                if obstacleGrid[row][col]==1:
                    ways[row][col]=0
                else:
                    ways[row][col]=ways[row-1][col]+ways[row][col-1]
        return ways[rows-1][cols-1]
        
        