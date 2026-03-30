class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col_set=set()
        pos_dia_set=set()
        neg_dia_set=set()
        board=[['.']*n for i in range(n)]
        res=[]
        def backtrack(row):
            if row==n:
                board_copy=[''.join(row) for row in board]
                res.append(board_copy)
                return
            for col in range(n):
                if col in col_set or row+col in pos_dia_set or col-row in neg_dia_set:
                    continue
                board[row][col]='Q'
                col_set.add(col)
                pos_dia_set.add(row+col)
                neg_dia_set.add(col-row)

                backtrack(row+1)

                board[row][col]='.'
                col_set.remove(col)
                pos_dia_set.remove(row+col)
                neg_dia_set.remove(col-row)

        backtrack(0)
        return res
        