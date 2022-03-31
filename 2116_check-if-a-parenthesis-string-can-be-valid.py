class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        rmin,rmax = 0,0 # delta min/max
        # ( -> +1, ) -> -1
        # must end at 0, never go below 0
        for i in range(len(s)):
            if locked[i] == '1': # locked
                d = 1 if s[i] == '(' else -1
                rmin += d
                rmax += d
            else: # unlocked
                rmin -= 1
                rmax += 1
            if rmin < 0: # do not allow negative
                rmin += 2
            if rmin > rmax: # does not allow enough open (
                return False
        return rmin == 0
