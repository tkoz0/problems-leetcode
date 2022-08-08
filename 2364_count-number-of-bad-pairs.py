class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        nmi = dict() # nums[i]-i value -> count
        for i,n in enumerate(nums):
            if n-i not in nmi:
                nmi[n-i] = 0
            nmi[n-i] += 1
        good_pairs = 0
        for n in nmi.values():
            good_pairs += n*(n-1)//2
        return len(nums)*(len(nums)-1)//2 - good_pairs
