class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left,right+1):
            flag = False
            for j in range(len(ranges)):
                if i >= ranges[j][0] and i <= ranges[j][1]:
                    flag = True
                    break
                else:
                    continue
            if not flag:
                return False
        return True
                
                
        