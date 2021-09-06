class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for ring in range(len(matrix)//2):
            side = len(matrix)-2*ring-1
            # pick a ring, represented by 4 segments
            # rotate each corresponding 4 elements
            for pos in range(side):
                matrix[ring][ring+pos],matrix[ring+pos][ring+side],matrix[ring+side][ring+side-pos],matrix[ring+side-pos][ring] = \
                    matrix[ring+side-pos][ring],matrix[ring][ring+pos],matrix[ring+pos][ring+side],matrix[ring+side][ring+side-pos]
