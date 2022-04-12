class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        counts = dict() # bitwise or -> count
        def recur(nums,i,l,b):
            if i == len(nums):
                if b not in counts:
                    counts[b] = 0
                counts[b] += 1
            else:
                recur(nums,i+1,l,b)
                recur(nums,i+1,l,b|nums[i])
        recur(nums,0,[],0)
        return counts[max(counts.keys())]
