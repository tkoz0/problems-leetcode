class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers = [sum(1 for x in row if x) for row in mat]
        roworder = list(range(len(mat)))
        roworder = sorted(roworder,key=lambda i:(soldiers[i],i))
        return roworder[:k]
