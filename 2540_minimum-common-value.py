class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        while True:
            while i < len(nums1) and nums1[i] < nums2[j]:
                i += 1
            if i >= len(nums1):
                return -1
            while j < len(nums2) and nums2[j] < nums1[i]:
                j += 1
            if j >= len(nums2):
                return -1
            if nums1[i] == nums2[j]:
                return nums1[i]
