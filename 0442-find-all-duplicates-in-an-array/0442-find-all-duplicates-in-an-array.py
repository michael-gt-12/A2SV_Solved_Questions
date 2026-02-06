from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums_dict = Counter(nums)
        result = []
        for key in nums_dict:
            if nums_dict[key] == 2:
                result.append(key)
        return result
        