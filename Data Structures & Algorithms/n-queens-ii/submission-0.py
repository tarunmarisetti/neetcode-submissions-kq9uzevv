class Solution:
    def totalNQueens(self, n: int) -> int:
        col_set=set()
        pos_dia_set=set()
        neg_dia_set=set()
        board=[['.']*n for i in range(n)]
        self.count=0
        def backtrack(row):
            if row==n:
                self.count+=1
            for col in range(n):
                if col in col_set or row+col in pos_dia_set or col-row in neg_dia_set:
                    continue
                board[row][col]="Q"
                col_set.add(col)
                pos_dia_set.add(row+col)
                neg_dia_set.add(col-row)

                backtrack(row+1)

                board[row][col]="."
                col_set.remove(col)
                pos_dia_set.remove(row+col)
                neg_dia_set.remove(col-row)
        backtrack(0)
        return self.count

        