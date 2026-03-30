class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        directions=[(1,0),(0,1),(0,-1),(-1,0)]
        min_heap=[]
        heapq.heappush(min_heap, (grid[0][0],0,0))
        visited={(0,0)}
        while min_heap:
            time,r,c=heapq.heappop(min_heap)
            if (r,c)==(rows-1,cols-1):
                return time
            for x,y in directions:
                newR, newC=x+r, y+c
                if 0<=newR<rows and 0<=newC<cols and (newR, newC) not in visited:
                    visited.add((newR, newC))
                    heapq.heappush(min_heap,(max(time, grid[newR][newC]), newR, newC))
        



        