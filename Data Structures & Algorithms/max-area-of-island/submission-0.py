class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r,c):
            if not 0<=r<rows or not 0<=c<cols or grid[r][c]!=1:
                return 0
            grid[r][c]=0
            return 1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1)

        rows=len(grid)
        cols=len(grid[0])
        max_area=0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    area=dfs(row, col)
                    max_area=max(max_area,area)
        return max_area


        