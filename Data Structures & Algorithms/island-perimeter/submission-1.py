class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(r,c):
            if (r,c) in visited:
                return 0
            if not(0<=r<rows) or not(0<=c<cols) or grid[r][c]==0:
                return 1
            visited.add((r,c))
            count=(dfs(r+1, c)+
                dfs(r, c+1)+
                dfs(r-1, c)+
                dfs(r, c-1))

            return count
            
        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    return dfs(row,col)