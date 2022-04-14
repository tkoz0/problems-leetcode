class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ret = 0
        oddi = [i for i in range(len(nums)) if nums[i]%2==1]
        a,b = 0,k-1 # window
        while b < len(oddi):
            l = oddi[a] - (oddi[a-1] if a>0 else -1)
            r = (oddi[b+1] if b<(len(oddi)-1) else len(nums)) - oddi[b]
            ret += l*r
            a,b = a+1,b+1
        return ret
