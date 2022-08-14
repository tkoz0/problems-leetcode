# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def rev_group(a,b):
            #print(a.val,b.val if b else 'none')
            # a = start ptr, b = end ptr
            p = a
            e = b
            while p is not b:
                n = p
                p = p.next
                n.next = e
                e = n
            return e
        pprev = head
        p = head.next
        kk = k-1
        while kk > 0: # since n >= k
            kk -= 1
            pprev = pprev.next
            p = p.next
        ret = rev_group(head,p)
        #z=ret;zz=[]
        #while z:zz.append(z.val);z=z.next
        #print(zz)
        last_ptr = head # last node in reversed group
        while True: # reverse other groups
            p = last_ptr.next
            next_last_ptr = p
            kk = k
            while kk > 0 and p:
                kk -= 1
                p = p.next
            if kk > 0: # not enough nodes
                break
            last_ptr.next = rev_group(last_ptr.next,p)
            last_ptr = next_last_ptr
            #z=ret;zz=[]
            #while z:zz.append(z.val);z=z.next
            #print(zz)
        return ret
