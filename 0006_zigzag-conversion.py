class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        # rows mod 2r-2 (where r=numRows)
        m = 2*numRows-2
        ret = s[::m]
        def interleave(s1,s2): # where len(s1) = len(s2) + (0 or 1)
            #print(s1,s2)
            r = ''.join(s1[i//2] if i%2==0 else s2[i//2] for i in range(2*len(s2)))
            return r if len(s1) == len(s2) else r+s1[-1]
        for i in range(1,numRows-1): # middle rows
            # mod 1,2r-2-i
            s1 = s[i:][::m]
            s2 = s[2*numRows-2-i:][::m]
            ret += interleave(s1,s2)
        ret += s[numRows-1:][::m]
        return ret
