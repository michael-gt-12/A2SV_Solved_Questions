class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        placeholder = 0
        for seeker in range(n):
            if nums[seeker] != 0:
                temp = nums[placeholder]
                nums[placeholder] = nums[seeker]
                nums[seeker] = temp
                placeholder += 1

        