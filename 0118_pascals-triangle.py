class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = [[1]]
        while len(ret) < numRows:
            a=ret[-1]+[0]
            b=[0]+ret[-1]
            ret.append([a[i]+b[i] for i in range(len(a))])
        return ret
