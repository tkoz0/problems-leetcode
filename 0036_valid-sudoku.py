class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in board:
            nums = set()
            for n in r:
                if n != '.' and n in nums:
                    return False
                nums.add(n)
        for c in range(9):
            nums = set()
            for r in range(9):
                n = board[r][c]
                if n != '.' and n in nums:
                    return False
                nums.add(n)
        for r in range(3):
            for c in range(3):
                r2,c2 = 3*r,3*c
                nums = set()
                for dr in range(3):
                    for dc in range(3):
                        n = board[r2+dr][c2+dc]
                        if n != '.' and n in nums:
                            return False
                        nums.add(n)
        return True
