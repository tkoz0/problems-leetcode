class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1i = {r:i for i,r in enumerate(list1)} # restaurant -> index
        bests = dict() # sum -> restaurants
        for i,rest in enumerate(list2):
            if rest in list1i:
                isum = i+list1i[rest]
                if isum not in bests:
                    bests[isum] = []
                bests[isum].append(rest)
        return bests[min(bests.keys())]
