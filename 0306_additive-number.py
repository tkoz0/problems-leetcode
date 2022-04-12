class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def recur(i,a,b): # i = next index, a,b = prev 2 nums
            return i == len(num) or any(recur(j,b,int(num[i:j])) for j in range(i+1,len(num)+1) if a+b==int(num[i:j]) and (num[i] != '0' or j-i==1))
        return any(recur(j,int(num[:i]),int(num[i:j])) for i in range(1,len(num)) for j in range(i+1,len(num)) if (num[0] != '0' or i-0==1) and (num[i] != '0' or j-i==1))
