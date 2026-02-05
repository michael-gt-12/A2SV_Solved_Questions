class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result = []
        common = list(set(list1).intersection(set(list2)))
        isum = []
        for i in common:
            isum.append(list1.index(i) + list2.index(i))
        least = min(isum)
        c = isum.count(least)
        for i in range(c):
            result.append(common[isum.index(least)])
            isum[isum.index(least)] = "seen"
        return result



