class Solution:
    def calculate(self, s: str) -> int:
        s = ''.join(c for c in s if c != ' ')
        i = 0
        pmsplit = [] # split by +-
        for j,c in enumerate(s):
            if c in '+-':
                pmsplit.append(s[i:j])
                pmsplit.append(c)
                i = j+1
        pmsplit.append(s[i:])
        #print(pmsplit)
        for i in range(0,len(pmsplit),2):
            # convert each multdiv into an integer
            mdsplit = []
            j = 0
            for k,c in enumerate(pmsplit[i]):
                if c in '*/':
                    mdsplit.append(pmsplit[i][j:k])
                    mdsplit.append(c)
                    j = k+1
            mdsplit.append(pmsplit[i][j:])
            #print(i,mdsplit)
            val = int(mdsplit[0])
            for j in range(1,len(mdsplit),2):
                if mdsplit[j] == '*':
                    val *= int(mdsplit[j+1])
                else:
                    val //= int(mdsplit[j+1])
            pmsplit[i] = val
        val = pmsplit[0]
        for i in range(1,len(pmsplit),2):
            if pmsplit[i] == '+':
                val += pmsplit[i+1]
            else:
                val -= pmsplit[i+1]
        return val
