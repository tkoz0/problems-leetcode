class Solution:
    def divandconq(self,arr,k) -> int:
        if len(arr) == 1:
            if arr[0]%k == 0:
                return 1
            else:
                return 0
        else:
            m = len(arr)//2
            arr1 = arr[:m] # left
            arr2 = arr[m:] # right
            t1 = self.divandconq(arr1,k)
            t2 = self.divandconq(arr2,k)
            ret = t1 + t2 # subarrays not sharing between both halfs
            lcache = dict() # map mod k val count arr1[i:m] subarrays
            s = 0
            for z in arr1[::-1]: # cache subarrays of arr1 including arr1[m-1]
                s += z
                if s%k not in lcache:
                    lcache[s%k] = 0
                lcache[s%k] += 1
            s = 0
            for z in arr2: # go through arr2 counting shared subarrays
                s += z
                y = k - (s%k) # sum needed to get mod k = 0
                if y == k:
                    y = 0
                if y in lcache:
                    ret += lcache[y]
            return ret
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        #return self.divandconq(nums,k)
        freq = dict()
        freq[0] = 1 # the "empty" prefix
        s = 0
        ret = 0
        for n in nums:
            s += n
            if s%k not in freq:
                freq[s%k] = 0
            ret += freq[s%k]
            freq[s%k] += 1
        return ret
