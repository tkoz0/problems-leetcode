class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo,hi = 0,len(nums) # [lo,hi)
        while hi-lo > 1:
            mid = (lo+hi)//2 # split [lo,mid) and [mid,hi)
            if target >= nums[mid]:
                lo = mid
            else:
                hi = mid
        return lo+1 if nums[lo] < target else lo
