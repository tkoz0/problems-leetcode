class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        mid = 0
        for i in range(1,len(nums)):
            if abs(nums[i]) <= abs(nums[mid]):
                mid = i
            else:
                break
        li = mid
        ri = mid+1
        ret = []
        while li >= 0 and ri < len(nums):
            if abs(nums[li]) < abs(nums[ri]):
                ret.append(nums[li]**2)
                li -= 1
            else:
                ret.append(nums[ri]**2)
                ri += 1
        while li >= 0:
            ret.append(nums[li]**2)
            li -= 1
        while ri < len(nums):
            ret.append(nums[ri]**2)
            ri += 1
        return ret
