class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        i = 0

        while i + 2 < len(nums):
            if nums[i] == 1:
                i += 1
                continue

            j = i
            while j <= i + 2:
                if nums[j] == 1:
                    nums[j] = 0
                else:
                    nums[j] = 1
                j += 1

            count += 1
            i += 1

        if nums.count(1) == len(nums):
            return count 
        else:
            return -1




        