class Solution:
    def countHomogenous(self, s: str) -> int:
        count = 0
        prevchar = ''
        homlen = 0
        for c in s:
            if c == prevchar:
                homlen += 1
            else:
                count += homlen*(homlen+1)//2
                prevchar = c
                homlen = 1
        return (count + homlen*(homlen+1)//2)%(10**9+7)
