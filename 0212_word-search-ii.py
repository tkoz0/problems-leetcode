class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # word dictionary mapping prefixes -> is a word
        W = dict()
        for word in words:
            # add prefixes
            for l in range(len(word)):
                if word[:l] not in W:
                    W[word[:l]] = False
            W[word] = True
        #print(W)
        # recursion continues as long as the prefix is in W
        # if the current prefix maps to True, output that word
        used = [[False]*len(board[0]) for _ in range(len(board))]
        out = set() # store words
        for r in range(len(board)):
            for c in range(len(board[r])):
                self.search(board,W,used,'',r,c,out)
        return list(out)
        # a better solution would use a trie and remove found words
        # since a word only need to be found once, it is unnecessary
        # to branch for the same word afterwards
    def search(self,board,W,used,prefix,r,c,output):
        # check bounds
        if not (0 <= r < len(board)): return
        if not (0 <= c < len(board[0])): return
        if used[r][c]: return # must be unused letter
        prefix += board[r][c]
        #print(prefix)
        if prefix not in W: return # dont recurse non prefixes
        if W[prefix]: output.add(prefix) # is a word
        used[r][c] = True
        # search adjacent
        self.search(board,W,used,prefix,r+1,c,output)
        self.search(board,W,used,prefix,r-1,c,output)
        self.search(board,W,used,prefix,r,c+1,output)
        self.search(board,W,used,prefix,r,c-1,output)
        # backtrack
        used[r][c] = False
