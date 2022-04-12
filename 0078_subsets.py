class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def recur(nums,i,l):
            if i == len(nums):
                ret.append(l)
            else:
                recur(nums,i+1,l)
                recur(nums,i+1,l+[nums[i]])
        recur(nums,0,[])
        return ret
