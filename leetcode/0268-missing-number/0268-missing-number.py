class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numsSum = sum(nums)
        total = (len(nums) + 1) * len(nums)/2
        return int(total - numsSum)
        
        

            

