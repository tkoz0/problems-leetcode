class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        cache = [arr] # cache[i][j] = xor of arr[2^i*j:2^i*(j+1)]
        blocklen = 1
        def xor_slow(i,j):
            x = 0
            for k in range(i,min(j,len(arr))):
                x ^= arr[k]
            return x
        while len(cache[-1]) > 1:
            row = []
            l = len(cache[-1]) - (len(cache[-1])%2)
            for i in range(0,l,2):
                row.append(cache[-1][i]^cache[-1][i+1])
            if l < len(cache[-1]):
                row.append(cache[-1][l])
            cache.append(row)
        #print(cache)
        def xor_fast(i,j):
            ret = 0
            while i < j:
                p = 0
                i2 = i # pick largest pow2 to use
                while i2%2==0 and i+2**(p+1) <= j:
                    p += 1
                    i2 //= 2
                ret ^= cache[p][i//2**p]
                i += 2**p
            return ret
        return [xor_fast(i,j+1) for i,j in queries]
