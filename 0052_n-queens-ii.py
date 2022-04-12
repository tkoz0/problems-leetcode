class Solution:
    def totalNQueens(self, n: int) -> int:
        ret = 0
        # taken lines
        #rows = [False]*n
        cols = [False]*n
        diags = [False]*(n+n-1) # r+c
        drdiags = [False]*(n+n-1) # n-1-r+c
        stack = [] # column values
        def recur(r):
            nonlocal ret
            if r == n:
                ret += 1
            else:
                for c in range(n):
                    if cols[c] or diags[r+c] or drdiags[n-1-r+c]:
                        continue
                    diags[r+c] = True
                    drdiags[n-1-r+c] = True
                    stack.append(c)
                    cols[c] = True
                    recur(r+1)
                    cols[c] = False
                    stack.pop()
                    diags[r+c] = False
                    drdiags[n-1-r+c] = False
        recur(0)
        return ret
