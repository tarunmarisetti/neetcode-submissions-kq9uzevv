class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(r,c):
            q=deque([(r,c)])
            grid[r][c]='0'
            while q:
                r,c=q.popleft()
                
                for x, y in directions:
                    nr,nc=r+x, c+y
                    if not(0<=nr<rows) or not(0<=nc<cols) or grid[nr][nc]=='0':
                        continue
                    grid[nr][nc]='0'
                    q.append((nr,nc))



        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        rows=len(grid)
        cols=len(grid[0])
        count=0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=='1':
                    count+=1
                    bfs(row, col)
        return count
        
        