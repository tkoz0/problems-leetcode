class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # index distance <= k
        # value difference <= t
        if t == 0: # special case, must be same number
            window = dict() # multiset: num -> count
            for i in range(min(k,len(nums))):
                if nums[i] not in window:
                    window[nums[i]] = 0
                window[nums[i]] += 1
                if window[nums[i]] > 1:
                    return True
            for i in range(k,len(nums)):
                if nums[i] in window:
                    return True
                window[nums[i]] = 1
                window[nums[i-k]] -= 1
                if window[nums[i-k]] == 0:
                    del window[nums[i-k]]
            return False
        window = dict() # map num//k -> multiset (num -> count) and track min/max
        def w_ins(n):
            if n//t not in window:
                window[n//t] = [dict(),n,n] # num->count, min, max
            if n not in window[n//t][0]:
                window[n//t][0][n] = 0
            window[n//t][0][n] += 1
            window[n//t][1] = min(window[n//t][1],n)
            window[n//t][2] = max(window[n//t][2],n)
        def w_rem(n):
            # remove n assuming it is already in window object
            window[n//t][0][n] -= 1
            if window[n//t][0][n] == 0:
                del window[n//t][0][n]
                if len(window[n//t][0]) == 0:
                    del window[n//t]
                else: # update min/max
                    if n == window[n//t][1]:
                        window[n//t][1] = min(window[n//t].keys())
                    if n == window[n//t][2]:
                        window[n//t][2] = max(window[n//t].keys())
        def has_nearby(n): # n may not be in window object
            if n//t in window:
                return True
            # check adjacent buckets
            if n//t+1 in window and window[n//t+1][1] <= n+t:
                return True
            if n//t-1 in window and window[n//t-1][2] >= n-t:
                return True
            return False
        for i in range(min(k,len(nums))):
            if has_nearby(nums[i]):
                return True
            w_ins(nums[i])
        for i in range(k,len(nums)):
            if has_nearby(nums[i]):
                return True
            w_ins(nums[i])
            w_rem(nums[i-k])
        return False
