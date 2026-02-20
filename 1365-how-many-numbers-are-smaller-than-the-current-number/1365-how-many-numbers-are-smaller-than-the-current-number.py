class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        Snums = sorted(nums)
        for i in nums:
            result.append(Snums.index(i))
        return result