class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [False]*len(nums)
        best = 0
        for i,n in enumerate(nums):
            if visited[n]:
                continue
            visited[n] = True
            j = nums[n]
            path = 1
            while j != n:
                visited[j] = True
                path += 1
                j = nums[j]
            best = max(best,path)
        return best
