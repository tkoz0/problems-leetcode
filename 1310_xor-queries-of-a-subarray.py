class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        cache = [0]*(len(arr)+1)
        for i,n in enumerate(arr):
            cache[i+1] = cache[i]^n
        return [cache[j+1]^cache[i] for i,j in queries]
