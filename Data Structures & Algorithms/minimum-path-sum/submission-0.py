class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # using dikstras
        rows=len(grid)
        cols=len(grid[0])
        start=[0,0]
        min_heap=[(grid[0][0],start)]
        visited={(0,0)}
        directions=[[0,1],[1,0]]
        while min_heap:
            currSum, [r,c]= heapq.heappop(min_heap)
            if [r,c]==[rows-1, cols-1]:
                return currSum
            
            for x,y in directions:
                newR,newC=x+r, y+c
                if 0<=newR<rows and 0<=newC<cols and (newR, newC) not in visited:
                    heapq.heappush(min_heap,(currSum+grid[newR][newC], [newR,newC]))
                    visited.add((newR, newC))
            
            
        