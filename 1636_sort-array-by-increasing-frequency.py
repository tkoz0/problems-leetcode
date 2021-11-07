class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = dict() # number -> frequency
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        return sorted(nums, key = lambda x : 256*freq[x] - x)
