class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        Lprev = [0]*301 # previous column needed
        L = [0]*301 # L[i][j] = num pairs of arr[:i+1] summing to j
        LL = [0]*301 # LL[i][j] = num triples of arr[:i+1] summing to j
        # only storing last column, loop starts at i=2
        prevcounts = {arr[0]:2} if arr[0]==arr[1] else {arr[0]:1,arr[1]:1}
        Lprev[arr[0]+arr[1]] = 1
        L[arr[0]+arr[1]] = 1
        for n in arr[2:]:
            for m in prevcounts:
                L[m+n] += prevcounts[m]
            if n not in prevcounts:
                prevcounts[n] = 0
            prevcounts[n] += 1
            for i in range(target-n+1):
                LL[i+n] += Lprev[i]
            Lprev = L[:]
        return LL[target]%(10**9+7)
