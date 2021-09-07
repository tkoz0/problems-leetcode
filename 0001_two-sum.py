class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = dict() # value -> [indexes...]
        for i,v in enumerate(nums):
            if v not in lookup: lookup[v] = []
            lookup[v].append(i)
        for v in lookup:
            needed = target-v
            if needed == v: # must have duplicate
                if len(lookup[v]) >= 2:
                    return lookup[v][:2]
            elif needed in lookup: # remainder exists
                return [lookup[v][0],lookup[needed][0]]
        assert 0, 'no solution'
