from collections import Counter

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        
        count = Counter(changed)
        changed.sort()
        
        result = []
        
        for x in changed:
            if count[x] == 0:
                continue
            
            if count[2 * x] <= 0:
                return []
            
            result.append(x)
            count[x] -= 1
            count[2 * x] -= 1
        
        return result