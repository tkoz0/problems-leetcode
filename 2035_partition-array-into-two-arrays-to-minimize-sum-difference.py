class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)//2
        ss = sum(nums)
        left = dict() # left half subsets map: size -> sums possible
        for i in range(n+1):
            left[i] = []
        def recur1(size_,sum_,i):
            nonlocal left
            if i == n:
                left[size_].append(sum_)
            else:
                recur1(size_,sum_,i+1)
                recur1(size_+1,sum_+nums[i],i+1)
        recur1(0,0,0)
        for i in range(n+1):
            left[i] = sorted(left[i])
        #print(left)
        best = abs(sum(nums[:n])-sum(nums[n:]))
        def recur2(size_,sum_,i):
            nonlocal best
            if i == 2*n:
                ohsum = left[n-size_]
                lo,hi = 0,len(ohsum)-1
                while lo != hi:
                    mid = (lo+hi)//2
                    test = ss - 2*(sum_ + ohsum[mid])
                    if test > 0:
                        lo = mid+1
                    else:
                        hi = mid
                best = min(abs(ss-2*(sum_+ohsum[lo])),best)
                if lo < len(ohsum)-1:
                    best = min(abs(ss-2*(sum_+ohsum[lo+1])),best)
                #b = min(abs(2*(sum_+s) - ss) for s in left[n-size_])
                #best = min(b,best)
            else:
                recur2(size_,sum_,i+1)
                recur2(size_+1,sum_+nums[i],i+1)
        recur2(0,0,n)
        return best
