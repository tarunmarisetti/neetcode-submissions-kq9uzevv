class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def dfs(r,c,visit,prevHeight):
            if r<0 or c<0 or r==rows or c==cols or (r,c) in visit or heights[r][c]<prevHeight:
                return
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])

        rows=len(heights)
        cols=len(heights[0])
        pac=set()
        atl=set()

        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows-1,c, atl, heights[rows-1][c])
        for r in range(rows):
            dfs(r,0,pac, heights[r][0])
            dfs(r,cols-1,atl,heights[r][cols-1])

        res=[]
        for row in range(rows):
            for col in range(cols):
                if (row,col) in atl and (row,col) in pac:
                    res.append((row,col))
        return res
        
        