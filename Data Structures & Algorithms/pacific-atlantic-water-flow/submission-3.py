class Solution:
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(row, col, visited, prevHeight):
            if not(0<=row<rows) or not(0<=col<cols) or (row, col) in visited or heights[row][col]<prevHeight:
                return 
            visited.add((row,col))
            dfs(row+1, col, visited, heights[row][col] )
            dfs(row, col+1, visited, heights[row][col] )
            dfs(row-1, col, visited, heights[row][col] )
            dfs(row, col-1, visited, heights[row][col] )

        rows=len(heights)
        cols=len(heights[0])
        pacific=set()
        atlantic=set()
        for row in range(rows):
            dfs(row,0, pacific, heights[row][0])
            dfs(row, cols-1, atlantic, heights[row][cols-1])
        
        for col in range(cols):
            dfs(0,col,pacific, heights[0][col])
            dfs(rows-1, col, atlantic, heights[rows-1][col])
        
        res=[]
        for pair in pacific:
            if pair in atlantic:
                res.append(pair)
        return res


        