class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==0:
                return 1
            if (r,c) in visited:
                return 0
            visited.add((r,c))
            perimeter= dfs(r+1,c) +dfs(r-1,c)+ dfs(r,c+1) + dfs(r, c-1)
            return perimeter
            
        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    return dfs(row,col)
        