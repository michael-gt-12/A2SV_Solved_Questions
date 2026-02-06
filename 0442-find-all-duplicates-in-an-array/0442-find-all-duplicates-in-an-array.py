from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                result.append(abs(num))
            else:
                nums[idx] = -nums[idx]
        return result
      
            
        # First solution

        # nums_dict = Counter(nums)
        # result = []
        # for key in nums_dict:
        #     if nums_dict[key] == 2:
        #         result.append(key)
        # return result
        