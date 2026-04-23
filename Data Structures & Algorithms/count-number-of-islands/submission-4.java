class Solution {

    private int rows, cols;
    private char[][] grid;
    
    public void dfs(int r, int c){
        if(r<0 || r>=rows || c<0 || c>=cols || grid[r][c]=='0'){
            return;
        }
        grid[r][c]='0';

        dfs(r+1,c);
        dfs(r,c+1);
        dfs(r-1,c);
        dfs(r,c-1);
    }
    public int numIslands(char[][] grid) {
        this.grid=grid;
        rows=grid.length;
        cols=grid[0].length;
        int noOfIslands=0;
        for(int r=0; r< rows; r++){
            for(int c=0; c<cols; c++){
                if(grid[r][c]=='1'){
                    dfs(r,c);
                    noOfIslands+=1;
                }
            }
        }
        return noOfIslands;
    }
}
