class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        def recur(i,f): # i = next index, f = list, f.length >= 2
            if i == len(num):
                return f
            if num[i] == '0':
                if f[-2]+f[-1]==0:
                    return recur(i+1,f+[0])
                return []
            for j in range(i+1,len(num)+1):
                n = int(num[i:j])
                if n >= 2**31:
                    break
                if f[-2]+f[-1]==n:
                    r = recur(j,f+[n])
                    if len(r):
                        return r
            return []
        for i in range(1,len(num)):
            for j in range(i+1,len(num)):
                if i-0>=2 and num[0]=='0':
                    continue
                if j-i>=2 and num[i]=='0':
                    continue
                ii = int(num[:i])
                jj = int(num[i:j])
                if ii >= 2**31 or jj >= 2**31:
                    continue
                r = recur(j,[ii,jj])
                if r:
                    return r
        return []
