class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        sums = [0]*(len(nums)-k+1) # given start index
        sums[-1] = sum(nums[-k:])
        for i in range(len(nums)-k-1,-1,-1):
            sums[i] = sums[i+1]+nums[i]-nums[i+k]
        # dp for 2 non overlapping
        best2 = [None]*(len(sums)-k) # give index of first array
        soln2 = [None]*(len(sums)-k)
        bestnext = len(best2)-1+k
        best2[-1] = sums[len(best2)-1]+sums[bestnext]
        soln2[-1] = [len(best2)-1,bestnext]
        for i in range(len(best2)-2,-1,-1):
            if sums[i+k] >= sums[bestnext]: # >= for lex min
                bestnext = i+k
            best2[i] = sums[i]+sums[bestnext]
            soln2[i] = [i,bestnext]
        print(best2)
        print(soln2)
        # dp for 3 non overlapping
        best3 = [None]*(len(best2)-k)
        soln3 = [None]*(len(best2)-k)
        bestnext = len(best3)-1+k
        best3[-1] = sums[len(best3)-1]+best2[bestnext]
        soln3[-1] = [len(best3)-1]+soln2[bestnext]
        for i in range(len(best3)-2,-1,-1):
            if best2[i+k] >= best2[bestnext]: # >= for lex min
                bestnext = i+k
            best3[i] = sums[i]+best2[bestnext]
            soln3[i] = [i]+soln2[bestnext]
        print(best3)
        print(soln3)
        # find lexicographic min solution
        i = 0
        for j in range(1,len(best3)):
            if best3[j] > best3[i]:
                i = j
        return list(soln3[i])
