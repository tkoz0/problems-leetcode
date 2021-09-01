class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return list(filter(lambda x:self.selfDividing(x),range(left,right+1)))
    def selfDividing(self, x: int) -> bool:
        x2 = x
        while x2:
            x2,rem = divmod(x2,10)
            if rem == 0: return False
            if x % rem != 0: return False
        return True
