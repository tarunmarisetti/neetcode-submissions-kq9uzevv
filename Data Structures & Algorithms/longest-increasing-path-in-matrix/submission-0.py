class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        dp={} #(r,c):LIP
        directions=[(0,1),(1,0),(-1,0),(0,-1)]

        def dfs(r,c,prevVal):
            if not (0<=r<rows and 0<=c<cols) or matrix[r][c]<=prevVal:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            res=1
            for dx, dy in directions:
                nr,nc=dx+r,dy+c
                res=max(res, 1+dfs(nr,nc, matrix[r][c]))
            dp[(r,c)]=res
            return res

        
        rows=len(matrix)
        cols=len(matrix[0])
        
        max_len=0
        for row in range(rows):
            for col in range(cols):
                max_len=max(max_len, dfs(row,col, float('-inf')))
        return max_len


        