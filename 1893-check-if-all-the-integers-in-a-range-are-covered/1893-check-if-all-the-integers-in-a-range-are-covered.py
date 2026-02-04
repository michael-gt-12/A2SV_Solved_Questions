class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left,right+1):
            flag = True
            for j in range(len(ranges)):
                if i not in ranges[j]:
                    continue
                else:
                    flag = False
                    break
            if flag:
                return False
        return True
                
                
        