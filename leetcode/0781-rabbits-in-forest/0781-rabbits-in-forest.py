from collections import Counter
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        result = 0
        
        for key, value in count.items():
            group_size = key + 1
            groups = math.ceil(value / group_size)
            result += groups * group_size
        
        return result