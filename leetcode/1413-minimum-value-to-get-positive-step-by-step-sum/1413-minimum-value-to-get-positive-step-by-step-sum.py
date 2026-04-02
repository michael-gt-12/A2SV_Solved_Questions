class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        total = 0
        prefix = []
        for num in nums:
            total += num
            prefix.append(total)
        
        minimum = min(prefix)
        if minimum >= 1:
            return 1
        else:
            return abs(minimum) + 1




        