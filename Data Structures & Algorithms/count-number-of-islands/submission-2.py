class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c):
            if not(0<=r<rows) or not(0<=c<cols) or grid[r][c]=='0':
                return
            grid[r][c]='0'
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)

        rows=len(grid)
        cols=len(grid[0])
        count=0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=='1':
                    count+=1
                    dfs(row, col)
        return count
        