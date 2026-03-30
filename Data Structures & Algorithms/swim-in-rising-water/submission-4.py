class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        min_heap=[(grid[0][0],0,0)]
        visited=set()
        while min_heap:
            t,r,c=heapq.heappop(min_heap)
            if (r,c) in visited:
                continue
            if (r,c)==(rows-1,cols-1):
                return t
            visited.add((r,c))
            for x, y in directions:
                newR,newC=x+r, y+c
                if not(0<=newR<rows) or not(0<=newC<cols) or (newR, newC) in visited:
                    continue
                heapq.heappush(min_heap, (max(t, grid[newR][newC]),newR,newC))




        