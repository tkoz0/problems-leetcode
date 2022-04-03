class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        fracs = [(0,1),(1,1)]
        while True:
            newfracs = []
            anynew = False
            for i in range(len(fracs)-1):
                a,b = fracs[i]
                c,d = fracs[i+1]
                newfracs.append((a,b))
                if b+d <= n:
                    newfracs.append((a+c,b+d))
                    anynew = True
            if not anynew:
                break
            newfracs.append((1,1))
            fracs = newfracs
        return ["%d/%d"%frac for frac in fracs[1:-1]]
