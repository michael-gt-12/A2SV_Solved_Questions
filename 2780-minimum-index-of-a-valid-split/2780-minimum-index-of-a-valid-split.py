class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        from collections import Counter
        nums_map = Counter(nums)
        num = None
        freq = 0
        
        for key, value in nums_map.items():
            if value > freq:
                num = key
                freq = value

        left_indx = 0
        split_indx = 1
        left_count = 0
        
        while split_indx < len(nums):
            if nums[left_indx] == num:
                left_count += 1

            left_size = split_indx
            right_size = len(nums) - split_indx
            right_count = freq - left_count

            if left_count * 2 > left_size and right_count * 2 > right_size:
                return split_indx - 1

            split_indx += 1
            left_indx += 1

        return -1