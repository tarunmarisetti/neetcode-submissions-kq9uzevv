class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions=[(1,0),(0,1),(0,-1),(-1,0)]
        rows=len(grid)
        cols=len(grid[0])
        min_heap=[(grid[0][0],0,0)]
        visited=set()
        while min_heap:
            time,i,j=heapq.heappop(min_heap)
            if (i,j)==(rows-1,cols-1):
                return time
            if (i,j) in visited:
                continue
            visited.add((i,j))
            for x,y in directions:
                new_x,new_y=x+i,y+j
                if not (0<=new_x<rows) or not(0<=new_y<cols) or (new_x,new_y)in visited:
                    continue
                heapq.heappush(min_heap,(max(time,grid[new_x][new_y]),new_x,new_y))
        
                
            
        
        