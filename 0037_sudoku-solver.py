class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        assert self.solver(board,0)
    def solver(self, board: List[List[str]], p: int) -> bool:
        if p == 81:
            return True
        r,c = divmod(p,9)
        if board[r][c] != '.':
            return self.solver(board,p+1)
        digits = set('123456789')
        for i in range(9):
            d1 = board[i][c]
            d2 = board[r][i]
            if d1 in digits:
                digits.remove(d1)
            if d2 in digits:
                digits.remove(d2)
        rb,cb = r-(r%3),c-(c%3)
        for rr in range(3):
            for cc in range(3):
                d = board[rb+rr][cb+cc]
                if d in digits:
                    digits.remove(d)
        for d in digits:
            board[r][c] = d
            if self.solver(board,p+1):
                return True
        board[r][c] = '.'
        return False
