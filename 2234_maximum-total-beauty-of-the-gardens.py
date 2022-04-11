class Node:
    def __init__(self,val,next_=None):
        self.val = val
        self.next = next_

class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        planted = [0]*len(flowers) # new amount planted in each garden
        # indexes starting with most/least flowers
        bymax = sorted(range(len(flowers)),key=lambda x:-flowers[x])
        #bymin = sorted(range(len(flowers)),key=lambda x:flowers[x])
        remaining = newFlowers # how many left to plant
        bestBeauty = 0
        fullGardens = 0 # calculated by first loop
        pghead = pgtail = None # partial gardens: list (numflowers,gardencount) increasing
        def spread_flowers(remaining,pghead,pgtail):
            # returns remaining,pghead,pgtail
            assert pghead and pgtail
            while remaining > 0 and pghead.val[0] < target-1:
                n,c = pghead.val
                if pghead.next:
                    ft = pghead.next.val[0]
                else:
                    ft = target-1
                if remaining >= c*(ft-n): # bump all to next level
                    remaining -= c*(ft-n)
                    pghead.val[0] = ft
                    if pghead.next and pghead.next.val[0] == ft: # merge with next
                        pghead.next.val[1] += c
                        pghead = pghead.next
                else: # spread out to current
                    addtoall = remaining//c
                    extra = remaining%c
                    n += addtoall
                    pghead.val[0] += addtoall
                    remaining -= addtoall*c
                    if extra != 0:
                        if not pghead.next: # append new node to move some
                            pghead.next = Node([n+1,extra])
                            pghead.val[1] -= extra
                            c -= extra
                            pgtail = pghead.next
                        elif pghead.next.val[0] == n+1: # merge into next node
                            pghead.next.val[1] += extra
                            pghead.val[1] -= extra
                            c -= extra
                        else: # insert new node
                            tmp = pghead.next
                            pghead.next = Node([n+1,extra])
                            pghead.val[1] -= extra
                            c -= extra
                            pghead.next.next = tmp
                        remaining -= extra
            return remaining,pghead,pgtail
        # fill gardens closest to target first
        for i,j in enumerate(bymax):
            if flowers[j] >= target: # already full
                fullGardens += 1
            elif target - flowers[j] <= remaining: # plant to fill
                planted[j] = target-flowers[j]
                remaining -= target-flowers[j]
                fullGardens += 1
            else: # fill emptygardens array for partial gardens
                for k in range(len(bymax)-1,i-1,-1):
                    j = bymax[k] # garden index
                    if not pghead:
                        pghead = pgtail = Node([flowers[j],1])
                    elif pgtail.val[0] == flowers[j]:
                        pgtail.val[1] += 1
                    else:
                        assert flowers[j] > pgtail.val[0]
                        pgtail.next = Node([flowers[j],1])
                        pgtail = pgtail.next
                remaining,pghead,pgtail = spread_flowers(remaining,pghead,pgtail)
                break
        bestBeauty = fullGardens*full + partial*(0 if not pghead else pghead.val[0])
        startK = len(bymax)-1 if not pghead else i-1
        for k in range(startK,-1,-1): # unfill gardens and spread to partials
            j = bymax[k] # garden index
            remaining += planted[j]
            if flowers[j] < target: # now have a partial garden
                fullGardens -= 1
                if not pghead: # insert
                    pghead = pgtail = Node([flowers[j],1])
                elif flowers[j] == pgtail.val[0]:
                    pgtail.val[1] += 1
                elif flowers[j] > pgtail.val[0]:
                    pgtail.next = Node([flowers[j],1])
                    pgtail = pgtail.next
                elif flowers[j] == pghead.val[0]:
                    pghead.val[1] += 1
                elif flowers[j] < pghead.val[0]:
                    tmp = pghead
                    pghead = Node([flowers[j],1])
                    pghead.next = tmp
                remaining,pghead,pgtail = spread_flowers(remaining,pghead,pgtail)
            flowermin = 0 if not pghead else pghead.val[0]
            bestBeauty = max(bestBeauty,fullGardens*full+partial*flowermin)
        return bestBeauty
