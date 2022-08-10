# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p = headA
        lenA = 0
        while p:
            p = p.next
            lenA += 1
        p = headB
        lenB = 0
        while p:
            p = p.next
            lenB += 1
        tort = headA.next
        if not tort:
            tort = headB
        hare = tort.next # when reach end, loop to headB
        if not hare:
            hare = headB
        steps = 0
        #print('start',tort.val,hare.val)
        while tort != hare and steps < lenA+lenB: # if cycle, will find in limited steps
            steps += 1
            tort = tort.next
            if not tort:
                tort = headB
            hare = hare.next
            if not hare:
                hare = headB
            hare = hare.next
            if not hare:
                hare = headB
            #print('mid',tort.val,hare.val)
        if tort != hare:
            return None
        #print('found cycle',tort)
        tort = headA
        #print('find start of cycle',tort.val,hare.val)
        while tort and tort != hare: # move 1 step each to find start of cycle
            tort = tort.next
            hare = hare.next
            if not hare:
                hare = headB
            #print('mid',tort.val,hare.val)
        return tort # if no cycle, reaches end of list B
