class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ways=[[0]*n for _ in range(m)]
        for col in range(n):
            ways[0][col]=1
        for row in range(m):
            ways[row][0]=1
        
        for row in range(1, m):
            for col in range(1,n):
                ways[row][col]=ways[row-1][col]+ways[row][col-1]
        return ways[m-1][n-1]
        