class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        freshOranges=0
        time=0
        q=deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    freshOranges+=1
                elif grid[row][col]==2:
                    q.append((row,col))

        
        def bfs(r,c):
            nonlocal freshOranges
            if not(0<=r<rows) or not(0<=c<cols) or  grid[r][c]!=1:
                return
            grid[r][c]=2
            freshOranges-=1
            q.append((r,c))
        
        while q and freshOranges>0:
            for _ in range(len(q)):
                r,c=q.popleft()
                bfs(r+1,c)
                bfs(r,c+1)
                bfs(r-1,c)
                bfs(r,c-1)
            time+=1
        
        return time if freshOranges==0 else -1

        