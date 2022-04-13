class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [1]*n
        acc = 1
        for i in range(n-1):
            acc *= nums[i]
            ret[i+1] *= acc
        acc = 1
        for i in range(n-1,0,-1):
            acc *= nums[i]
            ret[i-1] *= acc
        return ret
        '''
        n = len(nums)
        left = [0]*n
        right = [0]*n
        left[0] = nums[0]
        right[-1] = nums[-1]
        for i in range(1,n):
            left[i] = nums[i]*left[i-1]
        for i in range(n-2,-1,-1):
            right[i] = nums[i]*right[i+1]
        ret = [0]*n
        ret[0] = right[1]
        ret[-1] = left[-2]
        for i in range(1,n-1):
            ret[i] = left[i-1]*right[i+1]
        return ret
        '''
