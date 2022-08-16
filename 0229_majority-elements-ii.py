class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        maj = len(nums)//3
        freq = dict()
        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n] += 1
        return [k for k in freq if freq[k] > maj]
