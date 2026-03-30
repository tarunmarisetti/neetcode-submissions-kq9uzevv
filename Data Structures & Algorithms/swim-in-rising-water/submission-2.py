class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        # start from top left
        min_heap=[(grid[0][0],0,0)]
        visited=set()
        while min_heap:
            time,x,y=heapq.heappop(min_heap)
            if (x,y)==(n-1,n-1):
                return time
            if (x,y) in visited:
                continue
            
            visited.add((x,y))
            for i, j in directions:
                new_x,new_y=x+i,y+j
                if not(0<=new_x<n) or not(0<=new_y<n) or (new_x, new_y) in visited:
                    continue
                heapq.heappush(min_heap,(max(time,grid[new_x][new_y]), new_x, new_y))
            

        