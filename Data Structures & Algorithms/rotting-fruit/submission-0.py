class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:           

        rows=len(grid)
        cols=len(grid[0])
        fresh_fruits=0
        q=deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    fresh_fruits+=1
                elif grid[row][col]==2:
                    q.append((row,col))
        time=0
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while q and fresh_fruits:
            for _ in range(len(q)):
                r,c=q.popleft()
                for dx,dy in directions:
                    nr,nc=r+dx,c+dy
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        fresh_fruits-=1
                        grid[nr][nc]=2
                        q.append((nr,nc))
            time+=1
            
        return time if not fresh_fruits else -1
        