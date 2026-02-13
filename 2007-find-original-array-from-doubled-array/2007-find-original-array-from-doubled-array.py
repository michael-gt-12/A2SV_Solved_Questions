class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        import copy
        check = copy.deepcopy(changed)
        result = []
        for num in changed:
            double = num * 2
            if num in check and double in check:
                if num == double:
                    if check.count(num) == 1:
                        continue
                else:
                    result.append(num)
                    check.remove(num)
                    check.remove(double)
        if not check:
            return result
        else:
            return []
        # original_map = {}

        # for num in changed:
        #     original_map[num] = num * 2
        
        # result = []

        # for item in original_map.items():
        #     if item[0] in changed and item[1] in changed:
        #         print(item[0])
        #         print(item[1])
        #         result.append(item[0])
        #         result.append(item[1])

        # result.sort()
        # changed.sort()

        # if result == changed:
        #     answer = []
        #     for i in range(0,len(result),2):
        #         answer.append(result[i])
        #     return answer
        # else:
        #     return []

        