class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        result = 0
        total = 0
        prefix_map = {0 : 1}

        for num in nums:
            total += num
            diff = total - goal
            result += prefix_map.get(diff,0)
            prefix_map[total] = 1 + prefix_map.get(total,0)
        
        return result