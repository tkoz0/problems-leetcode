class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        R,C = len(image),len(image[0])
        q = [(sr,sc)]
        oc = image[sr][sc] # original color
        if oc != color:
            while len(q):
                q2 = []
                for r,c in q:
                    if 0 <= r < R and 0 <= c < C and image[r][c] == oc:
                        image[r][c] = color
                        q2 += [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
                q = q2
        return image
