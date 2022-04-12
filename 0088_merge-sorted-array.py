class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m-1,-1,-1):
            nums1[i+n] = nums1[i]
        i1 = n # next in nums1
        i2 = 0 # next in nums2
        i = 0 # insertion position
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] < nums2[i2]:
                nums1[i] = nums1[i1]
                i1 += 1
            else:
                nums1[i] = nums2[i2]
                i2 += 1
            i += 1
        while i1 < len(nums1):
            nums1[i] = nums1[i1]
            i1 += 1
            i += 1
        while i2 < len(nums2):
            nums1[i] = nums2[i2]
            i2 += 1
            i += 1
