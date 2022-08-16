class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        cache = [0]
        for n in arr:
            cache.append(cache[-1]^n)
        return [cache[j+1]^cache[i] for i,j in queries]
