class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def helper(val):
            for key,value in numsMap.items():
                if value == val:
                    return key
        numsMap = {}
        for i in range(len(nums)):
            numsMap[i] = nums[i]
        for i in range(len(nums)):
            number = target - nums[i]
            if number in numsMap.values():
                numberIndex = helper(number)
                if not numberIndex == i:
                    return [numberIndex,i]
        



            
        