class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        freq = dict()
        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n] += 1
        pairs = sum(z//2 for z in freq.values())
        return [pairs,len(nums)-2*pairs]
