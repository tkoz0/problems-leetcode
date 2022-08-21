class Solution:
    def numDecodings(self, s: str) -> int:
        ways = [1]+[0]*len(s)
        ways[1] = 9 if s[0]=='*' else (0 if s[0]=='0' else 1)
        for i in range(2,len(s)+1):
            if s[i-1] == '*':
                ways[i] += 9*ways[i-1] # (*) group with single *
                if s[i-2] == '*':
                    ways[i] += 15*ways[i-2] # (**) group of double * (encode 11-19 or 21-26)
                else: # digit and *
                    if s[i-2] == '1': # 11-19
                        ways[i] += 9*ways[i-2] # (1*)
                    elif s[i-2] == '2': # 21-26
                        ways[i] += 6*ways[i-2] # (2*)
            else: # s[i-1] is digit
                if s[i-1] != '0':
                    ways[i] += ways[i-1] # (d) single nonzero digit
                    d = int(s[i-1])
                    if s[i-2] == '*':
                        ways[i] += (1 if d>6 else 2)*ways[i-2] # (*d)
                    elif s[i-2] in '12':
                        ways[i] += (1 if s[i-2] == '1' or d<=6 else 0)*ways[i-2] # (1d|2d)
                else: # s[i-1] == '0'
                    # single 0 digit not allowed
                    if s[i-2] == '*':
                        ways[i] += 2*ways[i-2] # (*0)
                    elif s[i-2] in '12':
                        ways[i] += ways[i-2] # (10|20)
            ways[i] %= 10**9+7
        return ways[-1]
