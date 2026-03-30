class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows=len(heights)
        cols=len(heights[0])
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        min_heap=[(0,0,0)] #[cost, r,c]
        visited=set()
        while min_heap:
            cost,i,j =heapq.heappop(min_heap)
            if (i,j) in visited:
                continue
            if (i,j)==(rows-1, cols-1):
                return cost
            visited.add((i,j))
            for x,y in directions:
                new_r, new_c= i+x, j+y
                if not(0<=new_r<rows) or not(0<=new_c<cols) or (new_r, new_c) in visited:
                    continue
                new_cost=max(cost, abs(heights[i][j]-heights[new_r][new_c]))
                if (new_r, new_c) not in visited:
                    heapq.heappush(min_heap, (new_cost, new_r,new_c))



        
        