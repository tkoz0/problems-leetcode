class Solution:
    def qpop(self,Q):
        Q[0] = Q[-1]
        Q.pop()
        i = 0
        while 2*i+1 < len(Q):
            j = i
            if Q[2*i+1][0] > Q[j][0]:
                j = 2*i+1
            if 2*i+2 < len(Q) and Q[2*i+2][0] > Q[j][0]:
                j = 2*i+2
            if j == i:
                break
            else:
                Q[i],Q[j] = Q[j],Q[i]
                i = j
    def qpush(self,Q,e):
        i = len(Q)
        Q.append(e)
        while i > 0 and Q[(i-1)//2][0] < Q[i][0]:
            Q[i],Q[(i-1)//2] = Q[(i-1)//2],Q[i]
            i = (i-1)//2
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        S = [nums[0]]
        Q = [(S[0],0)] # maintain max heap of S values and indexes
        for i in range(1,len(nums)):
            # basic solution that is too slow, just to check work
            #bestsum = 0
            #for j in range(max(0,i-k),i):
            #    if S[j] > bestsum:
            #        bestsum = S[j]
            #S.append(bestsum + nums[i])
            while Q[0][1] < i-k: # pop elements not in current k window
                self.qpop(Q)
            # use best in k window or 0 if they are all negative
            S.append(max(Q[0][0],0) + nums[i])
            self.qpush(Q,(S[-1],i))
        print(S)
        return max(S)
