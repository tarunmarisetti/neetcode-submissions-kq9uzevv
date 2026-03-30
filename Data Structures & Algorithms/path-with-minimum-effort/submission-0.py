class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows=len(heights)
        cols=len(heights[0])
        min_heap=[(0,0,0)]
        visited=set()
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        while min_heap:
            diff,i,j =heapq.heappop(min_heap)
            if (i,j) in visited:
                continue
            visited.add((i,j))
            if (i,j)==(rows-1,cols-1):
                return diff
            for x,y in directions:
                new_i,new_j=i+x,j+y
                if not(0<=new_i<rows) or not(0<=new_j<cols) or (new_i,new_j) in visited:
                    continue
                newDiff=max(diff,abs(heights[new_i][new_j]-heights[i][j]))
                heapq.heappush(min_heap,(newDiff,new_i,new_j))
        

                

        