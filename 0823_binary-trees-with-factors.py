class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        trees = dict() # map root -> num trees
        for n in sorted(arr):
            count = 1 # no root
            for d in trees.keys(): # sorted order because python3 dict
                if d*d > n: # maintains order of left subtree <= right subtree
                    break
                elif n%d == 0 and n//d in trees: # subtrees n,n//d and n//d,n
                    count += ((1 if d*d==n else 2)*trees[d]*trees[n//d])%(10**9+7)
            trees[n] = count%(10**9+7)
        return sum(trees.values())%(10**9+7)
