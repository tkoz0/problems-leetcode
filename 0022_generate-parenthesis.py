class Solution:
    def recur(self,n:int) -> List[str]:
        if self.pars[n]: return self.pars[n]
        if n == 0:
            self.pars[n] = [""]
        elif n == 1:
            self.pars[n] = ["()"]
        else:
            result = []
            for inside in range(n):
                after = n-1-inside
                inside_pars = self.recur(inside)
                after_pars = self.recur(after)
                for a in inside_pars:
                    for b in after_pars:
                        result.append("("+a+")"+b)
            self.pars[n] = result
        return self.pars[n]
    def generateParenthesis(self, n: int) -> List[str]:
        self.pars = [None]*9
        return self.recur(n)
