class Solution:
    def totalNQueens(self, n: int) -> int:
        col_set=set()
        pos_dia=set()
        neg_dia=set()
        count=0
        def backtrack(row):
            nonlocal count
            if row==n:
                count+=1
                return
            
            for col in range(n):
                if col in col_set or row+col in pos_dia or col-row in neg_dia:
                    continue
                col_set.add(col)
                pos_dia.add(row+col)
                neg_dia.add(col-row)

                backtrack(row+1)

                col_set.remove(col)
                pos_dia.remove(row+col)
                neg_dia.remove(col-row)
        backtrack(0)
        return count




        