class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        freq = Counter(nums)
        result = []
        for item in freq.items():
            if item[1] > floor(len(nums)/3):
                result.append(item[0])
        return result
        