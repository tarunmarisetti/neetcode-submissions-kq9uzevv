class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_pos=[]
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    zero_pos.append([i,j])
        for i,j in zero_pos:
            for row in range(rows):
                for col in range(cols):
                    matrix[i][col]=matrix[row][j]=0
            

        
        