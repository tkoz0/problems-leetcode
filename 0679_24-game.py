from fractions import Fraction

# binary operators that can always be used
# division uses / because Fraction is being used for more flexibility
ops = \
{
    '+': lambda x,y : x+y,
    '-': lambda x,y : x-y,
    '*': lambda x,y : x*y,
    '/': lambda x,y : x/y
}

# generator for multiset partitions: sequence of tuples with 2 lists each
# ms is list of (x,i) where each x is unique and each i >= 1
# represents amount of each x to pick from
def multiset_partitions(ms,i=0,A=[],B=[]):
    if i == len(ms):
        yield A,B
    else:
        for j in range(1+ms[i][1]):
            yield from multiset_partitions(ms,i+1,
                                           A+[ms[i][0]]*j,
                                           B+[ms[i][0]]*(ms[i][1]-j))

# returns the list of (x,i) used by multiset_partitions()
def make_multiset(nums):
    ms = dict()
    for n in nums:
        if n not in ms:
            ms[n] = 0
        ms[n] += 1
    return list(ms.items())

# returns a dictionary mapping possible value to a parse tree for computing it
# the parse tree is represented as a Fraction or recursive list:
# [operation, left, right], left/right are recursive or Fraction
# operation is a string key from ops
search_cache = dict() # tuple(nums) -> S dict()
def search(nums):
    global search_cache
    if tuple(nums) in search_cache:
        return search_cache[tuple(nums)]
    assert len(nums) > 0
    for num in nums:
        assert type(num) == Fraction
    if len(nums) == 1:
        return {nums[0]:nums[0]}
    S = dict() # evaluated value (Fraction) -> expression
    for A,B in multiset_partitions(make_multiset(nums)):
        if len(A) == 0 or len(B) == 0: continue # both partitions nonempty
        A_vals = search(A) # Fraction -> expression
        B_vals = search(B) # Fraction -> expression
        for a in A_vals:
            for b in B_vals:
                for op in ops:
                    # try/except because zero division is possible
                    try:
                        r = ops[op](a,b)
                        if r not in S:
                            S[r] = [op,A_vals[a],B_vals[b]]
                    except:
                        continue
    search_cache[tuple(nums)] = S
    return S

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        return Fraction(24) in search(list(map(Fraction,cards)))
