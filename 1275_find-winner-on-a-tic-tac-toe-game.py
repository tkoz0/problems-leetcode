class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid=[['','',''],['','',''],['','','']]
        def check():
            nonlocal grid
            if grid[0][0] and grid[0][0]==grid[0][1]==grid[0][2]:
                return grid[0][0]
            if grid[1][0] and grid[1][0]==grid[1][1]==grid[1][2]:
                return grid[1][0]
            if grid[2][0] and grid[2][0]==grid[2][1]==grid[2][2]:
                return grid[2][0]
            if grid[0][0] and grid[0][0]==grid[1][0]==grid[2][0]:
                return grid[0][0]
            if grid[0][1] and grid[0][1]==grid[1][1]==grid[2][1]:
                return grid[0][1]
            if grid[0][2] and grid[0][2]==grid[1][2]==grid[2][2]:
                return grid[0][2]
            if grid[0][0] and grid[0][0]==grid[1][1]==grid[2][2]:
                return grid[0][0]
            if grid[0][2] and grid[0][2]==grid[1][1]==grid[2][0]:
                return grid[0][2]
            return ''
        # start on x
        x = True
        for r,c in moves:
            grid[r][c] = 'x' if x else 'o'
            win = check()
            if win != '':
                return 'A' if win == 'x' else 'B'
            x = not x
        return 'Draw' if len(moves) == 9 else 'Pending'
