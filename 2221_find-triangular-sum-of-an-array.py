class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        # this is like pascal's triangle
        # a b c d e (1)
        # a+b b+c c+d d+e (1 1)
        # a+2b+c b+2c+d c+2d+e (1 2 1)
        # a+3b+3c+d b+3c+3d+e (1 3 3 1)
        # a+4b+6c+4d+e (1 4 6 4 1)
        # answer is sum (len(nums)-1 choose i) nums[i] for i=0 to i=n-1
        while len(nums) > 1:
            for i in range(len(nums)-1):
                nums[i] += nums[i+1]
                nums[i] %= 10
            nums.pop()
        return nums[0]
