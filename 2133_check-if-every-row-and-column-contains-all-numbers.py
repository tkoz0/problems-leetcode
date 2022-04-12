class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        v = set(range(1,n+1))
        return all(set(r)==v for r in matrix) and all(set(matrix[r][c] for r in range(n))==v for c in range(n))
