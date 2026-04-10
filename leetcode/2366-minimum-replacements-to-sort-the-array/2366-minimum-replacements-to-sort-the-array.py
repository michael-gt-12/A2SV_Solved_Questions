class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count = 0
        previous = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= previous:
                previous = nums[i]
                continue

            k = (nums[i] + previous - 1) // previous
            count += k - 1
            previous = nums[i] // k

        return count