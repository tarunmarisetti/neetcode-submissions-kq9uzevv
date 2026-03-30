class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(r,c,visited, prevHeight):
            if not(0<=r<rows) or not(0<=c<cols) or (r,c) in visited or prevHeight>heights[r][c]:
                return
            visited.add((r,c)) 
            dfs(r+1,c,visited, heights[r][c])
            dfs(r,c+1,visited, heights[r][c])
            dfs(r-1,c,visited, heights[r][c])
            dfs(r,c-1,visited, heights[r][c])

        rows=len(heights)
        cols=len(heights[0])
        pac_set=set()
        atl_set=set()

        for col in range(cols):
            dfs(0, col, pac_set, heights[0][col])
            dfs(rows-1, col, atl_set, heights[rows-1][col])
        for row in range(rows):
            dfs(row, 0, pac_set, heights[row][0])
            dfs(row, cols-1, atl_set, heights[row][cols-1])
        
        res=[]
        for pair in pac_set:
            if pair in atl_set:
                res.append(pair)
        return res


        