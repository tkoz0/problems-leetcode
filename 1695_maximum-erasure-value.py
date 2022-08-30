class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        next_i = 1
        start_i = 0
        num_set = set(nums[:1])
        num_set_sum = nums[0]
        ret = nums[0]
        while next_i < len(nums):
            if nums[next_i] in num_set: # dupe, must remove prev to add it
                while nums[start_i] != nums[next_i]:
                    num_set.remove(nums[start_i])
                    num_set_sum -= nums[start_i]
                    start_i += 1
                num_set.remove(nums[start_i])
                num_set_sum -= nums[start_i]
                start_i += 1
            num_set.add(nums[next_i])
            num_set_sum += nums[next_i]
            ret = max(ret,num_set_sum)
            next_i += 1
            #print(num_set,num_set_sum)
        return ret
