class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r,c,index):
            if index==len(word):
                return True
            if not(0<=r<rows) or not(0<=c<cols) or board[r][c]!=word[index]:
                return False
            temp=board[r][c]
            board[r][c]='#'
            found=dfs(r+1,c,index+1) or dfs(r-1,c,index+1) or dfs(r,c+1, index+1) or dfs(r,c-1,index+1)
            board[r][c]=temp
            return found

        rows=len(board)
        cols=len(board[0])
        for row in range(rows):
            for col in range(cols):
                if board[row][col]==word[0]:
                    if dfs(row,col,0):
                        return True
        return False
        