class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for i in range(9)]
        cols=[set() for i in range(9)]
        boxs=[set() for i in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                digit=board[i][j]
                if digit == '.':
                    continue
                box_indx=(i//3)*3 +(j//3)
                if digit in cols[j] or digit in rows[i] or digit in boxs[box_indx]:
                    return False
                rows[i].add(digit)
                cols[j].add(digit)
                boxs[box_indx].add(digit)
        return True

        