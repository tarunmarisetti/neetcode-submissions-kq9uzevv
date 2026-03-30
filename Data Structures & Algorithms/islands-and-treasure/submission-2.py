class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        def bfs(r,c):
            if not 0<=r<rows or not 0<=c<cols or grid[r][c]==-1 or (r,c) in visited:
                return
            visited.add((r,c))
            q.append((r,c))
            
        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        q=deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==0:
                    q.append((row,col))
                    visited.add((row,col))

        dist=0
        while q:
            for _ in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=dist
                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c+1)
                bfs(r,c-1)
            dist+=1

        