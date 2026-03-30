class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left,right=0,len(matrix)-1
        while left<right:
            for i in range(right-left):
                top,bottom=left,right
                # store topleft into temp
                temp=matrix[top][left+i]
                # rortate bottom left to topleft
                matrix[top][left+i]=matrix[bottom-i][left]
                # rotate bottom right to bottom left
                matrix[bottom-i][left]=matrix[bottom][right-i]
                # rotate top right to bottom right
                matrix[bottom][right-i]=matrix[top+i][right]
                # store temp into top right
                matrix[top+i][right]=temp
            left+=1
            right-=1




        