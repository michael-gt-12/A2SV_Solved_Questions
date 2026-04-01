class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = 0
        min_prefix = 0
        maximum = nums[0]

        for num in nums:
            prefix += num
            maximum = max(maximum, prefix - min_prefix)
            min_prefix = min(min_prefix, prefix)

        return maximum