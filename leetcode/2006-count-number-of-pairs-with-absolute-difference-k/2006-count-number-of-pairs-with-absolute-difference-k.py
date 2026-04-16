class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        for num in nums:
            count += nums.count(num-k)
            count += nums.count(num+k)
        return count//2
        