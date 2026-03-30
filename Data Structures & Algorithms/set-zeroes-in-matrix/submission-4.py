class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Use first row and first column as markers.
        # If matrix[r][c] == 0, mark its row and column in matrix[r][0] and matrix[0][c].
        # Finally, zero out cells based on these markers.
        # Use two flags to handle first row and first column separately.

        firstRowZero=False
        firstColZero=False

        rows=len(matrix)
        cols=len(matrix[0])

        # check the first row has a zero
        for col in range(cols):
            if matrix[0][col]==0:
                firstRowZero=True

        # check the first col has a zero
        for row in range(rows):
            if matrix[row][0]==0:
                firstColZero=True
            
        # now we start from 2nd row and 2nd col
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c]==0:
                    matrix[0][c]=0  #marking the firstRow 
                    matrix[r][0]=0 #marking the firstCol

        # use the markers starting from 2nd row and 2nd col
        for r in range(1,rows):
            for c in range(1, cols):
                if matrix[r][0]==0 or matrix[0][c]==0:
                    matrix[r][c]=0
        
        # check if first row has zero
        if firstRowZero:
            for col in range(cols):
                matrix[0][col]=0
        
        # check if first col has zero
        if firstColZero:
            for row in range(rows):
                matrix[row][0]=0
        




        
        