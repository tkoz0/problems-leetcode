class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def r(arr):
            n=len(arr)
            if n == 2:
                return arr
            else:
                left=r(arr[:n//2])
                right=r(arr[n//2:])
                return [min(left),max(right)]
        return min(r(nums))
