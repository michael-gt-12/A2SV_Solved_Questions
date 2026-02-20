class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        k = len(arr)
        
        while k > 1:
            indx = arr.index(k)
            
            if indx == k - 1:
                k -= 1
                continue
            
            if indx != 0:
                arr[:indx+1] = reversed(arr[:indx+1])
                result.append(indx+1)
            
            arr[:k] = reversed(arr[:k])
            result.append(k)
            
            k -= 1
            
        return result