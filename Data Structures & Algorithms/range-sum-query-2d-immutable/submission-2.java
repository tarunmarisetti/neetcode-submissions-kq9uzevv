class NumMatrix {

    private int[][] prefixMatrix;

    public NumMatrix(int[][] matrix) {
        int rows=matrix.length;
        int cols=matrix[0].length;
        prefixMatrix=new int[rows+1][cols+1];

        for(int r=0; r<rows; r++){
            int prefix=0;
            for(int c=0; c<cols; c++){
                prefix+=matrix[r][c];
                prefixMatrix[r+1][c+1]=prefix+prefixMatrix[r][c+1];
            }
        }
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        row1+=1;
        col1+=1;
        row2+=1;
        col2+=1;

        int totalSum=prefixMatrix[row2][col2];
        int topSum=prefixMatrix[row1-1][col2];
        int leftSum=prefixMatrix[row2][col1-1];
        int topLeftSum=prefixMatrix[row1-1][col1-1];
        return totalSum-topSum-leftSum+topLeftSum;
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */