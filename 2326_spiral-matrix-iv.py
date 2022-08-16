# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat = [[-1]*n for _ in range(m)]
        r,c = 0,0
        mat[r][c] = head.val
        head = head.next
        while head:
            while head and c+1 < n and mat[r][c+1] == -1: # right
                c += 1
                mat[r][c] = head.val
                head = head.next
            while head and r+1 < m and mat[r+1][c] == -1: # down
                r += 1
                mat[r][c] = head.val
                head = head.next
            while head and c-1 >= 0 and mat[r][c-1] == -1: # left
                c -= 1
                mat[r][c] = head.val
                head = head.next
            while head and r-1 >= 0 and mat[r-1][c] == -1: # up
                r -= 1
                mat[r][c] = head.val
                head = head.next
        return mat
