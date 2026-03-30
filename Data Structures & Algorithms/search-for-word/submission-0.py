class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r,c,index):
            if index==len(word):
                return True
            elif r<0 or c<0 or r>=rows or c>=cols or board[r][c]!=word[index] or board[r][c]=='#':
                return False
            temp=board[r][c]
            board[r][c]='#'
            found=(dfs(r+1,c,index+1) or
                    dfs(r-1,c, index+1) or
                    dfs(r, c+1, index+1) or
                    dfs(r, c-1, index+1))
            board[r][c]=temp
            return found

        rows=len(board)
        cols=len(board[0])
        for row in range(rows):
            for col in range(cols):
                if dfs(row,col,0):
                    return True
        return False
        