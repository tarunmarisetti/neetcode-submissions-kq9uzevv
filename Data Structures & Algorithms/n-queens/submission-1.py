class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[['.']*n for i in range(n)]
        col_set=set()
        pos_dia=set()
        neg_dia=set()
        res=[]
        def backtrack(row):
            if row==n:
                boardCopy=["". join(row) for row in board]
                res.append(boardCopy)
                return 
            for col in range(n):
                if col in col_set or row+col in pos_dia or col-row in neg_dia:
                    continue
                board[row][col]='Q'
                col_set.add(col)
                pos_dia.add(row+col)
                neg_dia.add(col-row)
                backtrack(row+1)

                board[row][col]='.'
                col_set.remove(col)
                pos_dia.remove(row+col)
                neg_dia.remove(col-row)
        backtrack(0)
        return res

