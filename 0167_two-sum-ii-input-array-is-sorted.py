class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i,n in enumerate(numbers):
            lo,hi = i+1,len(numbers) # binary search
            while lo+1 < hi:
                mid = (lo+hi)//2
                if numbers[mid] <= target-n:
                    lo = mid
                else:
                    hi = mid
            if numbers[lo]+n == target:
                return [i+1,lo+1]
