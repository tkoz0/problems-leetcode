class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        L = [[0]*(301)]
        # L[i][j] = ways for 2 nums in arr[:i+1] to sum to j
        prevcounts = {arr[0]:1}
        for n in arr[1:]:
            L.append(L[-1][:]) # if n not included
            for m in prevcounts:
                #print(len(L),len(L[-1]),m+n,prevcounts)
                L[-1][m+n] += prevcounts[m]
            L[-1] = [z%(10**9+7) for z in L[-1]]
            if n not in prevcounts:
                prevcounts[n] = 0
            prevcounts[n] += 1
        #for z in L: print('L',z[:20])
        LL = [[0]*(301),[0]*(301)]
        # LL[i][j] = ways for 3 nums in arr[:i+1] to sum to j
        arr_i = 2
        for n in arr[2:]:
            LL.append(LL[-1][:])
            for i in range(target-n+1):
                LL[-1][i+n] += L[arr_i-1][i]
            LL[-1] = [z%(10**9+7) for z in LL[-1]]
            arr_i += 1
        #for z in LL: print('LL',z[:20])
        return LL[-1][target]
