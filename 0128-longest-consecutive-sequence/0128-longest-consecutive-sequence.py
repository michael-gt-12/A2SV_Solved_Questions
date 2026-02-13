class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_length = 0
        for item in nums:
            current = item
            if current - 1 not in nums:
                length = 1
                while current + 1 in nums:
                    current += 1
                    length += 1
                max_length = max(max_length,length)
        return max_length

        
        