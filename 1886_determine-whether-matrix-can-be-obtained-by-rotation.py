class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        def rot(M):
            nonlocal n
            for r in range(n//2):
                for c in range(r,n-1-r):
                    #print(r,c,c,n-1-r,n-1-r,n-1-c,n-1-c,r)
                    M[r][c],M[c][n-1-r],M[n-1-r][n-1-c],M[n-1-c][r] = M[c][n-1-r],M[n-1-r][n-1-c],M[n-1-c][r],M[r][c]
                    #t = M[r][c]
                    #M[r][c] = M[c][n-1-r]
                    #M[c][n-1-r] = M[n-1-r][n-1-c]
                    #M[n-1-r][n-1-c] = M[n-1-c][r]
                    #M[n-1-c][r] = t
        def prt(M):
            #for r in M: print(r)
            #print()
            return
        def eq(M,N):
            return M == N
            #return all(M[i]==N[i] for i in range(n))
        prt(mat)
        if eq(mat,target): return True
        rot(mat);prt(mat)
        if eq(mat,target): return True
        rot(mat);prt(mat)
        if eq(mat,target): return True
        rot(mat);prt(mat)
        return eq(mat,target)
