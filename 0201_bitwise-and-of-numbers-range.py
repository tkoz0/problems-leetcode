class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ret = 0
        bit = 1
        lower = 0
        while bit <= left:
            #print(f'bit = {bit}')
            if left & bit:
                change = left + bit - (left & (bit - 1))
                #print(f'change = {change}')
                if change > right:
                    ret |= bit
                    #print(f'set bit')
                lower |= bit
            bit <<= 1
        return ret
