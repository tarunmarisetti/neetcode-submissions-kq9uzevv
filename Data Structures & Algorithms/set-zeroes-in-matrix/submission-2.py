class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows=len(matrix)
        cols=len(matrix[0])
        pos=[]
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]==0:
                    pos.append((r,c))
        
        for r,c in pos:
            for row in range(rows):
                for col in range(cols):
                    if r==row or c==col:
                        matrix[row][col]=0
            

        
        