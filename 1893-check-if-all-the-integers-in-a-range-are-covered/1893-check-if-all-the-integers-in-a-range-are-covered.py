class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # could not pass testcase 102 /106

        # ranges.sort()
        # pointer = 0
        # while pointer < len(ranges):           
        #     if left >= ranges[pointer][0]:
        #         if right <= ranges[pointer][1]:
        #             return True
        #         else:
        #             while pointer < len(ranges):
        #                 if right <= ranges[pointer][1] and right >= ranges[pointer][0]:
        #                     return True
        #                 else:
        #                     pointer += 1
        #     else:
        #         pointer += 1
        # return False
            
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
                
                
        