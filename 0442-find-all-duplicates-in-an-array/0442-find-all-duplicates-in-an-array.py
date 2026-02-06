from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = set()
        for i in range(len(nums)):
            if nums.count(nums[i]) == 2:
                result.add(nums[i])
        return list(result)

        # nums_dict = Counter(nums)
        # result = []
        # for key in nums_dict:
        #     if nums_dict[key] == 2:
        #         result.append(key)
        # return result
        