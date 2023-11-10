class Solution:
    def look(self, board, word, visit, r, c) -> bool:
        m = len(board)
        n = len(board[0])
        if word == '':
            return True
        if r < 0 or c < 0 or r >= m or c >= n:
            return False
        if visit[r][c]:
            return False
        if board[r][c] != word[0]:
            return False
        visit[r][c] = True
        ret = False
        for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            i,j = r+dr,c+dc
            if self.look(board,word[1:],visit,i,j):
                ret = True
                break
        visit[r][c] = False
        return ret
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visit = [[False]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.look(board,word,visit,i,j):
                    return True
        return False
