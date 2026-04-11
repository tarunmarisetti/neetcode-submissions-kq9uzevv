class Solution {
    public boolean isValidSudoku(char[][] board) {
        List<Set<Character>> rows=new ArrayList<>();
        List<Set<Character>> cols=new ArrayList<>();
        List<Set<Character>> subBox=new ArrayList<>();
        for(int i=0; i<9; i++){
            rows.add(new HashSet<>());
            cols.add(new HashSet<>());
            subBox.add(new HashSet<>());
        }
        int bROws=board.length;
        int bCols=board[0].length;
        for(int r=0;r<bROws;r++){
            for(int c=0;c<bCols;c++){
                char currChar=board[r][c];
                if(currChar=='.') continue;
                if(rows.get(r).contains(currChar)){
                    return false;
                }
                rows.get(r).add(currChar);
                if(cols.get(c).contains(currChar)){
                    return false;
                }
                cols.get(c).add(currChar);

                int subBoxIndx=(r/3)*3+(c/3);
                if(subBox.get(subBoxIndx).contains(currChar)){
                    return false;
                }
                subBox.get(subBoxIndx).add(currChar);
            }
        }
        return true;
        
    }
}
