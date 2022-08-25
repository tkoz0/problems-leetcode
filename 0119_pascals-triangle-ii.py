class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        a=[1]
        while len(a) < rowIndex+1:
            a.append(0)
            b=[0]+a
            a=[a[i]+b[i] for i in range(len(a))]
        return a
