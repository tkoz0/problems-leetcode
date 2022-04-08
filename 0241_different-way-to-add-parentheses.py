class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        nums = list(map(int,expression.replace('+',' ').replace('-',' ').replace('*',' ').split()))
        ops = [c for c in expression if c in '+-*']
        assert len(ops)+1 == len(nums)
        vals = dict() # (i,j) -> list(int) (values possible for nums[i:j])
        self.recur(nums,ops,vals,0,len(nums))
        return list(vals[(0,len(nums))])
    lams = {'+':lambda x,y:x+y,'-':lambda x,y:x-y,'*':lambda x,y:x*y}
    def recur(self,nums,ops,vals,i,j):
        if (i,j) in vals:
            return
        if i+1 == j:
            vals[(i,j)] = [nums[i]]
        else:
            vals[(i,j)] = []
            for k in range(i+1,j):
                # split to nums[i:k],nums[k:j]
                self.recur(nums,ops,vals,i,k)
                self.recur(nums,ops,vals,k,j)
                A = vals[(i,k)]
                B = vals[(k,j)]
                vals[(i,j)] += [Solution.lams[ops[k-1]](a,b) for a in A for b in B]
