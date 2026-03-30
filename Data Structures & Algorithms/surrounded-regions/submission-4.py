class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(r,c):
            if not(0<=r<rows) or not(0<=c<cols) or board[r][c]!='O':
                return
            board[r][c]='#'
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
        

        rows=len(board)
        cols=len(board[0])
        for row in [0,rows-1]:
            for col in range(cols):
                if board[row][col]=="O":
                    dfs(row,col)
        for row in range(rows):
            for col in [0, cols-1]:
                if board[row][col]=="O":
                    dfs(row,col)
        for row in range(rows):
            for col in range(cols):
                if board[row][col]=='O':
                    board[row][col]='X'
                elif board[row][col]=='#':
                    board[row][col]='O'
            
        