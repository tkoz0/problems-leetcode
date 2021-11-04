class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        assert len(nums) % 2 == 1
        lo, hi = 0, len(nums)-1
        while lo < hi:
            # split to [lo,mid] and [mid+1,hi]
            mid = (lo+hi)//2
            # ensure [lo,mid] doesn't break a consecutive pair
            if nums[mid] == nums[mid+1]:
                mid += 1
                # ensure mid does not increase to equal hi
                if mid == hi:
                    mid -= 2
            # pick odd length half
            if (hi-mid) % 2 == 1:
                lo = mid+1
            else:
                hi = mid
        return nums[lo]
