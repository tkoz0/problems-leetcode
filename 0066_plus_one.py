class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d = digits[::-1]
        done = False
        for i in range(len(d)):
            d[i] += 1
            if d[i] == 10:
                d[i] = 0
                done = False
            else:
                done = True
                break
        if not done:
            d.append(1)
        return d[::-1]
